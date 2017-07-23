"""
Get the image file.
"""
import os
import pathlib
import random

from .settings import __cache_dir__
from . import util
from . import wallpaper


def get_random_image(img_dir, cache_dir):
    """Pick a random image file from a directory."""
    current_wall = wallpaper.get()
    current_wall = os.path.basename(current_wall[0])

    file_types = (".png", ".jpg", ".jpeg", ".jpe", ".gif")
    images = [img for img in os.scandir(img_dir)
              if img.name.endswith(file_types) and img.name != current_wall]

    if not images:
        print("image: No new images found (nothing to do), exiting...")
        quit(1)

    return str(img_dir / random.choice(images).name)


def get(img, cache_dir=__cache_dir__):
    """Validate image input."""
    image = pathlib.Path(img)

    if image.is_file():
        wal_img = str(image)

    elif image.is_dir():
        wal_img = get_random_image(image, cache_dir)

    else:
        print("error: No valid image file found.")
        exit(1)

    # Cache the image file path.
    util.save_file(wal_img, cache_dir / "wal")

    print("image: Using image", wal_img)
    return wal_img
