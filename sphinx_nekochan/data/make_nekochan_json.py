"""make nekochan emoji json file"""

import base64
import json
import unicodedata
import sys
from pathlib import Path
from zipfile import ZipFile

URL = "https://note.com/shikamatsu/n/nd217dc0617db"
ZIPFILE = "neco202408.zip"

ALIASES_JSON = "aliases.json"
NEKOCHAN_EMOJI_JSON = "nekochan_emoji.json"

# Nekochan emoji list markdown file
MD = "../../doc/nekochan_emojis.md"

MIME_TYPES = {
    "png": "image/png",
    "gif": "image/gif",
}


def update_aliases_json(name_dict: dict[str, str]):
    """create or update nekochan emoji aliases"""
    aliases = {}
    p = Path(ALIASES_JSON)
    if p.exists():
        try:
            aliases = json.loads(p.read_text())
        except json.decoder.JSONDecodeError:
            pass
    for name in name_dict.keys():
        if name not in aliases:
            if name.endswith("-nya"):
                aliases[name] = [name.removesuffix("-nya")]
            else:
                aliases[name] = []
    with p.open(mode="w", encoding="utf-8") as f:
        json.dump(aliases, f, ensure_ascii=False, indent=2, sort_keys=True)


def make_json_files():
    """make json files for aliases and emoji base64 data"""
    with ZipFile(ZIPFILE, metadata_encoding="utf-8") as zip:
        # key: neko-chan emoji name
        # value: path in zipfile
        name_dict = {}
        for name in sorted(zip.namelist()):
            # ignore file for mac
            if name.startswith("__MACOSX"):
                continue
            if not name.endswith((".png", ".gif")):
                continue
            basename = name.split("/")[-1]
            basename = basename.removesuffix(".png").removesuffix(".gif")
            # normalize basename
            basename = unicodedata.normalize("NFKC", basename)
            name_dict[basename] = name

        # create or update nekochan emoji aliases
        update_aliases_json(name_dict)

        # create nekochan emoji json
        nekochan_emoji = {}
        for name in name_dict.keys():
            filename = name_dict[name]
            image_data = zip.read(filename)
            encoded = base64.b64encode(image_data).decode("utf-8")
            nekochan_emoji[name] = {
                "mimetype": MIME_TYPES[filename[-3:]],
                "base64": encoded,
            }

        with open(NEKOCHAN_EMOJI_JSON, mode="w", encoding="utf-8") as f:
            json.dump(nekochan_emoji, f, ensure_ascii=False, indent=2, sort_keys=True)


def make_markdown():
    """make markdown file for nekochan emoji list"""

    # load data from json
    with open(ALIASES_JSON, encoding="utf-8") as f:
        aliases = json.load(f)
    with open(NEKOCHAN_EMOJI_JSON, encoding="utf-8") as f:
        nekochan_emoji = json.load(f)

    with open(MD, "w", encoding="utf-8") as f:
        f.write("# Nekochan emoji list\n\n")
        first_char = ""
        for name, data in nekochan_emoji.items():
            if name[0] != first_char:
                first_char = name[0]
                f.write(f"## {first_char.upper()}\n\n")
                f.write("| name | aliases | image |\n")
                f.write("| -- | -- | -- |\n")

            alias = ", ".join(f"`{a}`" for a in aliases[name])

            mime = data["mimetype"]
            b64 = data["base64"]
            img = f'<img src="data:{mime};base64,{b64}"/>'
            f.write(f"| `{name}` |  {alias} | {img} |\n")


def main():
    p = Path(ZIPFILE)
    if not p.exists():
        print(f"Please download {ZIPFILE} from {URL}.")
        sys.exit()

    # make aliases.json and nekochan_emoji.json
    make_json_files()

    # make markdown for document
    make_markdown()


if __name__ == "__main__":
    main()
