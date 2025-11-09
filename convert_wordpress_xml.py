#!/usr/bin/env python3
"""
Convert WordPress XML export to Hugo markdown files
Downloads images and updates paths automatically
"""

import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from datetime import datetime
import requests
from urllib.parse import urlparse
import html
import time

# Configuration
OUTPUT_DIR = Path("content/posts")
IMAGES_DIR = Path("static/images")

def clean_filename(title):
    """Convert title to clean filename"""
    # Remove special characters, convert to lowercase
    filename = re.sub(r'[^\w\s-]', '', title.lower())
    filename = re.sub(r'[-\s]+', '-', filename)
    return filename.strip('-')

def download_image(image_url):
    """Download image and return local path"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        parsed = urlparse(image_url)
        filename = os.path.basename(parsed.path)
        filename = re.sub(r'[^\w\-.]', '_', filename)

        output_path = IMAGES_DIR / filename

        if output_path.exists():
            print(f"      ✓ Already have: {filename}")
            return f"/images/{filename}"

        print(f"      ⬇ Downloading: {filename}")
        response = requests.get(image_url, headers=headers, timeout=30)
        response.raise_for_status()

        IMAGES_DIR.mkdir(parents=True, exist_ok=True)
        output_path.write_bytes(response.content)

        print(f"      ✓ Saved: {filename}")
        return f"/images/{filename}"

    except Exception as e:
        print(f"      ✗ Failed to download {image_url}: {e}")
        return image_url  # Keep original URL if download fails

def convert_content(content):
    """Convert WordPress content to Hugo-compatible markdown"""
    if not content:
        return ""

    # Decode HTML entities
    content = html.unescape(content)

    # Find and download all images
    img_pattern = r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>'
    images = re.findall(img_pattern, content)

    for img_url in images:
        if 'wp-content/uploads' in img_url or img_url.startswith('http'):
            local_path = download_image(img_url)
            # Replace image URL in content
            content = content.replace(img_url, local_path)

    # Convert WordPress image blocks to markdown
    # <img src="..." alt="...">  →  ![alt](src)
    def img_to_markdown(match):
        src = re.search(r'src=["\']([^"\']+)["\']', match.group(0))
        alt = re.search(r'alt=["\']([^"\']+)["\']', match.group(0))
        if src:
            alt_text = alt.group(1) if alt else ""
            return f"![{alt_text}]({src.group(1)})"
        return match.group(0)

    content = re.sub(r'<img[^>]+>', img_to_markdown, content)

    # Remove WordPress shortcodes
    content = re.sub(r'\[caption[^\]]*\](.*?)\[/caption\]', r'\1', content, flags=re.DOTALL)
    content = re.sub(r'\[/?[a-z_]+[^\]]*\]', '', content)

    # Convert basic HTML to markdown
    conversions = [
        (r'<h1>(.*?)</h1>', r'# \1'),
        (r'<h2>(.*?)</h2>', r'## \1'),
        (r'<h3>(.*?)</h3>', r'### \1'),
        (r'<h4>(.*?)</h4>', r'#### \1'),
        (r'<strong>(.*?)</strong>', r'**\1**'),
        (r'<b>(.*?)</b>', r'**\1**'),
        (r'<em>(.*?)</em>', r'*\1*'),
        (r'<i>(.*?)</i>', r'*\1*'),
        (r'<code>(.*?)</code>', r'`\1`'),
        (r'<a href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', r'[\2](\1)'),
        (r'<p>', '\n'),
        (r'</p>', '\n'),
        (r'<br\s*/?>', '\n'),
        (r'</?div[^>]*>', ''),
        (r'</?span[^>]*>', ''),
        (r'&nbsp;', ' '),
        (r'&amp;', '&'),
        (r'&lt;', '<'),
        (r'&gt;', '>'),
        (r'&quot;', '"'),
    ]

    for pattern, replacement in conversions:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL | re.IGNORECASE)

    # Clean up multiple newlines
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content.strip()

def extract_featured_image(content):
    """Try to extract first image as featured image"""
    img_match = re.search(r'!\[[^\]]*\]\(([^)]+)\)', content)
    if img_match:
        return img_match.group(1)
    return None

def parse_wordpress_xml(xml_file):
    """Parse WordPress XML and extract posts"""
    print(f"Parsing WordPress XML: {xml_file}")
    print()

    tree = ET.parse(xml_file)
    root = tree.getroot()

    # WordPress namespace
    namespaces = {
        'wp': 'http://wordpress.org/export/1.2/',
        'content': 'http://purl.org/rss/1.0/modules/content/',
        'excerpt': 'http://wordpress.org/export/1.2/excerpt/',
        'dc': 'http://purl.org/dc/elements/1.1/'
    }

    posts = []
    items = root.findall('.//item')

    print(f"Found {len(items)} items in XML")
    print()

    for item in items:
        # Only process published posts
        post_type = item.find('wp:post_type', namespaces)
        status = item.find('wp:status', namespaces)

        if post_type is not None and post_type.text == 'post' and status is not None and status.text == 'publish':
            title = item.find('title').text or "Untitled"
            date_elem = item.find('wp:post_date', namespaces)
            content_elem = item.find('content:encoded', namespaces)
            excerpt_elem = item.find('excerpt:encoded', namespaces)

            # Extract categories/tags
            categories = []
            tags = []
            for cat in item.findall('category'):
                domain = cat.get('domain')
                term = cat.text
                if term:
                    if domain == 'category':
                        categories.append(term)
                    elif domain == 'post_tag':
                        tags.append(term)

            post = {
                'title': title,
                'date': date_elem.text if date_elem is not None else None,
                'content': content_elem.text if content_elem is not None else "",
                'excerpt': excerpt_elem.text if excerpt_elem is not None else "",
                'categories': categories,
                'tags': tags
            }

            posts.append(post)

    print(f"Found {len(posts)} published blog posts")
    return posts

def create_hugo_post(post, output_dir):
    """Create Hugo markdown file from post"""
    title = post['title']
    filename = clean_filename(title)

    print(f"  Converting: {title}")

    # Parse date
    date_str = post['date'][:10] if post['date'] else datetime.now().strftime('%Y-%m-%d')

    # Convert content
    print(f"    Processing content...")
    content = convert_content(post['content'])

    # Extract featured image
    featured_image = extract_featured_image(content)

    # Create frontmatter
    frontmatter = f"""---
