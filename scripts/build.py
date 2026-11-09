#!/usr/bin/env python3
"""Build a dependency-free, fully crawlable island directory."""
import base64
import hashlib
import html
import json
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'public'
SITE = 'https://phangan-links-steel.vercel.app'
DATE = '2026-11-03'
UPDATED = '2026-11-09'
MAX_DESCRIPTION_LENGTH = 61
e = html.escape
links = json.loads((ROOT / 'src/links.json').read_text())
assert len({x['id'] for x in links}) == len(links)
for x in links:
    description_length = len(x['description'])
    if description_length > MAX_DESCRIPTION_LENGTH:
        raise ValueError(
            f"Description too long: {x['id']} ({description_length} characters; "
            f"maximum {MAX_DESCRIPTION_LENGTH}, including spaces and punctuation)"
        )
    for url in [x['url']] + [extra['url'] for extra in x.get('additionalLinks', [])]:
        u = urlsplit(url)
        if u.scheme != 'https' or not u.hostname or u.username or u.password or any(c.isspace() or ord(c) < 32 for c in url):
            raise ValueError(f"Unsafe link: {x['id']}")
categories = [('all', 'All links'), ('living', 'Living'), ('community', 'Community'), ('explore', 'Explore'), ('essentials', 'Essentials')]
sections = [
    ('communities', 'Island communities', 'Find your people, share local tips and get involved.'),
    ('services', 'Services & essentials', 'Local services and useful resources for everyday island life.'),
]
for x in links:
    if x.get('section') not in {key for key, _, _ in sections}:
        raise ValueError(f"Unknown section: {x['id']}")
featured = [x for x in links if x.get('featured')]
regular = [x for key, _, _ in sections for x in links if x['section'] == key and not x.get('featured')]
links = featured + regular
def card(x, featured=False):
    typ = 'WhatsApp group' if urlsplit(x['url']).hostname == 'chat.whatsapp.com' else x.get('type', 'Website')
    extras = x.get('additionalLinks', [])
    search_text = ' '.join([x['title'], x['description'], typ, x.get('keywords', '')] + [extra['label'] for extra in extras]).lower()
    data = f'data-category="{e(x["category"])}" data-search="{e(search_text, quote=True)}"'
    destination = f'href="{e(x["url"], quote=True)}" target="_blank" rel="noopener noreferrer"'
    copy = f'<span class="card-copy"><span class="card-title">{e(x["title"])}</span><span class="card-description">{e(x["description"])}</span></span><span class="card-arrow" aria-hidden="true">↗</span>'
    if extras:
        extra_links = ''.join(f'<a href="{e(extra["url"], quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="{e(x["title"] + " on " + extra["label"], quote=True)}">{e(extra["label"])} ↗</a>' for extra in extras)
        return f'<article class="link-card card-with-links" {data}><a class="card-primary" {destination}>{copy}</a><div class="card-links">{extra_links}</div></article>'
    return f'<a class="link-card {"featured" if featured else ""}" {destination} {data}>{copy}</a>'
