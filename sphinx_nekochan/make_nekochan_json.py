"""make nekochan emoji json file"""

import base64
import json
import unicodedata
import sys
from collections import Counter
from pathlib import Path
from zipfile import ZipFile

URL = "https://note.com/shikamatsu/n/nd217dc0617db"

DATADIR = "data"
ZIPFILE = "neco202408.zip"
ALIASES_JSON = "aliases.json"
NEKOCHAN_EMOJI_JSON = "nekochan_emoji.json"

MIME_TYPES = {
    "png": "image/png",
    "gif": "image/gif",
}


def update_aliases_json(name_dict: dict[str, str]) -> dict[str : list[str]]:
    """create or update nekochan emoji aliases

    aliases = {
        "akeome-nya": ["akeome"],
        "ame-nya": ["ame"],
        "amefoot-nya": ["amefoot", "american-football"],
        :
    }
    """
    aliases = {}
    p = Path(DATADIR) / ALIASES_JSON
    if p.exists():
        aliases = json.loads(p.read_text())
    for name in name_dict.keys():
        if name not in aliases:
            if name.endswith("-nya"):
                aliases[name] = [name.removesuffix("-nya")]
            else:
                aliases[name] = []

    # dupulicate check
    counter = Counter()
    for name, alias_list in aliases.items():
        counter.update([name])
        counter.update(alias_list)
    dupulicates = [(k, v) for k, v in counter.items() if v > 1]
    if dupulicates:
        for name, count in dupulicates:
            print(f"Duplicate: {name}, {count}")

    with p.open(mode="w", encoding="utf-8") as f:
        json.dump(aliases, f, ensure_ascii=False, indent=2, sort_keys=True)

    return aliases


def make_json_files(zip: Path) -> None:
    """make json files for aliases and emoji base64 data"""
    with ZipFile(zip, metadata_encoding="utf-8") as zip:
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
        aliases = update_aliases_json(name_dict)

        # create nekochan emoji json
        nekochan_emoji = {}
        for name in name_dict.keys():
            filename = name_dict[name]
            image_data = zip.read(filename)
            b64 = base64.b64encode(image_data).decode("utf-8")
            nekochan_emoji[name] = {
                "aliases": aliases.get(name, []),
                "mimetype": MIME_TYPES[filename[-3:]],
                "base64": b64,
            }

        p = Path(DATADIR) / NEKOCHAN_EMOJI_JSON
        with p.open(mode="w", encoding="utf-8") as f:
            json.dump(nekochan_emoji, f, ensure_ascii=False, indent=2, sort_keys=True)


def main():
    zip = Path(DATADIR) / ZIPFILE
    if not zip.exists():
        print(f"Please download {ZIPFILE} from {URL}.")
        sys.exit()

    # make aliases.json and nekochan_emoji.json
    make_json_files(zip)


if __name__ == "__main__":
    main()
