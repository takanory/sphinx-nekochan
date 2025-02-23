"""sphinx-nekochan emoji extension"""

__version__ = "0.2.0"

from functools import cache
from importlib import resources
from pathlib import Path

import json
from docutils import nodes
from sphinx.application import Sphinx
from sphinx.directives import SphinxDirective
from sphinx.util.docutils import SphinxRole
from sphinx.util.typing import ExtensionMetadata

NEKOCHAN_EMOJI_JSON = "nekochan_emoji.json"

TRANSFORMS = (
    "rotate-90",
    "rotate-180",
    "rotate-270",
    "flip-horizontal",
    "flip-vertical",
    "flip-both",
)


@cache
def get_nekochan_emoji_data() -> tuple[dict[str : dict[str:str]], dict[str:str]]:
    """create Nekochan emoji and aliases dict from json

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
        .read_text(encoding="utf-8")
    )
    nekochan_emoji = json.loads(content)

    aliases = {}
    for name, value in nekochan_emoji.items():
        aliases[name] = name
        for alias in value["aliases"]:
            aliases[alias] = name

    return nekochan_emoji, aliases


def create_nekochan_img_tag(
    name: str, height: str = "1em", alt: str = None, transform: str = None
) -> str:
    """Create Nekochan emoji img tag"""
    if alt is None or alt == "":
        alt = name

    nekochan_emoji, aliases = get_nekochan_emoji_data()

    original_name = aliases[name]
    data = nekochan_emoji[original_name]
    mime = data["mimetype"]
    b64 = data["base64"]
    style = f"height: {height}"

    class_ = "nekochan"
    if transform in TRANSFORMS:  # add transform style
        class_ = f"nekochan nekochan-{transform}"

    return f'<img alt="{alt}" class="{class_}" style="{style}" src="data:{mime};base64,{b64}"/>'


class NekochanRole(SphinxRole):
    """Role to display Nekochan emoji"""

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        """Run Nekochan role

        Additional height(ex: 2em, 128px) and alt text can be added to the
        element after a semicolon.

        * markdown: {nekochan}`ame-nya;2em;rain`
        * reST: :nekochan:`ame-nya;2em;rain`
        """
        try:
            match self.text.split(";", 3):
                case [name]:
                    img_tag = create_nekochan_img_tag(name)
                case [name, height]:
                    img_tag = create_nekochan_img_tag(name, height)
                case [name, height, alt]:
                    img_tag = create_nekochan_img_tag(name, height, alt)
                case [name, height, alt, transform]:
                    img_tag = create_nekochan_img_tag(name, height, alt, transform)
        except Exception as e:
            msg = self.inliner.reporter.error(
                f"Invalid nekochan emoji name: {e}",
                line=self.lineno,
            )
            prb = self.inliner.problematic(self.rawtext, self.rawtext, msg)
            return [prb], [msg]

        node = nodes.raw("", nodes.Text(img_tag), format="html")
        return [node], []


class AllNekochanDirective(SphinxDirective):
    """Directive to generate all Nekochan emoji list

    see: https://sphinx-nekochan.readthedocs.io/nekochan_emojis.html
    """

    def run(self) -> list[nodes.Node]:
        node_list = []

        nekochan_emoji, _ = get_nekochan_emoji_data()

        text = f"Number of Nekochan emojis: {len(nekochan_emoji)}"
        node_list.append(nodes.Text(text))

        first_char = ""
        for name, data in nekochan_emoji.items():
            if name[0] != first_char:
                first_char = name[0]
                # create section and title(H2)
                section = nodes.section(ids=[first_char])
                title = nodes.title(first_char.upper(), first_char.upper())
                section.append(title)
                node_list.append(section)

                # create table and header
                table, tgroup = self.create_table_header()
                tbody = nodes.tbody()
                tgroup += tbody
                node_list.append(table)
            # add row to table
            tbody += self.create_row(name, nekochan_emoji[name]["aliases"])

        return node_list

    def create_table_header(self) -> nodes.Node:
        """create table and table header node"""
        table = nodes.table()

        tgroup = nodes.tgroup(cols=3)
        table += tgroup
        tgroup.extend(
            (
                nodes.colspec(colwidth=1),
                nodes.colspec(colwidth=1),
                nodes.colspec(colwidth=1),
            )
        )

        thead = nodes.thead()
        row = nodes.row()
        thead += row
        cell = nodes.entry()
        row += cell
        cell += nodes.Text("Emoji", "Emoji")
        cell = nodes.entry()
        row += cell
        cell += nodes.Text("Name", "Name")
        cell = nodes.entry()
        row += cell
        cell += nodes.Text("Alias", "Alias")
        tgroup += thead

        return table, tgroup

    def create_row(self, name: str, aliases) -> nodes.Node:
        """create a row for a Nekochan emoji"""
        row = nodes.row()

        cell = nodes.entry()
        row += cell
        img_tag = create_nekochan_img_tag(name, height="64px")
        cell += nodes.raw("", nodes.Text(img_tag), format="html")
        cell = nodes.entry()
        row += cell
        cell += nodes.literal(name, name)
        cell = nodes.entry()
        row += cell
        for idx, alias in enumerate(aliases):
            if idx > 0:
                cell += nodes.Text(", ")
            cell += nodes.literal(alias, alias)

        return row


def setup(app: Sphinx) -> ExtensionMetadata:
    app.config.html_static_path.append(
        str(Path(__file__).parent.joinpath("_static").absolute())
    )
    app.add_css_file("sphinx_nekochan.css")
    app.add_role("nekochan", NekochanRole())
    app.add_directive("_all_nekochan", AllNekochanDirective)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
