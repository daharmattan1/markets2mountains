# Blog Migration Guide

## Step 1: Scrape Images from WordPress

Run the image scraper to download all images from your live site:

```bash
cd 05_shop/markets2mountains
python scrape_images.py
```

**What it does:**
- Visits https://markets2mountains.com/posts
- Finds all blog post URLs
- Scans each post for images
- Downloads images to `static/images/`
- Skips images already downloaded

**Time:** ~5-10 minutes depending on number of images

---

## Step 2: Export Blog Posts from WordPress

Two options:

### Option A: WordPress Export (Recommended)
1. Log into WordPress admin
2. Go to **Tools → Export**
3. Select **Posts**
4. Click **Download Export File**
5. You get an XML file with all content

### Option B: Manual Export
Copy/paste your blog posts from the live site into markdown files.

---

## Step 3: Convert WordPress Export to Markdown

If you exported XML from WordPress, I can write a script to convert it:

```bash
python convert_wordpress_to_markdown.py wordpress-export.xml
```

This will:
- Parse the XML
- Create markdown files in `content/posts/`
- Add proper frontmatter (title, date, tags)
- Update image paths to `/images/...`
- Handle categories and tags

---

## Step 4: Manual Post Migration (Alternative)

If you prefer to do it manually:

**For each post:**

1. **Create markdown file:**
   ```bash
   # In content/posts/
   my-post-title.md
   ```

2. **Add frontmatter:**
   ```yaml
   ---
   title: "Post Title"
   date: 2019-04-08
   tags: ["tag1", "tag2"]
   featuredImage: "/images/hero.jpg"  # Optional
   ---
   ```

3. **Copy content** from WordPress

4. **Update image paths:**
   - Before: `![Alt](http://markets2mountains.com/wp-content/uploads/2024/01/image.jpg)`
   - After: `![Alt](/images/image.jpg)`

5. **Save and preview**

---

## Step 5: Verify Images Load

1. Start Hugo server: `hugo server -D`
2. Visit each post
3. Check images load correctly
4. Verify featured images appear

---

## Image Path Conversion Patterns

| WordPress | Hugo |
|-----------|------|
| `http://site.com/wp-content/uploads/2024/01/photo.jpg` | `/images/photo.jpg` |
| `../uploads/2024/photo.jpg` | `/images/photo.jpg` |
| Embedded base64 images | Save as file, reference normally |

---

## Next Steps After Migration

1. **Review all posts** - Check formatting
2. **Add featured images** - Make home page visual
3. **Update About page** - Add photo if you want
4. **Test thoroughly** - All links and images work
5. **Set up GitHub Pages** - Deploy to production

---

## Need Help?

If you hit any issues:
1. Check `scrape_images.py` output for errors
2. Manually download missing images from WordPress Media Library
3. Ask me to write a converter script for your WordPress XML export

The scraper handles most of the work. You'll mainly need to:
- Export posts from WordPress (5 minutes)
- Run conversion script (I'll write this if needed)
- Review and tweak formatting (30-60 minutes)

Total time: 1-2 hours for full migration.
