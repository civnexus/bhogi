"""Build the public Bhogi Life site. SITE_URL overrides the production URL."""
import os,json,html
from pathlib import Path
ROOT=Path(__file__).parent
SITE=os.environ.get('SITE_URL','https://www.bhogi.life').rstrip('/')
data=json.loads((ROOT/'content/book.json').read_text())
esc=html.escape
DESC='An illustrated introduction to Tridib Nandy’s life, from spiritual roots and early Bitcoin to digital currency, music, travel, and traditional healers around the world.'
def head(title,path='',prefix='',description=DESC):
 url=SITE+'/'+path
 schema={'@context':'https://schema.org','@type':'WebPage','name':title,'url':url,'description':description,'isPartOf':{'@type':'WebSite','name':data['title'],'alternateName':data['alternateTitle'],'url':SITE+'/'},'about':{'@type':'CreativeWork','name':data['title'],'alternateName':data['alternateTitle'],'author':{'@type':'Person','name':data['author']},'inLanguage':'en','creativeWorkStatus':'Work in progress'}}
 return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><meta name="description" content="{esc(description)}"><meta name="theme-color" content="#062326"><link rel="canonical" href="{url}"><meta name="robots" content="index,follow"><meta property="og:type" content="website"><meta property="og:site_name" content="Autobiography of a Bhogi"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/bhogi-mountain-share.jpg"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:type" content="image/jpeg"><meta property="og:image:alt" content="Autobiography of a Bhogi beside a mountain portrait of Tridib Nandy"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(description)}"><meta name="twitter:image" content="{SITE}/assets/bhogi-mountain-share.jpg"><meta name="twitter:image:alt" content="Autobiography of a Bhogi by Tridib Nandy"><link rel="icon" href="{prefix}favicon.ico" sizes="any"><link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png"><link rel="stylesheet" href="{prefix}assets/style.css"><script type="application/ld+json">{json.dumps(schema,ensure_ascii=False)}</script></head>'''
def header(prefix=''):
 return f'''<a class="skip" href="#main">Skip to content</a><header class="wrap topbar"><a class="brand" href="{prefix}index.html" aria-label="bhogi.life home">bhogi<span>.</span>life</a><nav aria-label="Main navigation"><a href="{prefix}index.html#story">The story</a><a href="{prefix}index.html#technology">Technology</a><a href="{prefix}index.html#music">Music</a><a href="{prefix}index.html#archive">Archive</a><a href="{prefix}index.html#about">About the book</a></nav></header>'''
def footer(prefix=''):
 return f'''<footer class="wrap"><span>© Tridib Nandy · Autobiography of a Bhogi</span><span>A life in the telling. <a href="{prefix}index.html#story">Explore the story</a></span></footer>'''
def photo(name, alt, caption, css_class='', priority=False):
    loading = 'fetchpriority="high"' if priority else 'loading="lazy" decoding="async"'
    return f'''<figure class="story-photo {css_class}"><img src="assets/photos/{name}.webp" {loading} alt="{esc(alt)}"><figcaption>{esc(caption)}</figcaption></figure>'''

def clip(name, caption):
    return f'''<figure class="story-photo archive-clip">
      <video controls playsinline preload="none" poster="assets/video/{name}.webp" aria-label="{esc(caption)}">
        <source src="assets/video/{name}.mp4" type="video/mp4">
        <a href="assets/video/{name}.mp4">Open video</a>
      </video>
      <figcaption>{esc(caption)}</figcaption>
    </figure>'''


travel = [
    ('on-the-tarmac', 'Tridib with a rolling bag on the tarmac in front of a jet', 'On the tarmac'),
    ('on-the-helipad', 'Tridib standing beside an orange and white helicopter', 'On the helipad'),
    ('boarding-the-helicopter', 'Tridib sitting in the doorway of a red and white helicopter', 'Ready for takeoff'),
    ('cockpit-view', 'Two pilots at the controls, seen from behind', 'From behind the cockpit seats'),
    ('in-flight', 'Tridib and a companion smiling inside a helicopter', 'In flight'),
    ('travel-keepsakes', 'Redacted boarding passes lying over a passport cover', 'Keepsakes from the road'),
]

archive = [
    ('outside-baba', 'Two friends smiling outside the Baba storefront', 'Outside Baba'),
    ('courtyard-portrait', 'Tridib standing in a courtyard with a broom', 'In the courtyard'),
    ('las-vegas-cannabis-tour', 'Tridib standing beside a green cannabis tour van', 'Cannabis culture in Las Vegas'),
    ('tridib-portrait', 'Tridib Nandy smiling at an outdoor café table', 'Tridib Nandy at a café'),
    ('around-the-table', 'A group laughing around a table', 'Around the table with Richard Branson'),
    ('bombay-hemp-company', 'Three people smiling beneath a Bombay Hemp Company sign', 'At Bombay Hemp Company'),
    ('ayush-entrance', 'Tridib beside the Ministry of AYUSH entrance sign', 'Outside India’s Ministry of AYUSH'),
    ('out-on-the-water', 'Two people aboard a white boat', 'Bhogimaxxing'),
    ('group-portrait', 'Four people standing together indoors', 'From the personal archive'),
    ('cannabis-market', 'Panoramic view of cannabis retail counters', 'Inside a cannabis marketplace'),
]

index = head('Autobiography of a Bhogi | Tridib Nandy') + '<body>' + header() + f'''
<main id="main">
  <section class="wrap hero" aria-labelledby="book-title">
    <div>
      <p class="eyebrow">A memoir in progress · Tridib Nandy</p>
      <h1 id="book-title">Autobiography<br>of a <em>Bhogi</em></h1>
      <p class="intro">From a pious childhood to early Bitcoin, cannabis, and the traditional healers he met along the way.</p>
      <a class="button" href="#story">Explore the story</a>
    </div>
    {photo('tridib-mountain', 'Tridib Nandy standing on a stone path above a mountain valley', 'Tridib Nandy', 'hero-portrait', priority=True)}
  </section>

  <section class="paper" id="story">
    <div class="wrap">
      <div class="split">
        <h2>The boy at<br>the window</h2>
        <div class="prose">
          <p>Tridib grew up in a pious family among stories of yogis. At school, his attention drifted toward the birds outside the classroom. Music and sport were easier to pay attention to. That boyhood tug between contemplation and the world beyond the window gives the memoir its starting point.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="wrap section story-section" aria-label="The story outline">
    <article class="story-feature" id="technology">
      <div class="prose">
        <p class="eyebrow">Technology</p>
        <h2>From early Bitcoin<br>to digital government</h2>
        <p>Tridib traces his discovery of Bitcoin to a sabbatical in Hawaiʻi around 2010–11. By December 2013, India’s first Bitcoin conference was drawing people to Bangalore to talk about how digital money might work in practice.</p>
        <p>In 2018 he founded Sovereign Union to develop digital tools for Pacific island governments, including digital IDs, wallets, and land registries. In 2020, the company announced an early digital-currency pilot in Palau following a letter of intent from the Ministry of Finance.</p>
        <p>His work now focuses on how public institutions and regulated issuers can design and govern digital currencies, including central bank digital currencies and stablecoins.</p>
        <p class="story-sources"><a href="https://tridibnandy.tech/">Tridib’s professional biography</a> · <a href="https://cio.economictimes.indiatimes.com/news/corporate-news/bangalore-to-host-indias-first-bitcoin-conference/26413131">2013 conference coverage</a></p>
      </div>
      {photo('coastal-road', 'A white convertible parked beside the ocean', 'A coastal drive from the personal archive')}
    </article>

    <article class="story-feature">
      {photo('cannabis-archive', 'Tridib working with cannabis plants by hand', 'A photograph from Tridib’s cannabis years')}
      <div class="prose">
        <h2>Cannabis and the people behind it</h2>
        <p>Cannabis took Tridib into a world of growers, entrepreneurs, and advocates. The photographs bring that part of the story down to earth, from working with the plant by hand to visiting a retail floor and meeting people at Bombay Hemp Company.</p>
      </div>
    </article>

    <article class="story-feature">
      <div class="prose">
        <h2>In the company<br>of healers</h2>
        <p>Tridib’s interest in traditional medicine brought him into contact with healers around the world. In India, the photo archive takes us from the entrance of the Ministry of AYUSH to an Ayurvedic research division. The memoir will follow the people he met and worked with, and what they taught him about how knowledge is passed from one person to another.</p>
      </div>
      {photo('ayurveda-research', 'Two people in front of an Ayurvedic research division sign', 'At an Ayurvedic drug discovery and development division')}
    </article>
  </section>

  <section class="paper" id="music">
    <div class="wrap split">
      <h2>A life with music</h2>
      <div class="prose">
        <p>Music was one of the things that held Tridib’s attention as a boy. He plays guitar and piano, and that love of making music found its way into his work. He co-founded Musiverse to explore how blockchain could help musicians raise money directly from their listeners.</p>
      </div>
    </div>
  </section>

  <section class="wrap section" id="travel">
    <h2>On the road and in the air</h2>
    <div class="photo-grid travel-photos">{''.join(photo(*item) for item in travel)}</div>
    <div class="archive-clips">
      {clip('helicopter-boarding', 'Walking out to the helicopter')}
      {clip('valley-from-above', 'A valley seen from the helicopter')}
    </div>
  </section>

  <section class="paper" id="archive">
    <div class="wrap">
      <h2>From the photo archive</h2>
      <div class="photo-grid">{''.join(photo(*item) for item in archive)}</div>
    </div>
  </section>

  <section class="wrap section" id="about">
    <div class="split about-book">
      <figure class="cover"><img src="assets/cover-860.webp" srcset="assets/cover-480.webp 480w, assets/cover-860.webp 860w" sizes="(max-width:760px) 270px, 320px" width="860" height="1290" loading="lazy" decoding="async" alt="Illustrated book cover showing a golden arched window opening onto a river"><figcaption class="cover-title"><span class="cover-kicker">Autobiography</span><span class="cover-of">of a</span><span class="cover-name">Bhogi</span><small>TRIDIB NANDY</small></figcaption></figure>
      <div class="prose">
        <h2>About the book</h2>
        <p>The title is a nod to Paramahansa Yogananda’s <em>Autobiography of a Yogi</em>. Tridib gives the title a turn of his own. The bhogi is drawn to the world and wants to see what experience can teach him. That impulse runs through the boy at the window and the man who went looking for unfamiliar ideas and people.</p>
        <p>The full memoir will appear here as an online book as Tridib develops it.</p>
      </div>
    </div>
  </section>
</main>''' + footer() + '</body></html>'
(ROOT/'index.html').write_text(index)

for chapter in data['chapters']:
    target = '../index.html#story'
    (ROOT/'chapters'/f"{chapter['slug']}.html").write_text(
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<title>The story | Bhogi Life</title><meta name="robots" content="noindex">'
        f'<meta http-equiv="refresh" content="0;url={target}">'
        f'</head><body><p><a href="{target}">Explore the story</a></p></body></html>'
    )

urls = [SITE+'/']
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+u+'</loc></url>' for u in urls)+'</urlset>\n')
(ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+SITE+'/sitemap.xml\n')
(ROOT/'.nojekyll').touch()
(ROOT/'404.html').write_text(head('Page not found — Bhogi',prefix=SITE+'/')+'<body>'+header(SITE+'/')+ '<main id="main" class="wrap section"><p class="eyebrow">A page beyond the story</p><h1>This page has not been written.</h1><p><a href="'+SITE+'/">Return to the book </a></p></main>'+footer(SITE+'/')+'</body></html>')
print('Built the story, legacy redirects, sitemap, robots and 404 for '+SITE)
