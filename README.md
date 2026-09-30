# links - personal website for posters and conferences

My personal landing page for posters, talks and conferences: the QR code on a poster points here.
It shows the current poster's paper, related papers, links (Scholar, LinkedIn, GitHub, email) and a web CV.

- Live: https://ad045.github.io/links/ (CV: https://ad045.github.io/links/cv.html)
- Repo: https://github.com/ad045/links (GitHub Pages, deployed from `main`, root)
- Local folder: `~/Documents/01_projects/30_links_page`

## Files

- `index.html` - landing page (current poster, related paper, links)
- `cv.html` - web CV
- `style.css` - shared styling, taken from the mapping paper / poster (IBM Plex Sans, orange `#FE961F`, blue `#3FA5C4`)
- `make_qr.py` - generates `qr.svg` (print) and `qr.png` (slides) for `https://ad045.github.io/links/`
- `ideas.md` - ideas for later

## Updating

Edit the HTML, then `git push`; GitHub Pages redeploys in about a minute.
Keep the URL stable: printed posters point at `https://ad045.github.io/links/`, so do not rename the repo.

For a new poster, replace the "This poster" card in `index.html`; the QR code stays the same.