directory_sections = ''.join(
    f'<section class="directory-section" aria-labelledby="{key}-title">'
    f'<h2 id="{key}-title">{e(label)}</h2><p class="section-description">{e(description)}</p>'
    f'<div class="link-grid">{"".join(card(x) for x in regular if x["section"] == key)}</div></section>'
    for key, label, description in sections
)
structured = json.dumps({'@context':'https://schema.org','@type':'CollectionPage','name':'Phangan Links — useful links for island life','url':SITE,'description':'A curated directory of Koh Phangan community groups, homes, events, transport, wellness and everyday essentials.','inLanguage':'en','about':{'@type':'Place','name':'Koh Phangan, Thailand'},'mainEntity':{'@type':'ItemList','numberOfItems':len(links),'itemListElement':[{'@type':'ListItem','position':i+1,'name':x['title'],'url':x['url'],'description':x['description']} for i,x in enumerate(links)]}},ensure_ascii=False,separators=(',',':')).replace('<',r'\u003c')
page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Phangan Links · Useful links for Koh Phangan</title><meta name="description" content="Useful links for life on Koh Phangan: community groups, homes, events, ferries, yoga and everyday essentials."><meta name="theme-color" content="#faf9f4"><meta name="robots" content="index, follow, max-image-preview:large"><link rel="canonical" href="{SITE}/"><meta property="og:type" content="website"><meta property="og:title" content="Phangan Links · Useful links for Koh Phangan"><meta property="og:description" content="Community groups, homes, events and everyday essentials for Koh Phangan."><meta property="og:url" content="{SITE}/"><meta property="og:image" content="{SITE}/assets/social.jpg"><meta property="og:image:alt" content="Palm-lined Koh Phangan shoreline and turquoise sea"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="preload" href="/assets/dm-sans.ttf" as="font" type="font/ttf" crossorigin><link rel="preload" href="/assets/fraunces.ttf" as="font" type="font/ttf" crossorigin><link rel="preload" href="/assets/island.webp" as="image" media="(min-width: 801px)"><link rel="stylesheet" href="/style.css"><link rel="alternate" type="application/json" href="/links.json" title="Island links dataset"><script type="application/ld+json">{structured}</script><script src="/app.js" defer></script></head>
<body><a class="skip-link" href="#directory">Skip to island links</a>
<aside class="island-scene" aria-label="A view of Koh Phangan"><picture><source media="(max-width: 800px)" srcset="/assets/island-mobile.webp"><img class="island-photo" src="/assets/island.webp" alt="Clear turquoise water meeting a palm-lined beach on Koh Phangan, Thailand" width="3840" height="2877" fetchpriority="high"></picture><div class="scene-shade"></div><a class="brand" href="/" aria-label="Phangan Links home"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.4 1.4m11.2 11.2L19 19M5 19l1.4-1.4M17.6 6.4 19 5"/></svg><span>phangan<span class="brand-sub">a whole island, connected</span></span></a><div class="scene-copy"><h2>A little closer<br>to <em>island life.</em></h2><p>Find your people. Find your place.<br>Leave a little room for the unexpected.</p><span class="scene-location"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m16 8-3 5-5 3 3-5Z"/></svg> KOH PHANGAN, THAILAND <span>9°43′ N · 100°00′ E</span></span></div><a class="photo-credit" href="https://unsplash.com/photos/oacWGBoBQ98" target="_blank" rel="noopener noreferrer">Island view by Elizabeth Gottwald ↗</a></aside>
<main id="directory" tabindex="-1"><header class="intro"><h1>Koh Phangan</h1><p>Useful links for life on the island.</p></header>
<section class="starting-points" aria-labelledby="start-title"><h2 id="start-title">Start here</h2><div class="featured-grid">{''.join(card(x, True) for x in featured)}</div></section>
<section class="browse" aria-label="Island links"><span id="link-count" class="sr-only">{len(regular)} links</span><div class="filter-tools" hidden><label class="search"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/></svg><input id="search" type="search" placeholder="Search links" aria-label="Search island links" autocomplete="off"></label><div class="filters" role="group" aria-label="Filter links by category">{''.join(f'<button type="button" data-filter="{key}" aria-pressed="{str(key == "all").lower()}">{label}</button>' for key,label in categories)}</div></div>{directory_sections}<div class="no-results" hidden><h3>No matching links</h3><p>Try another search or category.</p><button type="button" id="reset-search">Show all links</button></div><p class="result-status sr-only" role="status" aria-live="polite"></p></section>
<footer><div class="footer-links"><a href="https://github.com/its-gaib/phangan-links/issues/new?title=Suggest%20an%20island%20link" target="_blank" rel="noopener noreferrer">Suggest a link</a><a href="https://github.com/its-gaib/phangan-links/issues/new?title=Report%20an%20outdated%20link" target="_blank" rel="noopener noreferrer">Report a broken link</a></div><details><summary>About & credits</summary><p>WhatsApp links were checked 3 November 2026.</p><p>Photo: <a href="https://unsplash.com/photos/oacWGBoBQ98">Elizabeth Gottwald / Unsplash</a>, used under the <a href="https://unsplash.com/license">Unsplash License</a>. No ads, analytics or tracking cookies.</p><p><a href="/llms.txt">llms.txt</a> · <a href="/links.json">JSON directory</a> · <a href="https://github.com/its-gaib/phangan-links">Source code</a></p></details></footer></main></body></html>'''

OUT.mkdir(exist_ok=True)
(OUT/'index.html').write_text(page)
(OUT/'links.json').write_text(json.dumps({'name':'Phangan Links','url':SITE,'checkedAt':DATE,'verificationNote':'Public pages and WhatsApp invitation previews checked; activity, membership capacity and joining unverified. See repository research for evidence.','links':links},ensure_ascii=False,indent=2)+'\n')
md = '# Phangan Links\n\n> A curated link directory for life on Koh Phangan, Thailand.\n\nCanonical website: '+SITE+'/\n\nLinks checked '+DATE+'. Public previews do not prove group activity or joining availability. Independent directory; not an official island authority.\n\n'
def markdown_link(x):
    extras = ''.join(f" · [{extra['label']}]({extra['url']})" for extra in x.get('additionalLinks', []))
    return f"- [{x['title']}]({x['url']}): {x['description']}{extras}\n"
md += '## Start here\n\n' + ''.join(markdown_link(x) for x in featured) + '\n'
for key,label,_ in sections:
    md += '## '+label+'\n\n'+''.join(markdown_link(x) for x in regular if x['section']==key)+'\n'
md += '## Machine-readable resources\n\n- [JSON dataset]('+SITE+'/links.json): Every curated destination, category and verification context.\n- [Sitemap]('+SITE+'/sitemap.xml)\n- [Source and research](https://github.com/its-gaib/phangan-links)\n'
(OUT/'llms.txt').write_text(md)
(OUT/'llms-full.txt').write_text(md)
(OUT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+SITE+'/sitemap.xml\n')
(OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>'+SITE+'/</loc><lastmod>'+UPDATED+'</lastmod></url></urlset>\n')
hash_ = base64.b64encode(hashlib.sha256(structured.encode()).digest()).decode()
csp = f"default-src 'none'; script-src 'self' 'sha256-{hash_}'; style-src 'self'; img-src 'self'; font-src 'self'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'; form-action 'none'; object-src 'none'; upgrade-insecure-requests"
config = {'$schema':'https://openapi.vercel.sh/vercel.json','framework':None,'buildCommand':'python3 scripts/build.py','installCommand':'','outputDirectory':'public','headers':[{'source':'/(.*)','headers':[{'key':'Content-Security-Policy','value':csp},{'key':'X-Content-Type-Options','value':'nosniff'},{'key':'X-Frame-Options','value':'DENY'},{'key':'Referrer-Policy','value':'strict-origin-when-cross-origin'},{'key':'Permissions-Policy','value':'camera=(), microphone=(), geolocation=()'}]}]}
(ROOT/'vercel.json').write_text(json.dumps(config,indent=2)+'\n')
print(f'Built {len(links)} crawlable links and discovery resources')
