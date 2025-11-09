#!/usr/bin/env python3
"""
Scrape images from markets2mountains.com WordPress site
Downloads all images from blog posts to static/images/
"""

import os
import re
import requests
from urllib.parse import urljoin, urlparse
from pathlib import Path
import time

# Configuration
SITE_URL = "https://markets2mountains.com"
OUTPUT_DIR = Path("static/images")
POSTS_URL = f"{SITE_URL}/posts"

def get_all_post_urls():
    """Get all blog post URLs from the site"""
    print(f"Fetching post list from {SITE_URL}...")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # Try homepage first
        response = requests.get(SITE_URL, headers=headers, timeout=10)
        response.raise_for_status()

        # Find all post URLs - WordPress typically uses /year/month/day/slug or /slug
        post_pattern = r'href="(https://markets2mountains\.com/\d{4}/\d{2}/\d{2}/[^"]+)"'
        simple_pattern = r'href="(https://markets2mountains\.com/[^"/]+/?)"'

        post_urls = set()
        post_urls.update(re.findall(post_pattern, response.text))
        post_urls.update(re.findall(simple_pattern, response.text))

        # Filter out non-post pages
        excluded = ['/posts', '/about', '/contact', '/category', '/tag', '/page', '/wp-']
        post_urls = {url for url in post_urls if not any(ex in url.lower() for ex in excluded)}

        print(f"Found {len(post_urls)} potential blog posts")
        return list(post_urls)

    except Exception as e:
        print(f"Error fetching post list: {e}")
        return []

def get_images_from_post(post_url):
    """Extract all image URLs from a blog post"""
    print(f"  Scanning: {post_url}")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(post_url, headers=headers, timeout=10)
        response.raise_for_status()

        # Find all img tags and wp-content image URLs
        img_pattern = r'<img[^>]+src="([^"]+)"'
        wp_content_pattern = r'(https?://[^"\']+/wp-content/uploads/[^"\']+\.(jpg|jpeg|png|gif|webp))'

        images = set()
        images.update(re.findall(img_pattern, response.text))
        images.update([match[0] for match in re.findall(wp_content_pattern, response.text)])

        # Filter for actual image files
        image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
        images = {img for img in images if img.lower().endswith(image_extensions)}

        print(f"    Found {len(images)} images")
        return images

    except Exception as e:
        print(f"  Error scanning post: {e}")
        return set()

def download_image(image_url, output_dir):
    """Download a single image"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # Get filename from URL
        parsed = urlparse(image_url)
        filename = os.path.basename(parsed.path)

        # Clean filename
        filename = re.sub(r'[^\w\-.]', '_', filename)

        output_path = output_dir / filename

        # Skip if already exists
        if output_path.exists():
            print(f"    ✓ Already have: {filename}")
            return True

        # Download
        print(f"    ⬇ Downloading: {filename}")
        response = requests.get(image_url, headers=headers, timeout=30)
        response.raise_for_status()

        output_path.write_bytes(response.content)
        print(f"    ✓ Saved: {filename}")
        return True

    except Exception as e:
        print(f"    ✗ Failed to download {image_url}: {e}")
        return False

def main():
    """Main scraping function"""
    print("=" * 60)
    print("Markets2Mountains Image Scraper")
    print("=" * 60)
    print()

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR.absolute()}")
    print()

    # Get all post URLs
    post_urls = get_all_post_urls()

    if not post_urls:
        print("No posts found. Try running again or check the site manually.")
        return

    print()
    print(f"Scanning {len(post_urls)} posts for images...")
    print()

    # Collect all images
    all_images = set()
    for i, post_url in enumerate(post_urls, 1):
        print(f"[{i}/{len(post_urls)}] {post_url}")
        images = get_images_from_post(post_url)
        all_images.update(images)
        time.sleep(0.5)  # Be nice to the server

    print()
    print(f"Total unique images found: {len(all_images)}")
    print()

    # Download all images
    if all_images:
        print("Downloading images...")
        print()

        success_count = 0
        for i, image_url in enumerate(sorted(all_images), 1):
            print(f"[{i}/{len(all_images)}]")
            if download_image(image_url, OUTPUT_DIR):
                success_count += 1
            time.sleep(0.3)  # Be nice to the server

        print()
        print("=" * 60)
        print(f"Complete! Downloaded {success_count}/{len(all_images)} images")
        print(f"Saved to: {OUTPUT_DIR.absolute()}")
        print("=" * 60)
    else:
        print("No images found to download.")

if __name__ == "__main__":
    main()
