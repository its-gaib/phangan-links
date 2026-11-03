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
