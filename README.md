# bertbullough.com

Personal portfolio website hosted on GitHub Pages.

## Quick Start

```bash
# Local development
python3 -m http.server 8000
# Visit http://localhost:8000
```

## Deployment

Push to `main` branch. GitHub Actions auto-deploys in 1-2 minutes.

## Tech Stack

- Pure HTML/CSS/JavaScript (no build process)
- Fonts: DM Serif Display + IBM Plex Mono
- Hosting: GitHub Pages
- Domain: bertbullough.com via Squarespace DNS

## Files

- `index.html` - Main site
- `404.html` - Custom error page
- `CNAME` - Custom domain config
- `robots.txt` / `sitemap.xml` - SEO

## Customization

Edit CSS variables in `index.html`:

```css
:root {
    --ink: #1a1a1a;      /* Main text */
    --paper: #fafafa;    /* Background */
    --accent: #ff4444;   /* Red accent */
}
```

## DNS Setup

See `squarespace.md` for Squarespace DNS configuration.
