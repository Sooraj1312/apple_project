"""
Apple Store Project - Banner Seed Data & Script for Django

Matches Model:
class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)
    link = models.URLField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
"""

import os
import urllib.request
from django.core.files.base import ContentFile

BANNERS_DATA = [
    {
        "title": "iPhone 16 Pro",
        "content": "Hello, Apple Intelligence. Built with Grade 5 Titanium, the powerful A18 Pro chip, and pro camera control.",
        "link": "/store/",
        "image_url": "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/iphone-16-finish-select-202409-6-1inch_GEO_IN_FMT_WHH?wid=1280&hei=492&fmt=p-jpg&qlt=80",
        "image_filename": "banner-iphone-16-pro.jpg",
        "is_active": True,
    },
    {
        "title": "MacBook Air M3",
        "content": "Lean. Mean. M3 machine. Strikingly thin design with up to 18 hours of all-day battery life.",
        "link": "/store/",
        "image_url": "https://www.apple.com/v/macbook-air/z/images/overview/hero/hero_static__c9sislzzicq6_large.png",
        "image_filename": "banner-macbook-air.png",
        "is_active": True,
    },
    {
        "title": "iPad Pro M4",
        "content": "Thinpossible. The thinnest Apple product ever, featuring the breakthrough Ultra Retina XDR OLED display.",
        "link": "/store/",
        "image_url": "https://www.apple.com/v/ipad-air/ah/images/overview/hero/hero_endframe__6gl84bccyaqi_large.png",
        "image_filename": "banner-ipad-pro.png",
        "is_active": True,
    },
    {
        "title": "Apple Watch Series 10",
        "content": "Thinscredible. Our thinnest smartwatch ever with the largest wide-angle OLED display and fast charging.",
        "link": "/store/",
        "image_url": "https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/121202-apple-watch-series-10.png",
        "image_filename": "banner-apple-watch-10.png",
        "is_active": True,
    },
    {
        "title": "AirPods Pro 2",
        "content": "Pro-level Active Noise Cancellation, Adaptive Audio, and clinical-grade Hearing Aid capabilities.",
        "link": "/store/",
        "image_url": "https://www.apple.com/v/homepage/images/airpods-5/a/promo_airpods_5_preorder__lydvte0llb6i_large.jpg",
        "image_filename": "banner-airpods-pro.jpg",
        "is_active": True,
    },
]


def seed_banners(auto_download_images=True):
    """
    Run this function in Django Shell:
    python manage.py shell
    >>> from seed_banners import seed_banners
    >>> seed_banners(auto_download_images=True)
    """
    try:
        # If your Banner model is in a different app (e.g. 'store.models' or 'home.models'),
        # adjust this import accordingly:
        from banners.models import Banner
    except ImportError:
        try:
            from banners.models import Banner
        except ImportError:
            try:
                from products.models import Banner
            except ImportError:
                print("Could not automatically locate the Banner model.")
                print("Please edit the import statement in seed_banners.py to point to your app.")
                return

    print("Starting banner seeding...")

    for item in BANNERS_DATA:
        # Create or update banner by title
        banner_obj, created = Banner.objects.get_or_create(
            title=item["title"],
            defaults={
                "content": item["content"],
                "link": item["link"],
                "is_active": item["is_active"],
            }
        )

        if auto_download_images and item.get("image_url") and not banner_obj.image:
            try:
                print(f"Downloading image for {banner_obj.title}...")
                req = urllib.request.Request(
                    item["image_url"],
                    headers={"User-Agent": "Mozilla/5.0"}
                )
                with urllib.request.urlopen(req) as resp:
                    image_bytes = resp.read()
                    banner_obj.image.save(item["image_filename"], ContentFile(image_bytes), save=True)
                    print(f"  Attached image: {item['image_filename']}")
            except Exception as err:
                print(f"  Could not download banner image: {err}")

        status = "Created" if created else "Already exists"
        print(f"{status}: {banner_obj.title}")

    print("Banner seeding completed successfully!")


if __name__ == "__main__":
    import django
    if not os.environ.get("DJANGO_SETTINGS_MODULE"):
        print("Set DJANGO_SETTINGS_MODULE to run directly.")
    else:
        django.setup()
        seed_banners(auto_download_images=True)