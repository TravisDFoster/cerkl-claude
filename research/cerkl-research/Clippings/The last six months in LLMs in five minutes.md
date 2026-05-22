---
title: "The last six months in LLMs in five minutes"
source: "https://simonwillison.net/2026/may/19/5-minute-llms/"
author:
  - "[[Simon Willison]]"
published:
created: 2026-05-19
description: "I put together these annotated slides from my five minute lightning talk at PyCon US 2026, using the latest iteration of my annotated presentation tool. # I presented this lightning …"
tags:
  - "clippings"
---
I put together these annotated slides from my five minute lightning talk at PyCon US 2026, using the [latest iteration](https://tools.simonwillison.net/annotated-presentations) of my [annotated presentation tool](https://simonwillison.net/2023/Aug/6/annotated-presentations/).

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.001.jpeg)

I presented this lightning talk at PyCon US 2026, attempting to summarize the last six months of developments in LLMs in five minutes.

![The November inflection point ](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.002.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.002.jpeg)

Six months is a pretty convenient time period to cover, because it captures what I’ve been calling the [November 2025 inflection point](https://simonwillison.net/tags/november-2025-inflection/). November was a critical month in LLMs, especially for coding.

![The “best” model changed hands 5 times between Anthropic, OpenAl and Google ](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.003.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.003.jpeg)

For one thing, the supposedly “best” model (depending mostly on vibes) changed hands five times between the three big providers.

![Generate an SVG of a pelican riding a bicycle ](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.004.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.004.jpeg)

As always, I’m using my [Generate an SVG of a pelican riding a bicycle](https://simonwillison.net/tags/pelican-riding-a-bicycle/) test to help illustrate the differences between the models.

Why this test? Because pelicans are hard to draw, bicycles are hard to draw, pelicans *can’t ride bicycles*... and there’s zero chance any AI lab would train a model for such a ridiculous task.

![Five pelicans, one for each of the following models. Varying qualities!](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.005.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.005.jpeg)

At the start of November the widely acknowledged “best” model was Claude Sonnet 4.5, released on [29th September](https://simonwillison.net/2025/Sep/29/claude-sonnet-4-5/). It drew me this pelican.

In November it was overtaken by [GPT-5.1](https://simonwillison.net/2025/Nov/13/gpt-51/), then [Gemini 3](https://simonwillison.net/2025/Nov/18/gemini-3/), then [GPT-5.1 Codex Max](https://simonwillison.net/2025/Nov/19/gpt-51-codex-max/), and then Anthropic took the crown back again with [Claude Opus 4.5](https://simonwillison.net/2025/Nov/24/claude-opus/).

I think Gemini 3 drew the best pelican out of this lot, but pelicans aren’t everything. Most practitioners will agree that Opus 4.5 held the crown for the next couple of months.

![The coding agents got good ](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.006.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.006.jpeg)

It took a little while for this to become clear, but the real news from November was that the coding agents got *good*.

OpenAI and Anthropic had spent most of 2025 running [Reinforcement Learning from Verifiable Rewards](https://simonwillison.net/2025/Dec/19/andrej-karpathy/) to increase the quality of code written by their models, especially when paired up with their Codex and Claude Code agent harnesses.

In November the results of this work became apparent. Coding agents went from often-work to mostly-work, crossing a quality barrier where you could use them as a daily-driver to get real work done, without needing to spend most of your time fixing their stupid mistakes.

![Screenshot of "Initial commit" on GitHub to steipete/Warelay, commit f6dd362, steipete authored on Nov 24, 2025  It's a copy of the MIT license](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.007.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.007.jpeg)

Also in November, this happened—the first commit to an obscure (back then) repo called “Warelay” by some guy called Pete.

![December/January (A little bit of LLM psychosis) ](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.008.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.008.jpeg)

Over the holiday period, from December to January, a whole lot of us took advantage of the break to have a poke at these new models and coding agents and see what they could do.

They could do a lot! Some of us got a little bit over-excited. I had my own short-lived bout of a form of LLM psychosis as I started spinning up wildly ambitious projects to see how far I could push them.

![micro-javascript playground Execute JavaScript code in a sandboxed micro-javascript environment powered by Pyodide  var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; var doubled = numbers.map(n => n * 2); console.log('Doubled: "', doubled); var evens = numbers.filter(n => n % 2 === 0); console.log('Evens: ', evens); var sum = numbers.reduce((a, b) => a + b, @); console.log('Sum:", sum);  Output 27 Doubled: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] Evens: [2, 4, 6, 8, 10] Sum: 55 Execution time: 8.00ms About: micro-javascript is a pure Python JavaScript interpreter with configurable memory and time limits. This playground runs entirely in your browser using Pyodide (Python compiled to WebAssembly). View on GitHub](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.009.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.009.jpeg)

One of my projects was a vibe-coded implementation of JavaScript in Python—a loose port of [MicroQuickJS](https://github.com/bellard/mquickjs) —which I called [micro-javascript](https://github.com/simonw/micro-javascript). You can try it out in your browser in [this playground](https://simonw.github.io/micro-javascript/playground.html).

![JavaScript running in Python running in Pyodide running in WebAssembly running in JavaScript](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.010.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.010.jpeg)

That playground demo shows JavaScript code run using my micro-javascript library, in Python, running inside Pyodide, running in WebAssembly, running in JavaScript, running in a browser!

It’s pretty cool! But did anyone out there *need* a buggy, slow, insecure half-baked implementation of JavaScript in Python?

They did not. I have quite a few other projects from that holiday period that I have since quietly retired!

![February 2026 ](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.011.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.011.jpeg)

On to February. Remember that Warelay project that had its first commit at the end of November?

![Warelay → CLAWDIS → CLAWDBOT → Clawdbot → Moltbot →🦞 OpenClaw](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.012.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.012.jpeg)

In December and January it had gone through [quite a few name changes](https://simonwillison.net/2026/May/16/openclaw-names/)... and by February it was taking the world by storm under its final name, [OpenClaw](https://openclaw.ai/).

The amount of attention it got is pretty astonishing for a project that was less than three months old.

![Generic term: Claw ](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.013.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.013.jpeg)

OpenClaw is a “personal AI assistant”, and we actually got a generic term for these, based on NanoClaw and ZeroClaw and suchlike... they’re called **Claws**.

![An aquarium for your Claw ](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.014.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.014.jpeg)

Mac Minis started to sell out around Silicon Valley, because people were buying them to run their Claws.

[Drew Breunig](https://www.dbreunig.com/) joked to me that this is because they’re the new digital pets, and a Mac Mini is the perfect aquarium for your Claw.

![Alfred Molina's Doc Ock in Spider-Man 2, tearing apart a New York subway train with his four claws.](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.015.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.015.jpeg)

My favourite metaphor for Claws is Alfred Molina’s Doc Ock in the 2004 movie Spider-Man 2. His claws were powered by AI, and were perfectly safe provided nothing damaged his inhibitor chip... after which they turned evil and took over.

![Gemini 3.1 Pro  A really good illustration of a pelican riding a bicycle. ](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.016.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.016.jpeg)

Also in February: Gemini 3.1 Pro came out, and drew me a *really good pelican riding a bicycle*. Look at this! It’s even got a fish in its basket.

![Gemini 3 Pro pelican contrasted with Gemini 3.1 Pro, as animated SVGs](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.017.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.017.jpeg)

And then Google’s Jeff Dean [tweeted this video](https://simonwillison.net/2026/Feb/19/gemini-31-pro/#jeff-dean) of an animated pelican riding a bicycle, plus a frog on a penny-farthing and a giraffe driving a tiny car and an ostrich on roller skates and a turtle kickflipping a skateboard and a dachshund driving a stretch limousine.

So maybe the AI labs have been paying attention after all!

![April 2026 ](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.018.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.018.jpeg)

A lot of stuff happened just in the past month.

![Gemma 4 26B-A4B (17.99GB)  A pretty decent pelican riding a bicycle, though the bike is a bit mis-shapen.](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.019.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.019.jpeg)

Google released the [Gemma 4](https://simonwillison.net/2026/Apr/2/gemma-4/) series of models, which are the most capable open weight models I’ve seen from a US company.

![GLM-5.1 MIT, 754B parameter, 1.51TB! ](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.020.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.020.jpeg)

Also last month, Chinese AI lab GLM came out with [GLM-5.1](https://simonwillison.net/2026/Apr/7/glm-51/) —an open weight 1.5TB monster! This is a very effective model... if you can afford the hardware to run it.

![](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.021.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.021.jpeg)

GLM-5.1 drew me this very competent pelican on a bicycle.

![The bike is wonky, the pelican is floating.](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.022.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.022.jpeg)

... though when it [tried to animate it](https://gisthost.github.io/?73bb6808b18c2482f66e5f082c75f36e) the bicycle bounced off into the top and the bicycle got warped.

![Screenshot of Bluesky  Charles ‪@charles.capps.me‬ I think you should pester it with another animal using another method of locomotion.   Something tells me it was trained for this. I can't quite put my finger on it. /s  NORTH VIRGINIA OPOSSUM ON AN E-SCOOTER!!](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.023.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.023.jpeg)

Charles [on Bluesky](https://bsky.app/profile/charles.capps.me/post/3miwrn42mjc2t) suggested I try it with a North Virginia Opossum on an E-scooter

![NORTH VIRGINIA OPOSSUM CRUISING THE COMMONWEALTH SINCE DUSK  And a really cool illustration of a possum.](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.024.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.024.jpeg)

And it did this! I’ve tried this on other models and they don’t even come close. “Cruising the commonwealth since dusk” is perfect. It’s [animated too](https://static.simonwillison.net/static/2026/glm-possum-escooter.html).

![Qwen3.6-35B-A3B is a 20.9GB file that runs on my laptop  It drew a better pelican on a bicycle than Opus 4.7, which messed up the bicycle frame.](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.025.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.025.jpeg)

The other neat Chinese open weight models in April came from Qwen. [Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7](https://simonwillison.net/2026/Apr/16/qwen-beats-opus/). That’s a 20.9GB open weights model that runs on my laptop!

(I think this mainly demonstrates that the pelican on the bicycle has firmly exceeded its limits as a useful benchmark.)

![Claude Sonnet 4.5 pelican for comparison.](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.026.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.026.jpeg)

Here’s that Claude Sonnet 4.5 pelican from September for comparison.

![The themes of the past 6 months: Coding agents got really good Local models wildly outperform expectations ](https://static.simonwillison.net/static/2026/5-minutes-llms/5-minutes-llms.027.jpeg)

[#](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.027.jpeg)

So those were the two main themes of the past six months. The coding agents got really good... and the laptop-available models, while a lot weaker than the frontier, have started wildly outperforming expectations.