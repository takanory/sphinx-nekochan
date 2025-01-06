"""Sphinx nekochan emoji extension"""

__version__ = "0.1.0"

from functools import cache
from importlib import resources

import json
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxRole
from sphinx.util.typing import ExtensionMetadata

from .make_nekochan_json import NEKOCHAN_EMOJI_JSON


@cache
def get_nekochan_emoji_data() -> tuple[dict[str : dict[str:str]], dict[str:str]]:
    """create nekochan emoji dict from json

    nekochan_emoji = {
        "akeome-nya": {
            "aliases" ["akeome"],
            "base64": "R0lGODlhgACA...",
            "mimetype": "image/gif",
        },
        "ame-nya": {
            "aliases" ["ame", "rain"],
            "base64": "iVBORw0KGgo...",
            "mimetype": "image/png",
        },
        :
    }

    aliases = {
        "akeome-nya": "akeome-nya",
        "akeome": "akeome-nya",
        "ame-nya": "ame-nya",
        "ame": "ame-nya",
        "rain": "ame-nya",
    }
    """
    content = (
        resources.files(__name__)
        .joinpath("data")
        .joinpath(NEKOCHAN_EMOJI_JSON)
        .read_text()
    )
    nekochan_emoji = json.loads(content)

    aliases = {}
    for name, value in nekochan_emoji.items():
        aliases[name] = name
        for alias in value["aliases"]:
            aliases[alias] = name

    return nekochan_emoji, aliases


def get_nekochan_emoji(name: str, height: str = "1.0em") -> str:
    """Return nokochan emoji img tag"""
    nekochan_emoji, aliases = get_nekochan_emoji_data()

    original_name = aliases[name]
    data = nekochan_emoji[original_name]
    mime = data["mimetype"]
    b64 = data["base64"]
    style = f"height: {height}"
    return f'<img alt="{name}" style="{style}" src="data:{mime};base64,{b64}"/>'


class NekochanRole(SphinxRole):
    """Nekochan emoji role"""

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        try:
            img_tag = get_nekochan_emoji(self.text)
        except Exception as e:
            msg = self.inliner.reporter.error(
                f"Invalid nekochan emoji name: {e}",
                line=self.lineno,
            )
            prb = self.inliner.problematic(self.rawtext, self.rawtext, msg)
            return [prb], [msg]

        node = nodes.raw("", nodes.Text(img_tag), format="html")
        return [node], []


# TODO: add Nekochan Directive
# https://github.com/atsphinx/audioplayer/blob/main/src/atsphinx/audioplayer/__init__.py#L29

# TODO: add All nekochan directive
# https://github.com/executablebooks/sphinx-design/blob/main/sphinx_design/icons.py#L145


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_role("nekochan", NekochanRole())

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
