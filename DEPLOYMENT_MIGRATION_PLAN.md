---
name: markets2mountains_deployment_migration_plan
description: Complete migration plan from WordPress hosting to GitHub Pages
domain: shop
file_type: workflow
last_updated: 2025-11-15
tags:
  - markets2mountains
  - deployment
  - migration
  - github-pages
audiences:
  - personal_productivity
topics:
  - web_development
  - deployment
related_docs:
  - "[[MIGRATION_PROGRESS]]"
---

# Markets2Mountains: WordPress to GitHub Pages Migration Plan

## Overview

**Current State:** WordPress site hosted on traditional webhost
**Target State:** Hugo static site on GitHub Pages with custom domain
**Timeline:** 2-3 hours total, minimal downtime

## Migration Architecture

```
WordPress (webhost)           Hugo Static Site (GitHub Pages)
└─ markets2mountains.com  →   └─ github.com/daharmattan1/markets2mountains
   └─ cPanel/MySQL               └─ Static HTML/CSS/JS
   └─ $X/month hosting           └─ Free hosting
   └─ Security updates           └─ No maintenance
   └─ Database required          └─ CDN included
```

## Phase 1: Pre-Migration Checklist (30 minutes)

### 1.1 Content Verification

- [x] All 40 blog posts migrated and rendering correctly
- [x] Featured images configured
- [x] About page created
- [ ] **Final content review** - Read through 3-5 posts to verify formatting
- [ ] **Test all internal links** - Ensure no broken links between posts
- [ ] **Verify images load** - Check featured images and inline images

### 1.2 URL Structure Planning

**WordPress URLs:**
```
https://markets2mountains.com/2018/11/10/post-title/
```

**Hugo URLs (current):**
```
https://markets2mountains.com/posts/post-title/
```

**Decision needed:**
- Option A: Keep Hugo structure, create redirects from old URLs
- Option B: Configure Hugo to match WordPress permalink structure

**Recommendation:** Option A (cleaner URLs + redirects)

### 1.3 Backup Current WordPress Site

**Critical: Do this before any DNS changes!**

```bash
# Via cPanel or SSH on current webhost:
# 1. Database backup
mysqldump -u username -p database_name > markets2mountains_backup.sql

# 2. Files backup
tar -czf markets2mountains_files_backup.tar.gz public_html/

# 3. Download backups to local machine
# Store in safe location (not in git repo!)
```

**Alternative:** Use WordPress export tool (already done for content)

## Phase 2: GitHub Repository Setup (15 minutes)

### 2.1 Initial Commit and Push

✅ **Status:** Repo exists at https://github.com/daharmattan1/markets2mountains

**Next steps:**

```bash
cd 05_shop/markets2mountains

# Stage all current changes (fonts, layouts, config)
git add .

# Create initial commit
git commit -m "Initial commit: Hugo site with Congo theme

- All 40 blog posts migrated from WordPress
- Custom fonts: DM Sans (headers), Instrument Sans (body)
- Centered Medium-style layout
- Congo theme configuration
- About page and site structure

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# Verify remote
git remote -v

# Push to GitHub
git push -u origin master
```

### 2.2 GitHub Pages Configuration

**In GitHub repo settings:**

1. Go to **Settings** → **Pages**
2. **Source:** Deploy from a branch
3. **Branch:** `master` (or `main` depending on default)
4. **Folder:** `/ (root)` or `/public` (need to decide)

**Important:** Hugo needs a build step. Two options:

#### Option A: Pre-built Site (Simpler)
- Build locally: `hugo` (generates `public/` directory)
- Deploy from `public/` folder
- Manual process: rebuild and commit when content changes

#### Option B: GitHub Actions (Recommended)
- Auto-build on every push
- Use Hugo GitHub Action
- No manual build step needed

**Recommendation:** Option B (GitHub Actions)

### 2.3 GitHub Actions Workflow

Create `.github/workflows/hugo.yml`:

```yaml
name: Deploy Hugo site to Pages

on:
  push:
    branches: ["master"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

defaults:
  run:
    shell: bash

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      HUGO_VERSION: 0.152.2
    steps:
      - name: Install Hugo CLI
        run: |
          wget -O ${{ runner.temp }}/hugo.deb https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_linux-amd64.deb \
          && sudo dpkg -i ${{ runner.temp }}/hugo.deb

      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: recursive

      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v5

      - name: Build with Hugo
        env:
          HUGO_CACHEDIR: ${{ runner.temp }}/hugo_cache
          HUGO_ENVIRONMENT: production
        run: |
          hugo \
            --minify \
            --baseURL "${{ steps.pages.outputs.base_url }}/"

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./public

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

## Phase 3: Custom Domain Configuration (30 minutes)

### 3.1 Add Custom Domain to GitHub Pages

**In GitHub repo → Settings → Pages:**

1. **Custom domain:** `markets2mountains.com`
2. **Enforce HTTPS:** ✅ (enable after DNS propagates)
3. GitHub creates a `CNAME` file in repo

### 3.2 DNS Configuration

**At your domain registrar (GoDaddy, Namecheap, etc.):**

#### For Apex Domain (markets2mountains.com):

**Option A: A Records (Recommended)**
```
Type: A
Name: @
Value: 185.199.108.153
TTL: 3600

