#!/usr/bin/env python3
"""Build a Vivaldi theme for every official Omarchy theme.

Each Omarchy theme ships a colors.toml and a folder of backgrounds. This packs
those into a theme archive Vivaldi can import (Settings > Themes > Import
Theme...), so the browser matches the desktop.

    python3 build.py                          # every theme in /usr/share/omarchy/themes
    python3 build.py --only nord tokyo-night  # just these
    python3 build.py --themes ~/omarchy/themes --out dist

Needs ImageMagick (`magick`) to scale the Start Page image.
"""

import argparse
import json
import os
import subprocess
import tempfile
import tomllib
import uuid
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))

# Theme IDs are derived from the theme name, so re-importing a rebuilt archive
# is recognisably the same theme.
ID_NAMESPACE = uuid.UUID("0a4c6172-6368-7900-8000-766976616c64")

# Start Page images are scaled down to this width: Omarchy's backgrounds run up
# to 6000px and 4 MB, which is a lot to carry in a browser theme.
IMAGE_WIDTH = 2560
IMAGE_QUALITY = 82

IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")

# Names that do not survive a plain title-case of the directory name.
TITLES = {
    "catppuccin-latte": "Catppuccin Latte",
    "osaka-jade": "Osaka Jade",
    "retro-82": "Retro-82",
}


def title_of(slug):
    return TITLES.get(slug, slug.replace("-", " ").title())


def first_background(theme_dir):
    bg_dir = os.path.join(theme_dir, "backgrounds")
    if not os.path.isdir(bg_dir):
        return None
    files = sorted(f for f in os.listdir(bg_dir) if f.lower().endswith(IMAGE_EXTENSIONS))
    return os.path.join(bg_dir, files[0]) if files else None


def scale(src, dst):
    subprocess.run(
        [
            "magick", src + "[0]",
            "-resize", f"{IMAGE_WIDTH}x>",
            "-strip",
            "-quality", str(IMAGE_QUALITY),
            dst,
        ],
        check=True,
    )


def settings_for(slug, c, has_image):
    """Map an Omarchy palette onto Vivaldi's theme fields."""
    title = title_of(slug)
    return {
        "accentFromPage": False,  # pages never tint the chrome
        "accentOnWindow": True,
        "accentSaturationLimit": 1,
        "alpha": 1,
        "backgroundImage": "background.webp" if has_image else "",
        "backgroundPosition": "stretch",
        "blur": 0,
        "colorAccentBg": c["dark_background"],  # tab bar: one step from the toolbars
        "colorBg": c["background"],  # toolbars, panels, address field
        "colorFg": c["foreground"],
        "colorHighlightBg": c["accent"],  # focus and selection
        "colorPosition": "unified",
        "colorWindowBg": c["dark_background"],
        "contrast": 0,  # higher draws light strokes around the chrome
        "dimBlurred": False,
        "engineVersion": 1,
        "id": str(uuid.uuid5(ID_NAMESPACE, slug)),
        "name": f"{title} (Omarchy)",
        "preferSystemAccent": False,
        "radius": 4,
        "simpleScrollbar": True,
        "transparencyTabBar": False,
        "transparencyTabs": False,
        "url": "",
        "version": 1,
    }


def build(slug, theme_dir, out):
    with open(os.path.join(theme_dir, "colors.toml"), "rb") as f:
        c = tomllib.load(f)
    image = first_background(theme_dir)
    settings = settings_for(slug, c, image is not None)

    with tempfile.TemporaryDirectory() as tmp, zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("settings.json", json.dumps(settings, indent=2) + "\n")
        if image:
            webp = os.path.join(tmp, "background.webp")
            scale(image, webp)
            z.write(webp, "background.webp")
    bg = os.path.basename(image) if image else "no background"
    print(f"  {os.path.basename(out):<28} {settings['name']:<28} {bg:<34} {os.path.getsize(out) // 1024} KB")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--themes", default="/usr/share/omarchy/themes", help="Omarchy themes directory")
    p.add_argument("--out", default=os.path.join(HERE, "themes"), help="output directory")
    p.add_argument("--only", nargs="*", help="build only these themes")
    args = p.parse_args()

    os.makedirs(args.out, exist_ok=True)
    for slug in sorted(os.listdir(args.themes)):
        theme_dir = os.path.join(args.themes, slug)
        if not os.path.isfile(os.path.join(theme_dir, "colors.toml")):
            continue
        if args.only and slug not in args.only:
            continue
        build(slug, theme_dir, os.path.join(args.out, slug + ".zip"))


if __name__ == "__main__":
    main()
