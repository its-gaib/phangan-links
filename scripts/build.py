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
e = html.escape
links = json.loads((ROOT / 'src/links.json').read_text())
assert len({x['id'] for x in links}) == len(links)
for x in links:
    u = urlsplit(x['url'])
    if u.scheme != 'https' or not u.hostname or u.username or u.password or any(c.isspace() or ord(c) < 32 for c in x['url']):
        raise ValueError(f"Unsafe link: {x['id']}")
categories = [('all', 'All the island'), ('living', 'Living here'), ('community', 'Find your people'), ('explore', 'Out & about'), ('essentials', 'The essentials')]
icons = {
 'home': '<path d="m3 10 9-7 9 7v10H3Z"/><path d="M9 20v-7h6v7"/>',
 'sun': '<circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.4 1.4m11.2 11.2L19 19M5 19l1.4-1.4M17.6 6.4 19 5"/>',
 'people': '<circle cx="9" cy="8" r="3"/><path d="M3 21v-3a6 6 0 0 1 12 0v3m1-16a3 3 0 0 1 0 6m3 10v-3a6 6 0 0 0-2-4"/>',
 'leaf': '<path d="M20 3C5 1 1 10 6 16s16 0 14-13ZM4 21 16 8"/>',
 'wave': '<path d="M2 8c3-5 6 5 10 0s7 5 10 0M2 15c3-5 6 5 10 0s7 5 10 0"/>',
 'heart': '<path d="M20 5a5 5 0 0 0-8 1 5 5 0 0 0-8-1c-5 5 3 11 8 15 5-4 13-10 8-15Z"/>',
 'compass': '<circle cx="12" cy="12" r="9"/><path d="m16 8-3 5-5 3 3-5Z"/>',
 'bag': '<path d="M4 7h16l1 14H3ZM8 8V6a4 4 0 0 1 8 0v2"/>',
 'boat': '<path d="m3 14 9-3 9 3-3 6H6Zm4-2V6h10v6M12 2v4M2 22c3-3 6 3 10 0s7 3 10 0"/>',
 'flower': '<path d="M12 21C-1 15 3 6 8 11c-2-12 10-12 8 0 5-5 9 4-4 10Z"/>',
 'search': '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/>',
 'arrow': '<path d="M5 12h14m-5-5 5 5-5 5"/>',
}
def icon(name):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{icons[name]}</svg>'
def card(x, featured=False):
    typ = 'WhatsApp group' if 'chat.whatsapp.com' in x['url'] else x.get('type', 'Website')
    return f'''<a class="link-card {'featured' if featured else ''}" href="{e(x['url'], quote=True)}" target="_blank" rel="noopener noreferrer" data-category="{e(x['category'])}" data-search="{e((x['title']+' '+x['description']+' '+typ+' '+x.get('keywords','')).lower(), quote=True)}"><span class="card-icon {e(x.get('color','sage'))}">{icon(x['icon'])}</span><span class="card-copy"><span class="card-title">{e(x['title'])}</span><span class="card-description">{e(x['description'])}</span><span class="card-type">{e(typ)}</span></span><span class="card-arrow">↗</span></a>'''
