# sphinx-nekochan

A Sphinx extension for adding the **Nekochan(cat) emoji** to documents.

See [the sphinx-nekochan documantation](https://sphinx-nekochan.readthedocs.io/) for more details.

## Installation

You can install `sphinx-nekochan` with `pip`:

```
pip install sphinx-nekochan
```

## Enable extension

In your `conf.py` configuration file, add `sphinx_nekochan` to your extensions list:

```python
extensions = [
    ...
    "sphinx_nekochan",
    ...
]
```

## Use `nekochan` role

When you use the `nekochan` roll, you will see any nekochan emoji.

* markdown

```markdown
Welcome to nekochan emoji {nekochan}`banzai` world!!

* Enjoy nekochan emoji {nekochan}`choo-choo-train`
* I love {nekochan}`beer`
```

* reStructuredText

```rst
Welcome to nekochan emoji :nekochan:`banzai` world!!

* Enjoy nekochan emoji :nekochan:`choo-choo-train`
* I love :nekochan:`beer`
```

![nekochan emoji with text](https://raw.githubusercontent.com/takanory/sphinx-nekochan/main/nekochan-emoji-with-text.gif)

## Customize emoji height and alt text

You can specify height and alt text with a semicolon(`;`) after the name of the `nekochan` role.

* markdown

```markdown
* Big bear nekochan {nekochan}`kuma-nya;2em`
* Huge hot-sprint nekochan {nekochan}`hot-spring;128px`
* Customize alt text for emoji {nekochan}`gohan-taberu;3em;Nekochan eating rice ball`
```

* reStructuredText

```rst
* Big bear nekochan :nekochan:`kuma-nya;2em`
* Huge hot-sprint nekochan :nekochan:`hot-spring;128px`
* Customize alt text for emoji :nekochan:`gohan-taberu;3em;Nekochan eating rice ball`
```

![customize emoji height and alt text](https://raw.githubusercontent.com/takanory/sphinx-nekochan/main/custom-height-alt.png)

## Transform emoji

Also, you can specify transform option with a semicolon(`;`) after the alt text of the `nekochan` role.

* markdown

```markdown
* Skip {nekochan}`skip-nya;2em` rotated 90 degrees clockwise {nekochan}`skip-nya;2em;;rotate-90`
* Flip the left and right side of the {nekochan}`yoshi;2em` Yoshi emoji {nekochan}`yoshi;2em;;flip-horizontal`
```

* reStructuredText

```rst
* Skip :nekochan:`skip-nya;2em` rotated 90 degrees clockwise :nekochan:`skip-nya;2em;;rotate-90`
* Flip the left and right side of the :nekochan:`yoshi;2em` Yoshi emoji :nekochan:`yoshi;2em;;flip-horizontal`
```

![Transform emoji](https://raw.githubusercontent.com/takanory/sphinx-nekochan/main/transform-emoji.png)

## License

* sphinx-nekochan is licensed under the MIT License.
* Please refer to the following guidelines for using Nekochan emojis.
  * [Guidelines for Using Cat Emojis](https://note.com/shikamatsu/n/n8818bb5ebea1#8b38f78f-1883-46c6-a596-63d9bf4c69da)
