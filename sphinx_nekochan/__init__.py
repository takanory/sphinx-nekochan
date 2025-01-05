"""Sphinx nekochan emoji extension"""

__version__ = "0.1.0"

from functools import cache
from importlib import resources
from pathlib import Path

import json
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxRole
from sphinx.util.typing import ExtensionMetadata

from . import data
from .data.make_nekochan_json import ALIASES_JSON, NEKOCHAN_EMOJI_JSON


@cache
def get_aliases_data() -> dict[str: str]:
    """make alias to emoji name convert dict from json

    aliases = {
        "akeome-nya": "akeome-nya",
        "akeome": "akeome-nya",
        :
    }
    """
    breakpoint()
    aliases = {}

    content = resources.read_text(data, ALIASES_JSON, encoding="utf-8")
    aliases_dict = json.loads(content)

    for name, alias_list in aliases_dict.items():
        aliases[name] = name
        for alias in alias_list:
            aliases[alias] = name

    return aliases


@cache
def get_nekochan_emoji_data() -> dict[str: dict[str: str]]:
    """create nekochan emoji dict from json

    nekochan_emoji = {
        "akeome-nya": {
            "base64": "R0lGODlhgACA...",
            "mimetype": "image/gif",
        },
        "ame-nya": {
            "base64": "iVBORw0KGgo...",
            "mimetype": "image/png",
        },
        :
    }
    """
    content = resources.read_text(data, NEKOCHAN_EMOJI_JSON, encoding="utf-8")
    nekochan_emoji = json.loads(content)
    return nekochan_emoji


def get_nekochan_emoji(name: str) -> str:
    """Return nokochan emoji img tag"""
    aliases = get_aliases_data()
    nekochan_emoji = get_nekochan_emoji_data()

    name = aliases[name]
    data = nekochan_emoji[name]
    mime = data["mimetype"]
    b64 = data["base64"]
    return f'<img height="1em" alt="{name}" src="data:{mime};base64,{b64}"/>'


class NekochanRole(SphinxRole):
    """Nekochan emoji role"""

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        img_tag = get_nekochan_emoji(self.text)
        node = nodes.raw("", nodes.Text(img_tag), format="html")
        return [node], []


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_role("nekochan", NekochanRole())

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
