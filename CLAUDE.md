# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal portfolio website for Bert Bullough. Static HTML/CSS/JS site hosted on GitHub Pages with custom domain bertbullough.com (registered with Squarespace).

## Tech Stack

- Pure HTML/CSS/JavaScript (no build process, no frameworks)
- Fonts: DM Serif Display (headlines) + IBM Plex Mono (body) via Google Fonts
- Hosting: GitHub Pages with auto-deployment via GitHub Actions

## Local Development

```bash
# Open index.html directly in browser, or run local server:
python3 -m http.server 8000
# Visit: http://localhost:8000
```

## Deployment

Push to main branch. GitHub Actions auto-deploys in 1-2 minutes.

```bash
git add .
git commit -m "Description of changes"
git push
```

## Design Guidelines

- Editorial-style with refined brutalist edge
- Color scheme: Black (#1a1a1a) on off-white (#fafafa) with red accent (#ff4444)
- Grain texture overlay for character
- Keep pure HTML/CSS/JS - no frameworks, this is intentional