Type: A
Name: @
Value: 185.199.109.153
TTL: 3600

Type: A
Name: @
Value: 185.199.110.153
TTL: 3600

Type: A
Name: @
Value: 185.199.111.153
TTL: 3600
```

#### For www subdomain:

```
Type: CNAME
Name: www
Value: daharmattan1.github.io
TTL: 3600
```

### 3.3 DNS Propagation Timeline

- **Minimum:** 30 minutes
- **Typical:** 2-4 hours
- **Maximum:** 48 hours

**Check propagation:** https://www.whatsmydns.net/

### 3.4 SSL/HTTPS Setup

GitHub Pages provides free SSL via Let's Encrypt:

1. Wait for DNS to propagate
2. In GitHub Pages settings, check **Enforce HTTPS**
3. Certificate provisioning: 5-15 minutes
4. Site will be accessible via `https://markets2mountains.com`

## Phase 4: URL Redirects (30-60 minutes)

### 4.1 Hugo Aliases for Old WordPress URLs

Add to each post's frontmatter:

```yaml
# In content/posts/post-name/index.md
aliases:
  - /2018/11/10/post-title/
  - /post-title/
```

**Automate this:**

```python
# Script: add_wordpress_aliases.py
import os
import re
from pathlib import Path

posts_dir = Path("content/posts")

for post_file in posts_dir.glob("*/index.md"):
    with open(post_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract date and slug from frontmatter
    date_match = re.search(r'date:\s*(\d{4})-(\d{2})-(\d{2})', content)
    slug = post_file.parent.name

    if date_match:
        year, month, day = date_match.groups()
        wp_url = f"/{year}/{month}/{day}/{slug}/"

        # Add alias if not already present
        if 'aliases:' not in content:
            # Insert after frontmatter opening
            content = content.replace('---\n', f'---\naliases:\n  - {wp_url}\n', 1)

            with open(post_file, 'w', encoding='utf-8') as f:
                f.write(content)

            print(f"Added alias to {slug}")
```

### 4.2 Verify Redirects Work

After deployment:

```bash
# Test old WordPress URL redirects to new Hugo URL
curl -I https://markets2mountains.com/2018/11/10/11-game-changing-mental-models-from-finance/

# Should return:
# HTTP/2 301 Moved Permanently
# Location: https://markets2mountains.com/posts/11-game-changing-mental-models-from-finance/
```

## Phase 5: Testing & Validation (30 minutes)

### 5.1 Pre-Launch Testing Checklist

**On staging URL (username.github.io/markets2mountains):**

- [ ] Homepage loads correctly
- [ ] All 40 posts accessible
- [ ] Featured images display
- [ ] About page works
- [ ] Navigation menu functional
- [ ] Search works (if enabled)
- [ ] Dark mode toggle works
- [ ] Mobile responsive
- [ ] Fonts loading (DM Sans, Instrument Sans)

### 5.2 Post-Launch Validation

**After DNS propagates:**

- [ ] `markets2mountains.com` resolves to GitHub Pages
- [ ] HTTPS certificate active (green padlock)
- [ ] Old WordPress URLs redirect correctly
- [ ] RSS feed accessible
- [ ] Sitemap generated (`/sitemap.xml`)
- [ ] Google Search Console verification
- [ ] Google Analytics migration (if used)

### 5.3 SEO Considerations

**Update in Hugo config:**

```toml
# config/_default/hugo.toml
baseURL = "https://markets2mountains.com/"

[params]
  description = "Insights on GTM, business strategy, and personal growth from 15 years scaling B2B SaaS"

[params.author]
  name = "Victor Sowers"

# Generate sitemap
[sitemap]
  changefreq = "weekly"
  priority = 0.5
```

**Submit to search engines:**

1. **Google Search Console**
   - Add property: `https://markets2mountains.com`
   - Submit sitemap: `https://markets2mountains.com/sitemap.xml`

2. **Bing Webmaster Tools**
   - Add site
   - Submit sitemap

## Phase 6: WordPress Decommission (After 30 days)

### 6.1 Monitoring Period (30 days)

**Keep WordPress site running for 30 days:**

- Monitor traffic analytics
- Watch for broken links
- Check search engine indexing
- Verify email addresses still work
- Ensure no dependencies on WordPress

### 6.2 WordPress Shutdown Process

**After confirming Hugo site is stable:**

1. **Download final backup**
   ```bash
   # Full site backup
   ssh user@webhost
   tar -czf markets2mountains_final_backup.tar.gz public_html/ databases/
   ```

2. **Redirect at webhost level (optional)**
   - Keep domain pointing to old host temporarily
   - Set up 301 redirect in `.htaccess`:
   ```apache
   RewriteEngine On
   RewriteCond %{HTTP_HOST} ^markets2mountains\.com$ [OR]
   RewriteCond %{HTTP_HOST} ^www\.markets2mountains\.com$
   RewriteRule ^(.*)$ https://markets2mountains.com/$1 [R=301,L]
   ```

