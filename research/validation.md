# Validation

Validated 3 November 2026.

- Playwright Chromium: 1440, 1024, 801, 800, 390, 360 and 320px viewport widths; no horizontal overflow.
- Search, all topic filters, no-results state/reset, keyboard focus, and `/` search shortcut passed.
- JavaScript disabled: every directory link remains visible as a real HTML anchor.
- No JavaScript errors or failed asset requests during browser checks.
- Axe WCAG 2 A/AA and WCAG 2.1 AA after contrast corrections: zero automated violations at 1440, 390 and 320px. Photography overlay text also visually inspected; automated checks cannot establish full WCAG conformance.
- HTML link count matches JSON dataset and schema.org ItemList: 34.
- JSON-LD parses, its exact hash matches the CSP, and discovery resources exist.
- Preimplementation and postimplementation security review: no actionable findings.
- Production responds publicly over HTTPS without authentication.

No group was joined and no messages were sent. Public previews alone cannot prove group activity or availability.

## Readability revision — 4 November 2026

The directory now uses one column, 20px link titles, 16px descriptions and 17px search text. Removed decorative badges, icon tiles, slogans, uppercase metadata and card hover motion. Mobile photo header is 250px high.

The community-document audit covers all 13 source entries and adds the verified local trading group. The HTML, JSON and structured data now contain 35 links. Security review of the changed template and generated output found no actionable issues; an isolated hostile-content build confirmed HTML and JSON-LD escaping.

Stable browser QA passed at 1440, 1024, 800, 390 and 320px: no horizontal overflow; search, every filter, empty-state reset, keyboard access and no-JavaScript visibility pass. All 33 regular links and two featured links remain available. No page errors or failed requests. Axe reports zero automated violations at 1440, 390 and 320px; the desktop photographic caption remains a manual contrast check. Featured titles are 22px, regular titles 20px, descriptions 16px and the search input 17px.
