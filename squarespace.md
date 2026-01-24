# Squarespace DNS Setup for GitHub Pages

## Step-by-Step Guide

### 1. Access DNS Settings in Squarespace

1. Log in to your Squarespace account
2. Go to **Settings** → **Domains**
3. Click on **bertbullough.com**
4. Click **DNS Settings** (or **Advanced Settings** → **DNS**)

### 2. Configure DNS Records

You need to add these exact records:

#### A Records (for root domain)
Add **4 A records** all pointing to `@` or leave the Name field blank:

| Type | Name/Host | Value/Points To    |
|------|-----------|-------------------|
| A    | @         | 185.199.108.153   |
| A    | @         | 185.199.109.153   |
| A    | @         | 185.199.110.153   |
| A    | @         | 185.199.111.153   |

#### CNAME Record (for www subdomain)
| Type  | Name/Host | Value/Points To              |
|-------|-----------|------------------------------|
| CNAME | www       | YOUR_USERNAME.github.io      |

**Replace `YOUR_USERNAME` with your actual GitHub username!**

### 3. Remove Conflicting Records

**IMPORTANT:** Delete any existing A records or CNAME records that point elsewhere.

Common records to remove:
- Old A records pointing to Squarespace IPs
- CNAME for `@` (root can't be CNAME)
- Any parking page records

### 4. Save Changes

Click **Save** in Squarespace. DNS changes can take 24-48 hours to propagate globally.

### 5. Verify DNS Setup

After 10-15 minutes, check if DNS is working:

**On Mac/Linux:**
```bash
dig bertbullough.com
```

**On Windows:**
```cmd
nslookup bertbullough.com
```

You should see the GitHub IP addresses (185.199.108.153, etc.)

### 6. Enable HTTPS in GitHub Pages

1. Go to your GitHub repository settings
2. Navigate to **Pages**
3. Under "Custom domain", enter: `bertbullough.com`
4. Wait 24 hours for DNS propagation
5. Check **Enforce HTTPS**

## Troubleshooting

### DNS Not Propagating?
- Clear your browser cache
- Try incognito/private mode
- Check on different devices/networks
- Use https://www.whatsmydns.net to check global propagation

### "Domain not properly configured" in GitHub?
- Wait longer (DNS can take 24-48 hours)
- Double-check A records are exact
- Make sure CNAME file exists in your repo
- Verify no typos in domain name

### Still seeing Squarespace parking page?
- You may need to disconnect the domain from Squarespace websites
- Go to **Settings** → **Domains** → **bertbullough.com**
- If it's connected to a site, click **Disconnect**
- Keep the domain registered with Squarespace, just disconnect from any site

## Quick Reference - Your DNS Records

```
Type: A      Name: @    Value: 185.199.108.153
Type: A      Name: @    Value: 185.199.109.153
Type: A      Name: @    Value: 185.199.110.153
Type: A      Name: @    Value: 185.199.111.153
Type: CNAME  Name: www  Value: YOUR_USERNAME.github.io
```

## Timeline

- **0 mins**: Configure DNS in Squarespace ✓
- **15-30 mins**: DNS starts propagating
- **2-4 hours**: DNS works for most locations
- **24-48 hours**: Full global propagation
- **24+ hours**: Enable HTTPS in GitHub

## Need Help?

- [GitHub Pages Custom Domain Docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [Squarespace DNS Help](https://support.squarespace.com/hc/en-us/articles/205812378-Connecting-a-domain-to-your-site)

---

**Pro tip:** After DNS propagates, both `bertbullough.com` and `www.bertbullough.com` will work. GitHub will automatically redirect www to the root domain (or vice versa, your choice in settings).
