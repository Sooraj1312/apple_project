"""
Apple Store Project - Product Seed Data & Script for Django

Matches Model:
    category: ForeignKey to Category
    name: CharField(max_length=255)
    description: TextField
    image: ImageField(upload_to='products/', blank=True, null=True)
    specifications: TextField(blank=True, null=True)
    price: DecimalField(max_digits=10, decimal_places=2)
    is_active: BooleanField(default=True)
"""

import os
from decimal import Decimal
import urllib.request
from django.core.files.base import ContentFile

# Sample structured Apple catalog data
PRODUCTS_DATA = [
    # ------------------ iPHONE ------------------
    {
        "category": "iPhone",
        "name": "iPhone 16 Pro",
        "price": Decimal("119900.00"),
        "description": "Built for Apple Intelligence with the all-new A18 Pro chip, Grade 5 titanium design, and camera control for instant photo and 4K 120 fps Dolby Vision video capture.",
        "specifications": (
            "- Display: 6.3-inch Super Retina XDR with ProMotion (up to 120Hz)\n"
            "- Processor: Apple A18 Pro chip with 6-core GPU\n"
            "- Storage: 128GB / 256GB / 512GB / 1TB\n"
            "- Camera: 48MP Fusion + 48MP Ultra Wide + 12MP 5x Telephoto\n"
            "- Build: Grade 5 Titanium with Ceramic Shield front\n"
            "- Battery Life: Up to 27 hours video playback\n"
            "- Connector: USB-C (USB 3 speeds up to 10Gb/s)"
        ),
        "image_url": "https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/121031-iphone-16-pro.png",
        "image_filename": "iphone-16-pro.png",
        "is_active": True,
    },
    {
        "category": "iPhone",
        "name": "iPhone 16",
        "price": Decimal("79900.00"),
        "description": "Featuring the fast A18 chip, Camera Control, 48MP Fusion camera with 2x optical-quality Telephoto, and durable color-infused back glass.",
        "specifications": (
            "- Display: 6.1-inch Super Retina XDR display\n"
            "- Processor: Apple A18 chip with 5-core GPU\n"
            "- Storage: 128GB / 256GB / 512GB\n"
            "- Camera: 48MP Fusion camera + 12MP Ultra Wide with Macro\n"
            "- Action Button: Customizable shortcut key\n"
            "- Battery Life: Up to 22 hours video playback\n"
            "- Connector: USB-C"
        ),
        "image_url": "https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/iphone-16.png",
        "image_filename": "iphone-16.png",
        "is_active": True,
    },
    {
        "category": "iPhone",
        "name": "iPhone 16 Pro Max",
        "price": Decimal("144900.00"),
        "description": "The ultimate iPhone with a massive 6.9-inch Super Retina XDR display, longest battery life ever in an iPhone, and A18 Pro power.",
        "specifications": (
            "- Display: 6.9-inch Super Retina XDR with ProMotion\n"
            "- Processor: Apple A18 Pro chip\n"
            "- Storage: 256GB / 512GB / 1TB\n"
            "- Camera: 48MP Fusion + 48MP Ultra Wide + 12MP 5x Telephoto\n"
            "- Battery Life: Up to 33 hours video playback\n"
            "- Build: Titanium frame with textured matte glass back"
        ),
        "image_url": "https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/121032-iphone-16-pro-max.png",
        "image_filename": "iphone-16-pro-max.png",
        "is_active": True,
    },

    # ------------------ MAC ------------------
    {
        "category": "Mac",
        "name": "MacBook Air 13-inch (M3)",
        "price": Decimal("114900.00"),
        "description": "Lean, mean, M3 machine. Incredibly thin and fast laptop with up to 18 hours of battery life and support for up to two external displays.",
        "specifications": (
            "- Display: 13.6-inch Liquid Retina display with True Tone\n"
            "- Processor: Apple M3 chip (8-core CPU, up to 10-core GPU)\n"
            "- Unified Memory: 8GB / 16GB / 24GB\n"
            "- Storage: 256GB / 512GB SSD\n"
            "- Ports: MagSafe 3 charging port, two Thunderbolt / USB 4 ports, 3.5mm headphone jack\n"
            "- Weight: 1.24 kg fanless silent design"
        ),
        "image_url": "https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/mba_13_m3_2024_hero.png",
        "image_filename": "macbook-air-13-m3.png",
        "is_active": True,
    },
    {
        "category": "Mac",
        "name": "MacBook Pro 14-inch (M3 Pro)",
        "price": Decimal("199900.00"),
        "description": "Pro-level performance in Space Black with extreme dynamic range Liquid Retina XDR display and comprehensive port connectivity.",
        "specifications": (
            "- Display: 14.2-inch Liquid Retina XDR (1000 nits sustained, 1600 nits peak HDR)\n"
            "- Processor: Apple M3 Pro chip (up to 12-core CPU, 18-core GPU)\n"
            "- Ports: HDMI, SDXC card slot, 3x Thunderbolt 4, MagSafe 3, headphone jack\n"
            "- Battery Life: Up to 18 hours\n"
            "- Audio: Six-speaker sound system with force-cancelling woofers"
        ),
        "image_url": "https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/macbook-pro-14-inch-m3-pro-or-m3.png",
        "image_filename": "macbook-pro-14-m3.png",
        "is_active": True,
    },

    # ------------------ iPAD ------------------
    {
        "category": "iPad",
        "name": "iPad Pro 11-inch (M4)",
        "price": Decimal("99900.00"),
        "description": "Ultra-thin design with groundbreaking Ultra Retina XDR tandem OLED display and next-generation Apple M4 performance.",
        "specifications": (
            "- Display: 11-inch Ultra Retina XDR Tandem OLED (ProMotion 10–120Hz)\n"
            "- Processor: Apple M4 chip with hardware-accelerated ray tracing\n"
            "- Thickness: Only 5.3 mm\n"
            "- Camera: 12MP Wide rear camera + Landscape 12MP Ultra Wide front camera with Center Stage\n"
            "- Accessories Supported: Apple Pencil Pro, Magic Keyboard for iPad Pro"
        ),
        "image_url": "https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/ipad-pro-11-inch-13-inch.png",
        "image_filename": "ipad-pro-m4.png",
        "is_active": True,
    },
    {
        "category": "iPad",
        "name": "iPad (10th Generation)",
        "price": Decimal("34900.00"),
        "description": "Colorfully reimagined all-screen iPad with 10.9-inch Liquid Retina display, A14 Bionic chip, and USB-C connectivity.",
        "specifications": (
            "- Display: 10.9-inch Liquid Retina display with True Tone\n"
            "- Processor: A14 Bionic chip with 16-core Neural Engine\n"
            "- Storage: 64GB / 256GB\n"
            "- Cameras: Landscape 12MP Ultra Wide front camera, 12MP Wide back camera\n"
            "- Authentication: Touch ID integrated into top button"
        ),
        "image_url": "https://cdsassets.apple.com/live/SZLF0YNV/images/sp/111840_sp884-ipad-10gen-960.png",
        "image_filename": "ipad-10th-gen.png",
        "is_active": True,
    },

    # ------------------ WATCH ------------------
    {
        "category": "Watch",
        "name": "Apple Watch Series 10",
        "price": Decimal("46900.00"),
        "description": "Thinnest Apple Watch ever with the biggest and most advanced wide-angle OLED display, faster charging, and sleep apnea notifications.",
        "specifications": (
            "- Case Sizes: 42mm or 46mm\n"
            "- Display: Wide-angle OLED display (up to 40% brighter off-axis)\n"
            "- Sensor: Electrical heart sensor (ECG), blood oxygen, depth gauge & water temperature\n"
            "- Charging: Fast charge to 80% in ~30 minutes\n"
            "- Water Resistance: 50m water resistant (swimproof)"
        ),
        "image_url": "https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/121202-apple-watch-series-10.png",
        "image_filename": "apple-watch-series-10.png",
        "is_active": True,
    },
    {
        "category": "Watch",
        "name": "Apple Watch Ultra 2",
        "price": Decimal("89900.00"),
        "description": "The ultimate sports and adventure watch in rugged corrosion-resistant titanium, with precision dual-frequency GPS and up to 72 hours of battery in Low Power Mode.",
        "specifications": (
            "- Case: 49mm aerospace-grade titanium case\n"
            "- Display: 3000 nits peak brightness sapphire crystal display\n"
            "- Battery Life: Up to 36 hours normal use / 72 hours low power mode\n"
            "- Water Resistance: 100m water resistant, certified EN13319 dive computer up to 40m\n"
            "- Action Button: Customizable high-contrast international orange button"
        ),
        "image_url": "https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/111832-watch-ultra-2.png",
        "image_filename": "apple-watch-ultra-2.png",
        "is_active": True,
    },

    # ------------------ AIRPODS ------------------
    {
        "category": "AirPods",
        "name": "AirPods Pro 2",
        "price": Decimal("24900.00"),
        "description": "Pro-level Active Noise Cancellation, Adaptive Audio, Transparency mode, and clinical-grade Hearing Aid feature with MagSafe Charging Case (USB-C).",
        "specifications": (
            "- Chip: Apple H2 headphone chip, U1/H2 in MagSafe case\n"
            "- Audio: 2x better Active Noise Cancellation + Adaptive EQ\n"
            "- Battery Life: Up to 6 hours listening with ANC on (up to 30 hours with case)\n"
            "- Case: Speaker, lanyard loop, Precision Finding, IP54 dust and water resistance"
        ),
        "image_url": "https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/airpods-pro-2.png",
        "image_filename": "airpods-pro-2.png",
        "is_active": True,
    },

    # ------------------ ACCESSORIES ------------------
    {
        "category": "Accessories",
        "name": "Apple Pencil (USB-C)",
        "price": Decimal("7900.00"),
        "description": "Pixel-perfect precision, low latency, and tilt sensitivity. Pairs and charges via USB-C and attaches magnetically to iPad.",
        "specifications": (
            "- Compatibility: iPad Pro, iPad Air, iPad mini, and iPad (10th gen)\n"
            "- Connection: Bluetooth and sliding USB-C port for pairing/charging\n"
            "- Features: Tilt sensitivity, magnetic attachment, Apple Pencil hover on iPad Pro"
        ),
        "image_url": "https://cdsassets.apple.com/live/7WUAS350/images/tech-specs/ipad-apple-pencil-witb-202310.png",
        "image_filename": "apple-pencil-usbc.png",
        "is_active": True,
    },
]