3. **Cancel hosting plan**
   - Ensure no auto-renewal
   - Confirm domain registration is separate
   - Download final invoices for records

### 6.3 Post-Shutdown Checklist

- [ ] Final backup stored securely (3 locations)
- [ ] Domain registration valid for 1+ years
- [ ] DNS pointing to GitHub Pages
- [ ] Hosting account canceled
- [ ] Email forwarding configured (if needed)
- [ ] SSL certificates still valid

## Phase 7: Ongoing Maintenance

### 7.1 Content Updates Workflow

**Writing a new post:**

```bash
# 1. Create new post
hugo new posts/new-post-title/index.md

# 2. Write content in Markdown
# Add featured image to post directory

# 3. Preview locally
hugo server -D

# 4. Commit and push
git add .
git commit -m "Add new post: Title"
git push origin master

# 5. GitHub Actions auto-builds and deploys
# Live in ~2 minutes
```

### 7.2 Theme Updates

```bash
# Update Congo theme submodule
cd themes/congo
git pull origin stable

# Test locally
cd ../..
hugo server

# If good, commit
git add themes/congo
git commit -m "Update Congo theme to latest stable"
git push
```

### 7.3 Hugo Version Updates

**Update GitHub Actions workflow when new Hugo version released:**

```yaml
# .github/workflows/hugo.yml
env:
  HUGO_VERSION: 0.XXX.X  # Update this
```

## Cost Comparison

| Item | WordPress (Current) | Hugo on GitHub Pages (New) |
|------|---------------------|---------------------------|
| Hosting | $10-30/month | **FREE** |
| Domain | $15/year | $15/year |
| SSL Certificate | Included or $50/year | **FREE** (Let's Encrypt) |
| CDN | Extra $10-20/month | **FREE** (GitHub CDN) |
| Backups | $5-10/month | **FREE** (Git = backup) |
| Security Updates | Manual effort | **Not needed** (static) |
| **Total Annual** | **$150-400** | **$15** |

**Savings:** $135-385/year

## Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| DNS propagation delay | Site temporarily down | Schedule during low-traffic period (weekend) |
| Old URLs break | Lost traffic/SEO | Implement aliases for all old URLs |
| Images don't load | Poor UX | Test all image paths before launch |
| SSL cert delay | HTTPS warning | Wait for DNS fully propagated before forcing HTTPS |
| GitHub Pages downtime | Site unavailable | GitHub Pages has 99.9% uptime SLA |

## Success Metrics

**Track these for 30 days post-migration:**

- [ ] 100% of old URLs redirect correctly
- [ ] No increase in bounce rate
- [ ] Page load time improved (target: <2 seconds)
- [ ] Google Search Console shows no crawl errors
- [ ] Traffic levels remain stable
- [ ] All images loading correctly
- [ ] Mobile usability score maintained/improved

## Rollback Plan

**If migration fails catastrophically:**

1. **Immediate:** Change DNS back to old webhost
   - Propagation: 1-4 hours
   - Site back online at old location

2. **Keep WordPress site running** until 100% confident in Hugo site

3. **Domain registrar backup:**
   - Keep old hosting account active for 30 days
   - Easy to revert DNS if needed

## Timeline Summary

| Phase | Duration | Can Do Now | Must Wait |
|-------|----------|-----------|-----------|
| Pre-migration checks | 30 min | ✅ Yes | - |
| GitHub setup | 15 min | ✅ Yes | - |
| GitHub Actions config | 15 min | ✅ Yes | - |
| Initial deployment test | 10 min | ✅ Yes | - |
| DNS configuration | 5 min | ⏳ Only when ready to go live | - |
| DNS propagation | 2-4 hours | - | ⏳ Must wait |
| SSL provisioning | 15 min | - | ⏳ After DNS |
| URL redirect testing | 30 min | - | ⏳ After deployment |
| **Total active time** | **~2 hours** | | |
| **Total elapsed time** | **~4-6 hours** | | |

## Next Steps

**Immediate (Can do now):**
1. ✅ Commit current Hugo site to GitHub
2. ✅ Set up GitHub Actions workflow
3. ✅ Test deployment to `username.github.io/markets2mountains`
4. ⏳ Add WordPress URL aliases to all posts
5. ⏳ Final content review and testing

**When Ready to Go Live (Schedule a 4-hour window):**
1. ⏳ Create final WordPress backup
2. ⏳ Configure custom domain in GitHub Pages
3. ⏳ Update DNS records at domain registrar
4. ⏳ Wait for DNS propagation
5. ⏳ Enable HTTPS enforcement
6. ⏳ Test all redirects and functionality
7. ✅ Celebrate! 🎉

**Post-Launch (30 days):**
1. Monitor analytics and search rankings
2. Fix any discovered issues
3. Decommission WordPress hosting
4. Update any external links to new URLs

---

*Last Updated: 2025-11-15*
*Status: Ready for execution*
*Estimated Savings: $135-385/year*
*Downtime Risk: Minimal (2-4 hours DNS propagation)*
