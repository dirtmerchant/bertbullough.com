---
title: "How This Site Is Built"
date: 2026-06-26
slug: how-this-site-is-built
tags: [meta, python, github-actions]
status: published
---

This site runs on a 180-line Python script, two HTML templates, and a GitHub Actions workflow. No static site generator, no JavaScript framework, no build toolchain beyond `pip install markdown pyyaml`. Here's how the whole thing works.

## The source files

Posts live in a `posts/` directory as Markdown files with YAML frontmatter:

```markdown
---
title: "How This Site Is Built"
date: 2026-06-26
slug: how-this-site-is-built
tags: [meta, python]
status: published
---

Post content goes here.
```

The `status` field controls publishing. Set it to `draft` and the build skips it. Set it to `published` and it goes live on the next push.

## The build script

`build.py` does three things:

1. **Parses posts** -- reads each `.md` file, splits the YAML frontmatter from the Markdown body, and filters to only `status: published`.

2. **Renders HTML** -- converts Markdown to HTML using Python's `markdown` library (with fenced code blocks, tables, and smart quotes), then drops the result into simple HTML templates using `{{placeholder}}` string replacement. No Jinja, no template engine. Just `str.replace()`.

3. **Generates output** -- writes each post to `{slug}/index.html` for clean URLs (so `/how-this-site-is-built/` instead of `/how-this-site-is-built.html`), generates the homepage as a post listing, and rebuilds `sitemap.xml`.

The templates are plain HTML files with placeholders like `{{title}}`, `{{date}}`, `{{content}}`, and `{{posts}}`. The build script reads them, replaces the placeholders, writes the output. That's it.

## The deploy pipeline

A GitHub Actions workflow in `.github/workflows/deploy.yml` handles deployment:

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-python@v5
    with:
      python-version: '3.12'
  - run: pip install -r requirements.txt
  - run: python3 build.py
  - uses: actions/upload-pages-artifact@v3
    with:
      path: '.'
  - uses: actions/deploy-pages@v4
```

Push to `main`, the workflow checks out the repo, installs two Python packages, runs the build, and deploys to GitHub Pages. The whole thing finishes in under a minute.

## Why not use a real static site generator?

I've used Jekyll, Hugo, and Gatsby on other projects. They're fine. But for a personal site with a handful of posts, they're overkill. I don't need plugins, themes, asset pipelines, or hot module replacement. I need Markdown in, HTML out.

The build script is small enough to read in one sitting, easy to modify, and has exactly two dependencies. When something breaks, there are about 180 lines of code to look at. That's the whole debugging surface.

## The stack

- **Content**: Markdown with YAML frontmatter
- **Build**: Python (`markdown` + `pyyaml`), ~180 lines
- **Templates**: Plain HTML with `{{placeholder}}` replacement
- **Styling**: Hand-written CSS, no framework
- **Hosting**: GitHub Pages
- **Deploy**: GitHub Actions, triggered on push to `main`
- **DNS**: Squarespace (custom domain)

Total JavaScript on the site: zero bytes.
