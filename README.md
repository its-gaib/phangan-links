# Phangan Links

A little link tree for a whole island. A calm, useful directory for life on Koh Phangan, Thailand.

Live: https://www.phangan.fyi

Repository default branch: `island-directory`.

## Develop

No runtime dependencies, accounts, analytics, or database. Python 3 builds semantic static HTML from `src/links.json`:

```sh
python3 scripts/build.py
python3 -m http.server 4173 --directory public
```

Edit the curated data, then rebuild. The committed `public/` output runs on any static host. Vercel uses the included configuration.

Listing descriptions must be at most 61 characters, including spaces and punctuation. The build rejects longer descriptions and reports the listing ID and character count.

## Discovery

Every directory link is a real anchor in the initial HTML. Search and category filters are progressive enhancements. Structured data, a sitemap, robots.txt, llms.txt, llms-full.txt and a public JSON dataset help crawlers discover the directory. These improve discoverability; they cannot guarantee indexing.

## Link checking

See `research/` for sources, dates, and verification limits. A successful public invitation preview does not prove group activity, available places, trustworthiness, or successful joining. Listings are independent destinations, not endorsements. Recheck links before updating the verification date.

## Credits

Photography and font attribution are documented in `research/credits.md`. Third-party photos and fonts retain their respective licenses.

## Deploy

```sh
python3 scripts/build.py
npx --yes vercel@65.2.0 link --yes --project phangan-links --scope its-gaibs-projects
npx --yes vercel@65.2.0 deploy --prod --yes --scope its-gaibs-projects
```

Run deployment from the reviewed repository checkout. Link it to the existing `phangan-links` project before deploying from a new worktree; do not let its task-directory name create a new project. Keep `.vercel/` and `.env*` out of Git.

The canonical URL is set in `scripts/build.py`. It generates the HTML canonical, structured data, social URLs, JSON and text resources, sitemap and robots declaration together. The build also generates the permanent redirect from the exact production alias `phangan-links-steel.vercel.app` to the custom domain, preserving paths and query strings; preview deployment hostnames are unaffected. Change the generator and rebuild instead of editing `public/` or `vercel.json` by hand.

After deployment, check the custom homepage and sitemap, plus a path and query on the production Vercel alias. The alias must return 308 to the corresponding custom-domain URL, and the custom homepage must return 200 with its self-canonical. Submit `https://www.phangan.fyi/sitemap.xml` in Search Console and use URL Inspection on the homepage to request indexing and check Google's selected canonical after recrawling.
