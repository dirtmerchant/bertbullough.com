# Quick Reference

## Deploy Changes

```bash
git add .
git commit -m "Description"
git push
```

## Local Preview

```bash
python3 -m http.server 8000
```

## Add a Project

Edit `index.html`, add in the projects section:

```html
<div class="project-card">
    <div class="project-meta">YEAR &bull; CATEGORY</div>
    <h3>Project Name</h3>
    <p>Description...</p>
    <div class="project-tags">
        <span class="tag">Tag</span>
    </div>
</div>
```

## Update Contact Links

In `index.html` footer, update:
- GitHub URL
- Twitter URL
- LinkedIn URL
- Email address

## DNS Records (Squarespace)

```
A     @    185.199.108.153
A     @    185.199.109.153
A     @    185.199.110.153
A     @    185.199.111.153
CNAME www  dirtmerchant.github.io
```
