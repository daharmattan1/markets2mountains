# Quick Start: Migrate Your WordPress Blog

## Step 1: Export from WordPress (5 minutes)

1. **Log into your WordPress admin**
   - Go to: https://markets2mountains.com/wp-admin

2. **Export your content**
   - Click **Tools** → **Export**
   - Select **Posts**
   - Click **Download Export File**
   - Save as `wordpress-export.xml` in this directory

## Step 2: Run the Converter (Automatic!)

```bash
cd 05_shop/markets2mountains
python convert_wordpress_xml.py wordpress-export.xml
```

**What it does automatically:**
- ✅ Parses all your blog posts
- ✅ Downloads all images from your live site
- ✅ Converts HTML to markdown
- ✅ Creates proper Hugo frontmatter (title, date, tags)
- ✅ Updates image paths to `/images/...`
- ✅ Extracts featured images
- ✅ Preserves categories and tags

**Time:** 5-10 minutes depending on number of posts/images

## Step 3: Review and Test

1. **Check the output:**
   ```bash
   ls content/posts/          # See all converted posts
   ls static/images/          # See downloaded images
   ```

2. **Preview the site:**
   - Already running at http://localhost:56062/
   - Refresh your browser to see new posts

3. **Review a few posts:**
   - Check formatting looks good
   - Verify images display correctly
   - Check tags/categories

## Step 4: Clean Up (Optional)

Delete the test posts:
```bash
rm content/posts/test-with-image.md
```

---

## What the Converter Handles

**Content conversion:**
- HTML → Markdown
- Headings, bold, italic, links
- Lists, code blocks, blockquotes
- Images (downloads + updates paths)
- WordPress shortcodes (removes)

**Frontmatter:**
```yaml
---
title: "Your Post Title"
date: 2019-04-08
tags: ["gtm", "sales"]
categories: ["Business"]
featuredImage: "/images/hero.jpg"  # Auto-extracted
---
```

**Known limitations:**
- Complex embedded content may need manual review
- Custom WordPress plugins output might need tweaking
- Very old HTML might need cleanup

---

## Troubleshooting

**If converter fails:**
1. Check XML file exists: `ls wordpress-export.xml`
2. Check Python packages: `pip install requests`
3. Run with error details: `python convert_wordpress_xml.py wordpress-export.xml`

**If images don't download:**
- They'll keep original URLs (still work)
- Manually download from WordPress Media Library
- Copy to `static/images/`

**If formatting is off:**
- Edit the markdown file directly
- Markdown is just text - easy to fix
- Ask me for help with specific issues

---

## After Migration

1. **Update your About page** with a photo
2. **Add featured images** to posts that don't have them
3. **Review categories/tags** - consolidate if needed
4. **Test everything** thoroughly
5. **Set up GitHub Pages** when ready

---

## Commands Reference

```bash
# Convert WordPress export
python convert_wordpress_xml.py wordpress-export.xml

# Preview site
hugo server -D

# Build for production (later)
hugo

# Stop server
Ctrl+C
```

---

That's it! The converter does all the heavy lifting. You just export from WordPress and run one command.