title: "{title}"
date: {date_str}
"""

    if post['tags']:
        tags_str = ', '.join(f'"{tag}"' for tag in post['tags'])
        frontmatter += f"tags: [{tags_str}]\n"

    if post['categories']:
        cats_str = ', '.join(f'"{cat}"' for cat in post['categories'])
        frontmatter += f"categories: [{cats_str}]\n"

    if featured_image:
        frontmatter += f'featuredImage: "{featured_image}"\n'

    frontmatter += "---\n\n"

    # Combine
    full_content = frontmatter + content

    # Write file
    output_path = output_dir / f"{filename}.md"
    output_path.write_text(full_content, encoding='utf-8')

    print(f"    ✓ Created: {output_path.name}")
    return output_path

def main():
    import sys

    if len(sys.argv) < 2:
        print("Usage: python convert_wordpress_xml.py <wordpress-export.xml>")
        print()
        print("To export from WordPress:")
        print("  1. Log into WordPress admin")
        print("  2. Go to Tools → Export")
        print("  3. Select 'Posts'")
        print("  4. Download the XML file")
        print("  5. Run: python convert_wordpress_xml.py wordpress-export.xml")
        return

    xml_file = sys.argv[1]

    if not os.path.exists(xml_file):
        print(f"Error: File not found: {xml_file}")
        return

    print("=" * 60)
    print("WordPress to Hugo Converter")
    print("=" * 60)
    print()

    # Create output directories
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    # Parse WordPress XML
    posts = parse_wordpress_xml(xml_file)

    if not posts:
        print("No posts found in XML file.")
        return

    print()
    print("Converting posts to Hugo markdown...")
    print()

    # Convert each post
    converted = []
    for i, post in enumerate(posts, 1):
        print(f"[{i}/{len(posts)}]")
        try:
            output_path = create_hugo_post(post, OUTPUT_DIR)
            converted.append(output_path)
        except Exception as e:
            print(f"    ✗ Error: {e}")

        print()
        time.sleep(0.2)  # Be nice when downloading images

    print("=" * 60)
    print(f"Conversion complete!")
    print(f"Converted: {len(converted)}/{len(posts)} posts")
    print(f"Output: {OUTPUT_DIR.absolute()}")
    print(f"Images: {IMAGES_DIR.absolute()}")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Review the converted posts")
    print("  2. Run: hugo server -D")
    print("  3. Check that everything looks good")
    print("  4. Delete test posts if needed")

if __name__ == "__main__":
    main()
