import sys
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile

import vtracer
from PIL import Image

URL = "https://note.com/shikamatsu/n/nd217dc0617db"
ZIPFILE = "neco202408.zip"
OUTDIR = "out"


def png2svg(data: bytes, stem: str):
    """convert PNG to SVG"""
    img = Image.open(BytesIO(data))
    pixels = list(img.convert("RGBA").getdata())
    svg_str = vtracer.convert_pixels_to_svg(pixels, size=img.size)

    p = Path(OUTDIR) / f"{stem}.svg"
    p.write_text(svg_str)


def gif2svg(data: bytes, stem: str):
    """convert animated GIF to SVG"""
    img = Image.open(BytesIO(data))
    print(img.n_frames)
    for i in range(img.n_frames):
        img.seek(i)
        duration = img.info["duration"]
        print(duration)
        pixels = list(img.convert("RGBA").getdata())
        svg_str = vtracer.convert_pixels_to_svg(pixels, size=img.size)

        p = Path(OUTDIR) / f"{stem}-{i}.svg"
        p.write_text(svg_str)


def image2svg(name: str, data: bytes):
    """Convert image data to svg"""
    print(name)
    basename = name.split("/")[-1]
    p = Path(OUTDIR) / basename
    p.write_bytes(data)

    if p.suffix == ".png":
        png2svg(data, p.stem)
        pass
    elif p.suffix == ".gif":
        gif2svg(data, p.stem)
        pass


def main():
    p = Path(ZIPFILE)
    if not p.exists():
        print(f"Please download {ZIPFILE} from {URL}.")
        sys.exit()

    with ZipFile(ZIPFILE, metadata_encoding="utf-8") as zip:
        for name in zip.namelist()[:50]:
            # ignore file for mac
            if name.startswith("__MACOSX"):
                continue
            if name.endswith((".png", ".gif")):
                data = zip.read(name)
                image2svg(name, data)


if __name__ == "__main__":
    main()