def seed_database(auto_download_images=False):
    """
    Run this function in Django Shell or as a management command:
    python manage.py shell
    >>> from seed_apple_products import seed_database
    >>> seed_database(auto_download_images=False)  # or True to fetch files automatically
    """
    # Import your models here
    try:
        from categories.models import Category
        # Replace 'products.models' with your actual product app name if different
        from products.models import Product
    except ImportError as e:
        print(f"Import error: {e}. Adjust the model import statements to match your app structure.")
        return

    print("Starting database seeding...")

    for item in PRODUCTS_DATA:
        # 1. Get or create category
        cat_obj, created_cat = Category.objects.get_or_create(name=item["category"])
        if created_cat:
            print(f"Created category: {cat_obj.name}")

        # 2. Get or create product
        prod, created_prod = Product.objects.get_or_create(
            name=item["name"],
            category=cat_obj,
            defaults={
                "description": item["description"],
                "specifications": item["specifications"],
                "price": item["price"],
                "is_active": item["is_active"],
            }
        )

        # 3. Optionally download and attach image automatically
        if auto_download_images and item.get("image_url") and not prod.image:
            try:
                print(f"Downloading image for {prod.name}...")
                req = urllib.request.Request(
                    item["image_url"],
                    headers={"User-Agent": "Mozilla/5.0"}
                )
                with urllib.request.urlopen(req) as resp:
                    image_bytes = resp.read()
                    prod.image.save(item["image_filename"], ContentFile(image_bytes), save=True)
                    print(f"  Attached image: {item['image_filename']}")
            except Exception as err:
                print(f"  Could not download image: {err}")

        action = "Created" if created_prod else "Already exists"
        print(f"{action}: {prod.name} - ₹{prod.price}")

    print("Seeding completed successfully!")


if __name__ == "__main__":
    # If run standalone inside Django environment
    import django
    if not os.environ.get("DJANGO_SETTINGS_MODULE"):
        print("Note: Set DJANGO_SETTINGS_MODULE and call django.setup() to run directly.")
    else:
        django.setup()
        seed_database(auto_download_images=False)