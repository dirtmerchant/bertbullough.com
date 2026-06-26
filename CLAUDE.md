# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal portfolio website for Bert Bullough. Static site hosted on GitHub Pages with custom domain bertbullough.com (DNS via Squarespace).

## Tech Stack

- Pure HTML/CSS/JavaScript — no frontend frameworks, this is intentional
- Python build script (`build.py`) generates the homepage and blog posts
- Fonts: DM Serif Display (headlines) + IBM Plex Mono (body) via Google Fonts
- Hosting: GitHub Pages with auto-deployment via GitHub Actions

## Local Development

```bash
# Build: generates index.html (homepage/blog listing) and blog/ posts from posts/
pip install -r requirements.txt
python3 build.py

# Serve locally
python3 -m http.server 8000
```

## Blog System

`build.py` converts Markdown posts into static HTML:

- **Source**: `posts/*.md` with YAML frontmatter (title, date, slug, tags, status)
- **Templates**: `_templates/post.html` and `_templates/blog-index.html` use `{{placeholder}}` syntax
- **Output**: `index.html` (homepage/blog listing) + `blog/{slug}/index.html` for clean URLs (the `blog/` directory is gitignored; `index.html` is committed via the build)
- **Filtering**: Only posts with `status: published` are built; drafts are skipped
- **Sitemap**: `sitemap.xml` is regenerated on each build

The deploy workflow (`deploy.yml`) runs `build.py` before publishing, so blog output doesn't need to be committed.

## Design Guidelines

- Editorial-style with refined brutalist edge
- Color scheme: Black (#1a1a1a) on off-white (#fafafa) with red accent (#ff4444), defined as CSS custom properties in `style.css`
- Grain texture overlay on body::before for character
- Keep pure HTML/CSS/JS — no frameworks
