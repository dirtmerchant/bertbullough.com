# bertbullough.com - Portfolio Site Project

## Project Overview
Personal portfolio website for Bert Bullough hosted on GitHub Pages with custom domain bertbullough.com (registered with Squarespace).

## Project Structure
```
bertbullough.com/
├── index.html              # Main landing page
├── 404.html                # Custom 404 error page
├── CNAME                   # Custom domain config
├── robots.txt              # SEO - search engine directives
├── sitemap.xml             # SEO - site structure
├── .gitignore              # Git ignore rules
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions auto-deployment
├── README.md               # Full documentation
├── QUICKSTART.md           # Quick reference guide
├── SQUARESPACE_DNS.md      # Squarespace DNS setup guide
└── deploy.sh               # Interactive deployment script
```

## Technology Stack
- Pure HTML/CSS/JavaScript (no build process)
- Fonts: DM Serif Display (headlines) + IBM Plex Mono (body)
- Hosting: GitHub Pages
- Domain: bertbullough.com via Squarespace DNS
- Auto-deployment: GitHub Actions

## Design Aesthetic
- Editorial-style with refined brutalist edge
- Color scheme: Black (#1a1a1a) on off-white (#fafafa) with red accent (#ff4444)
- Grain texture overlay for character
- Smooth animations and micro-interactions
- Fully responsive layout

## Current Status
- ✅ Complete site structure built
- ✅ All configuration files ready
- ✅ GitHub Actions workflow configured
- ✅ SEO optimization complete
- ⏳ Pending: Initial GitHub deployment
- ⏳ Pending: Squarespace DNS configuration
- ⏳ Pending: Custom domain setup in GitHub Pages

## Deployment Steps

### 1. GitHub Repository Setup
```bash
# Initialize and push to GitHub
git init
git add .
git commit -m "Initial commit - portfolio site"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/bertbullough.com.git
git push -u origin main
```

### 2. Enable GitHub Pages
- Go to repository Settings → Pages
- Source: Deploy from branch
- Branch: main, folder: / (root)
- Save

### 3. Squarespace DNS Configuration
Add these DNS records in Squarespace (Settings → Domains → bertbullough.com → DNS Settings):

**A Records (all pointing to @):**
- 185.199.108.153
- 185.199.109.153
- 185.199.110.153
- 185.199.111.153

**CNAME Record:**
- Name: www
- Value: YOUR_USERNAME.github.io

**Important:** Delete any conflicting A or CNAME records

### 4. GitHub Custom Domain Setup
- After DNS propagates (24-48 hours)
- GitHub Pages settings → Custom domain: bertbullough.com
- Enable "Enforce HTTPS"

## Content Updates Needed

### Priority 1: Contact Information
Update in `index.html` footer section:
- GitHub: https://github.com/yourusername
- Twitter: https://twitter.com/yourusername
- LinkedIn: https://linkedin.com/in/yourusername
- Email: hello@bertbullough.com (or your preferred email)

### Priority 2: Projects Section
Replace example project cards in `index.html` with real projects:
```html
<div class="project-card">
    <div class="project-meta">YEAR • CATEGORY</div>
    <h3>Project Name</h3>
    <p>Project description...</p>
    <div class="project-tags">
        <span class="tag">Technology</span>
        <span class="tag">Stack</span>
    </div>
</div>
```

### Priority 3: Hero Section
Customize the hero intro text in `index.html` to better reflect your background and interests.

## Common Tasks

### Deploy Updates
```bash
git add .
git commit -m "Description of changes"
git push
```
Site updates automatically in 1-2 minutes via GitHub Actions.

### Local Testing
```bash
# Simple: just open index.html in browser
# Or run local server:
python3 -m http.server 8000
# Visit: http://localhost:8000
```

### Add New Project
1. Edit `index.html`
2. Add new `<div class="project-card">` in the projects section
3. Commit and push

### Update Sitemap
After adding new pages, update `sitemap.xml` with new URLs and dates.

## Design Customization

### Color Scheme
Modify CSS variables in `index.html`:
```css
:root {
    --ink: #1a1a1a;      /* Main text */
    --paper: #fafafa;    /* Background */
    --accent: #ff4444;   /* Red accent */
    --mid: #666;         /* Secondary text */
    --border: #d0d0d0;   /* Borders */
}
```

### Typography
Current fonts loaded from Google Fonts:
- Display: DM Serif Display (serif, distinctive)
- Body: IBM Plex Mono (monospace, technical)

To change fonts, update the Google Fonts link and CSS font-family declarations.

## Troubleshooting

### Site Not Updating
- Wait 1-2 minutes for GitHub Actions to complete
- Check Actions tab: github.com/USERNAME/REPO/actions
- Hard refresh browser: Ctrl+Shift+R or Cmd+Shift+R

### Custom Domain Not Working
- Verify CNAME file contains: bertbullough.com
- Check DNS propagation: whatsmydns.net
- DNS can take 24-48 hours to fully propagate
- Ensure no typos in Squarespace DNS records

### HTTPS Issues
- Wait 24+ hours after DNS propagation
- GitHub needs time to provision SSL certificate
- Check "Enforce HTTPS" is enabled in Pages settings

## Future Enhancements

### Potential Additions
- Blog section (add blog.html or use Jekyll/Hugo)
- Individual project detail pages
- Contact form (using Formspree or similar)
- Analytics (Google Analytics, Plausible, etc.)
- Dark/light mode toggle
- Project filtering by tags
- RSS feed for updates

### Scaling Options
- Keep as static site (current approach)
- Add static site generator (11ty, Hugo, Jekyll)
- Add CMS (Netlify CMS, Forestry, Tina)
- Migrate to framework (Next.js, Astro) if needed

## Key Files Reference

**index.html** - Main site file, update for content changes
**SQUARESPACE_DNS.md** - DNS configuration guide specific to Squarespace
**QUICKSTART.md** - Quick reference for common tasks
**README.md** - Full documentation and setup guide
**deploy.sh** - Interactive script for initial setup

## Notes for AI Assistant
- User prefers clean, minimal interaction
- Focus on efficiency and quick deployment
- Squarespace is domain registrar (DNS only, not hosting)
- Target: Get site live as quickly as possible
- Design style: Editorial brutalist, not generic AI aesthetic
- No frameworks needed - pure HTML/CSS/JS is intentional
- Auto-deployment via GitHub Actions is configured
- User may want to add projects incrementally over time

## GitHub Username Required
Replace `YOUR_USERNAME` throughout this project with actual GitHub username before deployment.
