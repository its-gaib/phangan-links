# Phangan Links

A little link tree for a whole island. A calm, useful directory for life on Koh Phangan, Thailand.

## Develop

No runtime dependencies, accounts, analytics, or database. Python 3 builds semantic static HTML from `src/links.json`:

```sh
python3 scripts/build.py
python3 -m http.server 4173 --directory public
```

Edit the curated data, then rebuild. The committed `public/` output runs on any static host. Vercel uses the included configuration.

## Discovery

Every directory link is a real anchor in the initial HTML. Search and category filters are progressive enhancements. Structured data, a sitemap, robots.txt, llms.txt, llms-full.txt and a public JSON dataset help crawlers discover the directory. These improve discoverability; they cannot guarantee indexing.

## Link checking

See `research/` for sources, dates, and verification limits. A successful public invitation preview does not prove group activity, available places, trustworthiness, or successful joining. Listings are independent destinations, not endorsements. Recheck links before updating the verification date.

## Credits

Photography and font attribution are documented in `research/credits.md`. Third-party photos and fonts retain their respective licenses.
