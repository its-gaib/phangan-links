# Complete audit of Koh Phangan Groups Google Doc

Audited 2026-11-04 UTC against `/home/gaib/git/its-gaib/phangan-links/src/links.json`.

Source: https://docs.google.com/document/d/1H18auNoNBECzqIIS6eNHBoSP8o41p0UgezX4542DP6w/edit?usp=sharing

The complete current plain-text export returned HTTP 200. The document still carries source date 2026-05-08 and contains **13 group/resource entries**, plus a footnote linking back to the same document. It is the same content retrieved in the first research pass.

## Outcome

Four entries were already directly represented on the site: comedy, Shaolin arts, hiking, volleyball. **One suitable verified island-specific entry had been omitted: Trading Sessions Ko Pha-ngang.** Its shortener was now expanded and the direct named public preview verified. Four island-specific invitations remain unverified (AI, acroyoga, vegan, Latino). One shortener remains blocked (Crypto Links). Three groups refer to other destinations (Samui, Tao, Bangkok) and are omitted to preserve island scope.

All URLs in the document were requested in this audit, including the out-of-scope shorteners, to establish explicit coverage. A matching public group title verifies destination identity only; no group was joined, and activity/capacity/joinability are not confirmed.

## Every document entry

| # | Document entry | Source URL | Resolved direct URL / result | Site coverage / decision |
|---|---|---|---|---|
| 1 | COMEDY KPG | https://chat.whatsapp.com/LgkYObLpk6p0VgunwH3Oj2 | Same URL, HTTP 200; metadata and visible body name `KPG.comedy`. | Already included as `comedy`, “A little island laughter”. Keep. |
| 2 | Crypto Links | https://shorturl.at/bzV17 | HTTP 403 Cloudflare “Just a moment…” challenge; no redirect destination exposed. Also tried www hostname, HTTP-to-HTTPS and browser web retrieval. | Omit from direct curated links because destination and island relevance cannot be verified. Source document remains accessible through “More community groups”. Do not describe as expired or unsafe: evidence only establishes retrieval blocked. |
| 3 | Pro traders/econ | https://bit.ly/3tAeHxx | Resolves to https://chat.whatsapp.com/GBoE51xlL4h25Yu6NC3Mu3, HTTP 200; metadata and body name `Trading Sessions Ko Pha-ngang 📈`. | **Missing. Add `trading` with direct invite**, factual description “Local conversations about trading, markets & economics.” No advice, promises or endorsement. |
| 4 | Pha ngan AI meetup | https://chat.whatsapp.com/EHuLy3KfzA93P5NYU3w9Xl | HTTP 200 generic WhatsApp template, empty og:title and empty invitation name in body. | Omit from curated direct links; identity/current usability cannot be verified. Retested with `?mode=gi_t`, browser User-Agent, `?lang=en`, social-preview User-Agent, and web retrieval. Same blank result. Do not assert definitively expired. |
| 5 | Shaolin arts | https://chat.whatsapp.com/FYAA1prpdMV4seE3cp9ObT | Same URL, HTTP 200; metadata/body name `Shaolin Arts Koh Phangan`. | Already included as `shaolin`. Keep. |
| 6 | Acroyoga | https://chat.whatsapp.com/HC8dFZVvrwi2KcGo9CFzbd | HTTP 200 generic template, empty metadata/body group name. Source has explicit footnote: “Invite expired”, asking for replacement. | Omit: source explicitly flags expired and public preview does not establish a current group. Same alternative retrieval attempts as AI. |
| 7 | Hiking | https://chat.whatsapp.com/DvsEn3NkD6a6UusFXNN6ok | Same URL, HTTP 200; metadata/body name `Koh Phangan Hiking`. | Already included as `group-10`, “Hiking together”; existing URL's `?mode=gi_c` does not change invite identity. Keep once, no duplicate. |
| 8 | Meet&Eat Vegan | https://chat.whatsapp.com/BxqFKcNOISP5hlwTWtebKs | HTTP 200 generic template, empty metadata/body group name. | Omit from curated direct links; identity/current usability not verified. Same alternative retrieval attempts as AI; do not call definitively expired. |
| 9 | Volleyball | https://bit.ly/43hsaLN | Resolves to https://chat.whatsapp.com/Dsf7SWh1uyZ2TuVrpVvwuP, HTTP 200; metadata/body name `KPG volley troop🤘`. | Already included as `volley` with direct URL. Keep. |
| 10 | Latino Dance | chat.whatsapp.com/FMzaV5eoCNDDfr5iDvvXaB | Normalized to https://chat.whatsapp.com/FMzaV5eoCNDDfr5iDvvXaB. HTTP 200 generic template, empty metadata/body group name. | Omit from curated direct links; identity/current usability not verified. Same alternative retrieval attempts as AI; do not call definitively expired. |
| 11 | Koh Samui Nomads | https://bit.ly/40Sr2fP | Resolves to https://chat.whatsapp.com/CEG75MX4vaR69PEzoOqiKv, HTTP 200; name `Remote&Nomads-Koh Samui 🏝️`. | Omit: clearly Koh Samui, not Koh Phangan. Source document retains optional onward discovery. |
| 12 | Digital Nomads Koh Tao | https://bit.ly/3Unnxf6 | Resolves to https://chat.whatsapp.com/K7hpgL1ifCvJLHZTAjEOSY, HTTP 200 generic template, empty group name. | Omit: source identifies Koh Tao, outside scope, and public preview unverified. |
| 13 | Digital Nomads BKK (Bangkok) | https://bit.ly/3KJclpZ | Resolves to https://chat.whatsapp.com/LBvAfS5CkID0ox06YLt0p2, HTTP 200; metadata/body name `General Chat in Bangkok`. | Omit: Bangkok, outside island scope. |

## Footnotes and non-link text

- “Source: WhatsApp Msg Grp: Housing: Short-term (6 mo max)” is provenance text without its own hyperlink; no extra target to follow.
- Source date 2026-05-08 is retained as document provenance, not proof of activity now.
- Footnote [a] explicitly marks the acroyoga invite as expired.
- Footnote [b] points to this same Google Doc with `?usp=drivesdk`; HTTP 200, same document ID. Already linked on site as `more`, so no duplicate.

## Files

- `/tmp/phangan-doc-current.txt`: full raw text export.
- `/tmp/phangan-doc-check-results.json`: all source requests, statuses, final redirects, metadata and visible text snapshots.
- `/tmp/phangan-doc-additions.json`: one new verified suitable direct link, matching existing entry schema.

## Honest answer to original coverage question

The original site did not add every suitable entry directly: the local trading discussion invite was omitted. The original research also did not expand all three out-of-island shorteners or the trading shortener, so claiming every document link had been followed would overstate that first pass. This audit has now attempted every entry, expands all accessible bit.ly shorteners, accounts for all 13 entries and proposes the one verified island-specific addition. Blocked/unverified entries remain available indirectly via the original source document, with reasons recorded here.
