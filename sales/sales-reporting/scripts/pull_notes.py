# /// script
# requires-python = ">=3.9"
# dependencies = ["requests"]
# ///
"""
pull_notes.py — pull AE notes for a period + their associations + feature_gaps,
for the feature-request extraction step (the LLM classifier reads this output).

This is the DETERMINISTIC data layer. It does not classify — it just assembles
candidate notes with enough context to cite a source. Output:
tmp/notes-<label>.json, shaped for the classifier.

Usage (same timeframe interface as pull_pipeline.py):
    source ../../../.env  (set -a)   # or rely on the orchestrator's env
    uv run pull_notes.py                # current ISO week
    uv run pull_notes.py --weeks 4
    uv run pull_notes.py --week-start 2026-05-04 --week-end 2026-05-31

Notes:
- ALL AE-owned notes in the window are pulled (not just deal-associated). Notes
  associated only with a contact/company (no deal) are flagged `assoc_type` so we
  can decide later whether to filter them out.
- Each associated deal's `feature_gaps` (the structured checkbox taxonomy) is
  attached so the classifier can reconcile structured vs. free-text signal.
"""

import argparse
import datetime as dt
import json
import os
import re
import sys

import requests

import pull_pipeline as pp  # reuse resolve_period, to_ms, OWNERS, OWNER_IDS, token, search

BASE = "https://api.hubapi.com"
SALES_REPORTING = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def clean_body(raw):
    if not raw:
        return ""
    txt = re.sub(r"<[^>]+>", " ", raw)            # strip HTML tags
    txt = txt.replace("&nbsp;", " ").replace("&amp;", "&")
    txt = re.sub(r"\s+", " ", txt).strip()         # collapse whitespace
    return txt


def to_date(ts):
    if not ts:
        return ""
    ts = str(ts)
    if ts.isdigit():  # epoch ms
        return dt.datetime.utcfromtimestamp(int(ts) / 1000).date().isoformat()
    try:
        return dt.datetime.fromisoformat(ts.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        return ts[:10]


def batch_assoc(tok, from_obj, to_obj, ids):
    """v4 batch association read: {note_id: [associated_to_ids]} — one call for all ids."""
    if not ids:
        return {}
    headers = {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"}
    out = {}
    for i in range(0, len(ids), 100):  # v4 batch cap
        chunk = ids[i:i + 100]
        r = requests.post(
            f"{BASE}/crm/v4/associations/{from_obj}/{to_obj}/batch/read",
            headers=headers, json={"inputs": [{"id": x} for x in chunk]}, timeout=30,
        )
        r.raise_for_status()
        for res in r.json().get("results", []):
            # v4 returns toObjectId as an int; v3 batch-read keys are strings — coerce to str.
            out[str(res["from"]["id"])] = [str(t["toObjectId"]) for t in res.get("to", [])]
    return out


def batch_read(tok, obj, ids, properties):
    """v3 batch read by id: {id: {props}}."""
    if not ids:
        return {}
    headers = {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"}
    out = {}
    ids = list(ids)
    for i in range(0, len(ids), 100):
        chunk = ids[i:i + 100]
        r = requests.post(
            f"{BASE}/crm/v3/objects/{obj}/batch/read",
            headers=headers,
            json={"inputs": [{"id": x} for x in chunk], "properties": properties},
            timeout=30,
        )
        r.raise_for_status()
        for res in r.json().get("results", []):
            out[res["id"]] = res.get("properties", {})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--week-start")
    ap.add_argument("--week-end")
    ap.add_argument("--weeks", type=int)
    ap.add_argument("--out")
    args = ap.parse_args()

    start, end, label, period_label, num_weeks = pp.resolve_period(args)
    start_ms, end_ms = pp.to_ms(start), pp.to_ms(end, end=True)
    tok = pp.token()

    raw_notes = pp.search(tok, [
        {"propertyName": "hubspot_owner_id", "operator": "IN", "values": pp.OWNER_IDS},
        {"propertyName": "hs_timestamp", "operator": "GTE", "value": str(start_ms)},
        {"propertyName": "hs_timestamp", "operator": "LTE", "value": str(end_ms)},
    ], ["hs_note_body", "hs_timestamp", "hubspot_owner_id"], obj="notes")

    note_ids = [n["id"] for n in raw_notes]
    note_deals = batch_assoc(tok, "notes", "deals", note_ids)
    note_companies = batch_assoc(tok, "notes", "companies", note_ids)
    note_contacts = batch_assoc(tok, "notes", "contacts", note_ids)

    deal_ids = {d for ds in note_deals.values() for d in ds}
    company_ids = {c for cs in note_companies.values() for c in cs}
    deals = batch_read(tok, "deals", deal_ids, ["dealname", "feature_gaps"])
    companies = batch_read(tok, "companies", company_ids, ["name"])

    notes, summary_counts = [], {"deal": 0, "company_only": 0, "contact_only": 0, "none": 0}
    for n in raw_notes:
        nid = n["id"]
        p = n["properties"]
        d_ids = note_deals.get(nid, [])
        c_ids = note_companies.get(nid, [])
        k_ids = note_contacts.get(nid, [])
        if d_ids:
            assoc_type = "deal"
        elif c_ids:
            assoc_type = "company_only"
        elif k_ids:
            assoc_type = "contact_only"
        else:
            assoc_type = "none"
        summary_counts[assoc_type] += 1

        date = to_date(p.get("hs_timestamp"))

        feature_gaps = []
        deal_names = []
        for did in d_ids:
            dp = deals.get(did, {})
            if dp.get("dealname"):
                deal_names.append(dp["dealname"])
            if dp.get("feature_gaps"):
                feature_gaps += [g for g in dp["feature_gaps"].split(";") if g]

        notes.append({
            "id": nid,
            "date": date,
            "owner": pp.OWNERS.get(p.get("hubspot_owner_id"), p.get("hubspot_owner_id")),
            "body": clean_body(p.get("hs_note_body")),
            "assoc_type": assoc_type,
            "deal_names": deal_names,
            "company_names": [companies.get(c, {}).get("name", c) for c in c_ids],
            "deal_feature_gaps": sorted(set(feature_gaps)),
        })

    out = {
        "label": label,
        "period_label": period_label,
        "start": start,
        "end": end,
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "note_count": len(notes),
        "assoc_breakdown": summary_counts,
        "notes": notes,
    }

    out_path = args.out or os.path.join(SALES_REPORTING, "tmp", f"notes-{label}.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    print(f"notes pulled: {len(notes)}  ({period_label})")
    print(f"  assoc: {summary_counts}")
    print(f"  notes with a deal's feature_gaps set: "
          f"{sum(1 for n in notes if n['deal_feature_gaps'])}")
    print(f"  WROTE: {out_path}")


if __name__ == "__main__":
    main()
