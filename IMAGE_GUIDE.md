# Image Handling in Hugo

## Two Ways to Add Images

### Option 1: Static Images (Simplest)

Put images in `/static/images/` and reference them in posts:

```markdown
---
title: "My Post"
date: 2025-01-15
---

This is my post with an image.

![Alt text](/images/my-photo.jpg)
```

**Pros:** Simple, works everywhere
**Cons:** Images not co-located with posts

---

### Option 2: Page Bundles (Organized)

Create a folder for each post with images:

```
content/posts/
└── my-post/
    ├── index.md          ← Your post content
    ├── hero-image.jpg    ← Feature image
    └── diagram.png       ← Inline images
```

**In your markdown:**
```markdown
---
title: "My Post"
date: 2025-01-15
---

![Alt text](diagram.png)
```

**Pros:** Images organized with content
**Cons:** Slightly more complex structure

---

## Featured Images (Hero Images)

Congo theme supports featured images in the frontmatter:

```markdown
---
title: "My Post"
date: 2025-01-15
featuredImage: "/images/hero.jpg"  # Option 1: Static
# OR
featuredImage: "hero.jpg"          # Option 2: Page bundle
---

Your post content here...
```

The featured image appears at the top of the post and in post listings.

---

## Current Setup

**Directory structure:**
```
05_shop/markets2mountains/
├── static/
│   └── images/              ← Put your images here (Option 1)
└── content/
    └── posts/
        ├── my-post.md       ← Simple post without images
        └── my-post/         ← Post with images (Option 2)
            ├── index.md
            └── image.jpg
```

---

## Image Formats Supported

- `.jpg` / `.jpeg` - Photos
- `.png` - Graphics, screenshots
- `.gif` - Animations
- `.webp` - Modern format (best compression)
- `.svg` - Vector graphics

---

## Quick Workflow

**Adding images to a new post:**

1. **Static method** (recommended for now):
   ```bash
   # Copy image to static folder
   cp my-image.jpg 05_shop/markets2mountains/static/images/

   # Reference in post
   ![My Image](/images/my-image.jpg)
   ```

2. **Page bundle method** (for posts with multiple images):
   ```bash
   # Create post folder
   mkdir content/posts/my-post

   # Create post + add images
   # content/posts/my-post/index.md
   # content/posts/my-post/image1.jpg
   # content/posts/my-post/image2.jpg
   ```

---

## Congo Theme Image Features

- **Responsive images** - Auto-resize for mobile
- **Lazy loading** - Faster page loads
- **Lightbox** - Click to enlarge (optional)
- **Thumbnails** - Auto-generated for listings

---

## Next Steps

When migrating your remaining blog posts:
1. Copy images from WordPress to `/static/images/`
2. Update image paths in markdown
3. Add featured images in frontmatter

**Example migration:**
```markdown
# WordPress
![Alt](https://oldsite.com/wp-content/uploads/2024/photo.jpg)

# Hugo
![Alt](/images/photo.jpg)
```
