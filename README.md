# sphinx-nekochan

A Sphinx extension for adding the **Nekochan(cat) emoji** to documents.

See [the sphinx-necochan documantation](https://sphinx-nekochan.readthedocs.io/) for more details.

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

![nekochan emoji with text](nekochan-emoji-with-text.gif)
