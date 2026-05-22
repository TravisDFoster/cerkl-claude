#!/usr/bin/env bash
# Render an HTML file to PNG via Chrome headless.
#
# Usage:
#   ./render.sh <html-path> [output-path] [width] [height]
#
# Defaults:
#   output-path: same basename as html, .png extension
#   width: 1200
#   height: 627
#
# Examples:
#   ./render.sh templates/concept-ladder/example.html
#   ./render.sh foo.html foo.png 1200 800

set -euo pipefail

HTML="${1:?usage: render.sh <html-path> [output-path] [width] [height]}"
PNG="${2:-${HTML%.html}.png}"
W="${3:-1200}"
H="${4:-627}"

# Resolve absolute paths (Chrome needs file:// with absolute path)
HTML_ABS="$(cd "$(dirname "$HTML")" && pwd)/$(basename "$HTML")"
PNG_DIR="$(dirname "$PNG")"
[[ -d "$PNG_DIR" ]] || mkdir -p "$PNG_DIR"
PNG_ABS="$(cd "$PNG_DIR" && pwd)/$(basename "$PNG")"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[[ -x "$CHROME" ]] || { echo "Chrome not found at: $CHROME" >&2; exit 2; }

"$CHROME" --headless --disable-gpu --hide-scrollbars --no-sandbox \
  --window-size="${W},${H}" \
  --default-background-color=00000000 \
  --screenshot="${PNG_ABS}" \
  "file://${HTML_ABS}" 2>/dev/null || true

[[ -s "$PNG_ABS" ]] || { echo "render failed (no output written)" >&2; exit 3; }

SIZE=$(stat -f%z "$PNG_ABS")
echo "Wrote ${PNG_ABS} (${SIZE} bytes, ${W}x${H})"
