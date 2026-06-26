#!/usr/bin/env python3
"""Build blog posts from Markdown source files.

Reads posts/*.md with YAML frontmatter, converts to HTML using templates,
and writes to blog/{slug}/index.html for clean URLs. Also generates a
blog index page and updates sitemap.xml.

Dependencies: markdown, pyyaml (see requirements.txt)
"""

import os
import shutil
from datetime import date, datetime
from pathlib import Path

import markdown
import yaml

ROOT = Path(__file__).resolve().parent
POSTS_DIR = ROOT / "posts"
BLOG_DIR = ROOT / "blog"
TEMPLATES_DIR = ROOT / "_templates"
SITEMAP_PATH = ROOT / "sitemap.xml"
SITE_URL = "https://bertbullough.com"


def parse_post(path: Path) -> dict | None:
    """Parse a markdown file with YAML frontmatter.

    Returns a dict with keys: title, date, slug, tags, status, content (raw md),
    or None if the file has no valid frontmatter.
    """
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None

    # Split on the second --- to separate frontmatter from body
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None

    meta = yaml.safe_load(parts[1])
    if not meta:
        return None

    body = parts[2].strip()

    # Normalize date to a date object
    post_date = meta.get("date")
    if isinstance(post_date, str):
        post_date = datetime.strptime(post_date, "%Y-%m-%d").date()
    elif isinstance(post_date, datetime):
        post_date = post_date.date()

    return {
        "title": meta.get("title", path.stem),
        "date": post_date,
        "slug": meta.get("slug", path.stem),
        "tags": meta.get("tags", []),
        "status": meta.get("status", "draft"),
        "content": body,
    }


def render_post(post: dict, template: str) -> str:
    """Render a single post dict into the post HTML template."""
    html_content = markdown.markdown(
        post["content"],
        extensions=["fenced_code", "tables", "smarty"],
    )

    date_str = post["date"].strftime("%B %d, %Y") if post["date"] else ""

    tags_html = ""
    if post["tags"]:
        tag_spans = " ".join(
            f'<span class="tag">{tag}</span>' for tag in post["tags"]
        )
        tags_html = f' &bull; {tag_spans}'

    html = template.replace("{{title}}", post["title"])
    html = html.replace("{{date}}", date_str)
    html = html.replace("{{tags}}", tags_html)
    html = html.replace("{{content}}", html_content)

    return html


def render_blog_index(posts: list[dict], template: str) -> str:
    """Render the blog listing page from published posts."""
    if not posts:
        posts_html = "<p>No posts yet.</p>"
    else:
        items = []
        for post in posts:
            date_str = post["date"].strftime("%B %d, %Y") if post["date"] else ""
            tags_html = ""
            if post["tags"]:
                tag_spans = " ".join(
                    f'<span class="tag">{tag}</span>' for tag in post["tags"]
                )
                tags_html = f'<div class="project-tags">{tag_spans}</div>'

            items.append(
                f'<div class="post-item">\n'
                f'    <div class="post-item-meta">{date_str}</div>\n'
                f'    <h3><a href="/blog/{post["slug"]}/">{post["title"]}</a></h3>\n'
                f"    {tags_html}\n"
                f"</div>"
            )
        posts_html = "\n".join(items)

    return template.replace("{{posts}}", posts_html)


def generate_sitemap(posts: list[dict]) -> str:
    """Generate sitemap.xml content including blog posts."""
    today = date.today().isoformat()
    urls = [
        f"    <url>\n"
        f"        <loc>{SITE_URL}/</loc>\n"
        f"        <lastmod>{today}</lastmod>\n"
        f"        <changefreq>monthly</changefreq>\n"
        f"        <priority>1.0</priority>\n"
        f"    </url>",
        f"    <url>\n"
        f"        <loc>{SITE_URL}/blog/</loc>\n"
        f"        <lastmod>{today}</lastmod>\n"
        f"        <changefreq>weekly</changefreq>\n"
        f"        <priority>0.8</priority>\n"
        f"    </url>",
    ]

    for post in posts:
        post_date = post["date"].isoformat() if post["date"] else today
        urls.append(
            f"    <url>\n"
            f'        <loc>{SITE_URL}/blog/{post["slug"]}/</loc>\n'
            f"        <lastmod>{post_date}</lastmod>\n"
            f"        <changefreq>monthly</changefreq>\n"
            f"        <priority>0.6</priority>\n"
            f"    </url>"
        )

    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )


def build():
    """Main build: convert all published posts to HTML, generate index + sitemap."""
    # Load templates
    post_template = (TEMPLATES_DIR / "post.html").read_text(encoding="utf-8")
    index_template = (TEMPLATES_DIR / "blog-index.html").read_text(encoding="utf-8")

    # Parse all posts
    posts = []
    if POSTS_DIR.exists():
        for md_file in sorted(POSTS_DIR.glob("*.md")):
            post = parse_post(md_file)
            if post and post["status"] == "published":
                posts.append(post)

    # Sort by date descending
    posts.sort(key=lambda p: p["date"] or date.min, reverse=True)

    # Clean and recreate blog directory
    if BLOG_DIR.exists():
        shutil.rmtree(BLOG_DIR)
    BLOG_DIR.mkdir(parents=True)

    # Render each post
    for post in posts:
        post_dir = BLOG_DIR / post["slug"]
        post_dir.mkdir(parents=True, exist_ok=True)
        html = render_post(post, post_template)
        (post_dir / "index.html").write_text(html, encoding="utf-8")
        print(f"  built: blog/{post['slug']}/index.html")

    # Render blog index
    index_html = render_blog_index(posts, index_template)
    (BLOG_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print(f"  built: blog/index.html ({len(posts)} posts)")

    # Update sitemap
    sitemap = generate_sitemap(posts)
    SITEMAP_PATH.write_text(sitemap, encoding="utf-8")
    print(f"  built: sitemap.xml")


if __name__ == "__main__":
    print("Building blog...")
    build()
    print("Done.")