featured = [x for x in links if x.get('featured')]
regular = [x for x in links if not x.get('featured')]
structured = json.dumps({'@context':'https://schema.org','@type':'CollectionPage','name':'Phangan Links — useful links for island life','url':SITE,'description':'A curated directory of Koh Phangan community groups, homes, events, transport, wellness and everyday essentials.','inLanguage':'en','about':{'@type':'Place','name':'Koh Phangan, Thailand'},'mainEntity':{'@type':'ItemList','numberOfItems':len(links),'itemListElement':[{'@type':'ListItem','position':i+1,'name':x['title'],'url':x['url'],'description':x['description']} for i,x in enumerate(links)]}},ensure_ascii=False,separators=(',',':')).replace('<',r'<')
page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Phangan Links · A little closer to island life</title><meta name="description" content="Your little link tree for Koh Phangan. Find community groups, homes, events, ferries, yoga and everyday island essentials. Less searching, more living."><meta name="theme-color" content="#f7f5ed"><meta name="robots" content="index, follow, max-image-preview:large"><link rel="canonical" href="{SITE}/"><meta property="og:type" content="website"><meta property="og:title" content="Phangan Links · A little closer to island life"><meta property="og:description" content="Good people. Slow days. Useful links. A little link tree for a whole island."><meta property="og:url" content="{SITE}/"><meta property="og:image" content="{SITE}/assets/social.jpg"><meta property="og:image:alt" content="Palm-lined Koh Phangan shoreline and turquoise sea"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="preload" href="/assets/fraunces.ttf" as="font" type="font/ttf" crossorigin><link rel="preload" href="/assets/island.webp" as="image" media="(min-width: 801px)"><link rel="stylesheet" href="/style.css"><link rel="alternate" type="application/json" href="/links.json" title="Island links dataset"><script type="application/ld+json">{structured}</script><script src="/app.js" defer></script></head>
<body><a class="skip-link" href="#directory">Skip to island links</a>
<aside class="island-scene" aria-label="A view of Koh Phangan"><picture><source media="(max-width: 800px)" srcset="/assets/island-mobile.webp"><img class="island-photo" src="/assets/island.webp" alt="Clear turquoise water meeting a palm-lined beach on Koh Phangan, Thailand" width="3840" height="2877" fetchpriority="high"></picture><div class="scene-shade"></div><a class="brand" href="/" aria-label="Phangan Links home">{icon('sun')}<span>phangan<span class="brand-sub">a whole island, connected</span></span></a><div class="island-stamp" aria-hidden="true"><span>GO GENTLY</span>{icon('flower')}<span>STAY AWHILE</span></div><div class="scene-copy"><span class="eyebrow">A LITTLE LINK TREE FOR A WHOLE ISLAND</span><h2>A little closer<br>to <em>island life.</em></h2><p>Find your people. Find your place.<br>Leave a little room for the unexpected.</p><span class="scene-location">{icon('compass')} KOH PHANGAN, THAILAND <span>9°43′ N · 100°00′ E</span></span></div><a class="photo-credit" href="https://unsplash.com/photos/oacWGBoBQ98" target="_blank" rel="noopener noreferrer">Island view by Elizabeth Gottwald ↗</a></aside>
<main id="directory" tabindex="-1"><header class="intro"><div class="intro-top"><span class="eyebrow">YOUR ISLAND SHORTCUT</span><span class="tiny-sun" aria-hidden="true">✳</span></div><h1>Koh Phangan<span class="heading-dot">.</span></h1><p>Good people. Slow days. Useful links.</p><div class="intro-note"><span class="line-wave" aria-hidden="true">∿∿</span> Less searching, more living.</div></header>
<section class="starting-points" aria-labelledby="start-title"><div class="section-heading"><h2 id="start-title">A good place to start</h2><span>THE ISLAND FAVOURITES</span></div><div class="featured-grid">{''.join(card(x,True) for x in featured)}</div></section>
<section class="browse" aria-labelledby="browse-title"><div class="section-heading browse-heading"><h2 id="browse-title">Your island, a little easier</h2><span id="link-count">{len(regular)} LINKS TO EXPLORE</span></div><div class="filter-tools" hidden><label class="search">{icon('search')}<input id="search" type="search" placeholder="A home, a ferry, your people…" aria-label="Search island links" autocomplete="off"><kbd aria-hidden="true">/</kbd></label><div class="filters" role="group" aria-label="Filter links by category">{''.join(f'<button type="button" data-filter="{key}" aria-pressed="{str(key == "all").lower()}">{label}</button>' for key,label in categories)}</div></div><div class="link-grid">{''.join(card(x) for x in regular)}</div><div class="no-results" hidden><span aria-hidden="true">☀</span><h3>A little too far off the beaten path.</h3><p>Try another word, or come back to all the island links.</p><button type="button" id="reset-search">Show all links</button></div><p class="result-status sr-only" role="status" aria-live="polite"></p><p class="group-note">Group links open in WhatsApp. Other links open in a new tab.</p></section>
<footer><div class="footer-wave" aria-hidden="true">∿ ∿ ∿</div><p>A little less scrolling. A little more sea.</p><div class="footer-links"><a href="https://github.com/its-gaib/phangan-links/issues/new?title=Suggest%20an%20island%20link" target="_blank" rel="noopener noreferrer">Suggest a link ↗</a><span>·</span><a href="https://github.com/its-gaib/phangan-links/issues/new?title=Report%20an%20outdated%20link" target="_blank" rel="noopener noreferrer">Something out of date?</a></div><details><summary>About these links & credits</summary><p>An independent, community-minded directory. Links checked 3 November 2026. WhatsApp previews were reachable; group activity and joining availability are unverified. Check current details directly with each provider.</p><p>Photography: <a href="https://unsplash.com/photos/oacWGBoBQ98">Elizabeth Gottwald / Unsplash</a>, used under the <a href="https://unsplash.com/license">Unsplash License</a>. Fonts: Fraunces & DM Sans (SIL Open Font License). No ads, analytics or tracking cookies.</p><p>For curious humans & helpful bots: <a href="/llms.txt">llms.txt</a> · <a href="/links.json">all links as JSON</a> · <a href="https://github.com/its-gaib/phangan-links">source code</a>.</p></details><span class="footer-signoff">MADE WITH LOVE FOR ISLAND LIFE <span aria-hidden="true">☼</span></span></footer></main></body></html>'''
OUT.mkdir(exist_ok=True)
(OUT/'index.html').write_text(page)
(OUT/'links.json').write_text(json.dumps({'name':'Phangan Links','url':SITE,'checkedAt':DATE,'verificationNote':'Public pages and WhatsApp invitation previews checked; activity, membership capacity and joining unverified. See repository research for evidence.','links':links},ensure_ascii=False,indent=2)+'\n')
md = '# Phangan Links\n\n> A curated link directory for life on Koh Phangan, Thailand.\n\nCanonical website: '+SITE+'/\n\nLinks checked '+DATE+'. Public previews do not prove group activity or joining availability. Independent directory; not an official island authority.\n\n'
for key,label in categories[1:]:
    md += '## '+label+'\n\n'+''.join(f"- [{x['title']}]({x['url']}): {x['description']}\n" for x in links if x['category']==key)+'\n'
md += '## Machine-readable resources\n\n- [JSON dataset]('+SITE+'/links.json): Every curated destination, category and verification context.\n- [Sitemap]('+SITE+'/sitemap.xml)\n- [Source and research](https://github.com/its-gaib/phangan-links)\n'
(OUT/'llms.txt').write_text(md)
(OUT/'llms-full.txt').write_text(md)
(OUT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+SITE+'/sitemap.xml\n')
(OUT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>'+SITE+'/</loc><lastmod>'+DATE+'</lastmod></url></urlset>\n')
hash_ = base64.b64encode(hashlib.sha256(structured.encode()).digest()).decode()
csp = f"default-src 'none'; script-src 'self' 'sha256-{hash_}'; style-src 'self'; img-src 'self'; font-src 'self'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'; form-action 'none'; object-src 'none'; upgrade-insecure-requests"
config = {'$schema':'https://openapi.vercel.sh/vercel.json','framework':None,'buildCommand':'python3 scripts/build.py','installCommand':'','outputDirectory':'public','headers':[{'source':'/(.*)','headers':[{'key':'Content-Security-Policy','value':csp},{'key':'X-Content-Type-Options','value':'nosniff'},{'key':'X-Frame-Options','value':'DENY'},{'key':'Referrer-Policy','value':'strict-origin-when-cross-origin'},{'key':'Permissions-Policy','value':'camera=(), microphone=(), geolocation=()'}]}]}
(ROOT/'vercel.json').write_text(json.dumps(config,indent=2)+'\n')
print(f'Built {len(links)} crawlable links and discovery resources')
