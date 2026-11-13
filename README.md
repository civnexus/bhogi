# Autobiography of a Bhogi

A static literary website for Tridib Nandy. Live on GitHub Pages at https://civnexus.github.io/bhogi/ until bhogi.life DNS is connected.

## Content and editorial provenance

The three supplied recordings were used privately as editorial source. At the user’s request, neither recordings nor transcripts are included in the site or repository. No family names, locations, dates, or ancestral lineages have been inferred. The reading pages are explicitly labeled editorial adaptations and opening fragments, not completed first-person memoir chapters.

`content/book.json` contains chapter titles, text, and order. Edit it, then run `python3 build.py`. Each chapter gets a directly addressable HTML page, canonical URL, social metadata, and sitemap entry. Extend the chapters array to grow the book. Chapter navigation is generated automatically. Reading settings persist only in the visitor's browser; no tracking or third-party fonts are used.

## Preview and deployment

Run `python3 -m http.server 8765` in this folder. GitHub Pages publishes from main, repository root. Generated HTML is committed so no package installation or build service is required.

To connect bhogi.life: configure the domain's DNS for GitHub Pages using GitHub's current custom-domain instructions, then set the custom domain in repository Settings → Pages. Rebuild using `SITE_URL=https://bhogi.life python3 build.py`, commit the resulting metadata and CNAME, and push. Verify HTTPS before sharing the custom domain. Do not set the custom domain before DNS is ready, since Pages redirects the working github.io URL to it.

## Visual identity

Original AI-generated illustration: a golden arched window opening onto a river, birds and sunrise, framed by botanical ornament in midnight teal and antique gold. The scene is symbolic, not a depiction of Tridib's actual childhood location or family property. Generated using the built-in image tool, optimized to responsive WebP. `assets/social.jpg` is a dedicated 1200×630 sharing card with live-rendered typography; favicon.svg, favicon.ico, and apple-touch-icon.png share a window-and-sun motif.

Cover prompt: “Create an original literary book cover illustration for Autobiography of a Bhogi. No text: typography will be overlaid on website. Portrait 2:3. Mystical antique illuminated book atmosphere, deep midnight teal and aged gold etched fine lines, an elegant tall arched classroom window opening onto a luminous winding river, distant mountains and golden sunrise, little birds in flight, intricate botanical border, a subtle celestial circular diagram above arch. A sense of wonder and the invitation of the world beyond a window; balance of spiritual contemplation and earthly delight. Rich tactile printmaking, restrained premium editorial design, luminous mist. Original imagery, no existing fantasy characters or logos. Keep upper quarter dark and quiet for title overlay. Flat cover artwork, no mockup, no lettering.”
