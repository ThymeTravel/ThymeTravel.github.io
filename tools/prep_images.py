#!/usr/bin/env python3
"""Prep photos for the web: fix rotation, resize, recompress, and STRIP ALL METADATA
(including GPS location from phone photos).

Usage:
    python3 tools/prep_images.py <input_dir> <output_dir> [max_px=1600]

Example (overwrites the 01-12 placeholders in order of input filename):
    python3 tools/prep_images.py ~/Pictures/portfolio images/photography

Needs Pillow:  pip install pillow
iPhone HEIC files: export as JPG first (Photos > File > Export), or install pillow-heif.
"""
import sys
from pathlib import Path
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit(__doc__)

src = Path(sys.argv[1]).expanduser()
dst = Path(sys.argv[2]).expanduser()
max_px = int(sys.argv[3]) if len(sys.argv) > 3 else 1600
dst.mkdir(parents=True, exist_ok=True)

files = sorted(p for p in src.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png"})
if not files:
    sys.exit(f"No jpg/png files found in {src}")

for i, p in enumerate(files, 1):
    im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
    im.thumbnail((max_px, max_px))
    out = dst / f"{i:02d}.jpg"
    # Not passing exif= means no metadata is written.
    im.save(out, "JPEG", quality=82, optimize=True, progressive=True)
    print(f"{p.name} -> {out}  {im.size[0]}x{im.size[1]}  {out.stat().st_size // 1024} KB")
