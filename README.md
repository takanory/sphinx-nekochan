# sphinx-nekochan

[![PyPI][pypi-badge]][pypi-link]
[![Python versions][versions-badge]][pypi-link]
[![GitHub Actions][github-ci-badge]][github-ci-link]
[![Documentation status][rtd-badge]][rtd-link]
[![PyPI - Download][downloads-badge]][downloads-link]
[![License][license-badge]][license-link]

[pypi-badge]: https://img.shields.io/pypi/v/sphinx-nekochan.svg
[pypi-link]: https://pypi.org/project/sphinx-nekochan/
[versions-badge]: https://img.shields.io/pypi/pyversions/sphinx-nekochan.svg
[github-ci-badge]: https://github.com/takanory/sphinx-nekochan/actions/workflows/workflow.yml/badge.svg
[github-ci-link]: https://github.com/takanory/sphinx-nekochan/actions
[rtd-badge]: https://readthedocs.org/projects/sphinx-nekochan/badge/?version=latest
[rtd-link]: https://sphinx-nekochan.readthedocs.io/
[downloads-badge]: https://img.shields.io/pypi/dm/sphinx-nekochan.svg
[downloads-link]: https://pypistats.org/packages/sphinx-nekochan
[license-badge]: https://img.shields.io/pypi/l/sphinx-nekochan.svg
[license-link]: https://github.com/takanory/sphinx-nekochan/blob/main/LICENSE

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

## Use `nekochan` role or directive

When you use the `nekochan` roll or directive, you will see any nekochan emoji.

* markdown

````markdown
Welcome to nekochan emoji {nekochan}`banzai` world!!

* Enjoy nekochan emoji {nekochan}`choo-choo-train`
* I love {nekochan}`beer`

```{nekochan} melty
```
````

* reStructuredText

```rst
Welcome to nekochan emoji :nekochan:`banzai` world!!

* Enjoy nekochan emoji :nekochan:`choo-choo-train`
* I love :nekochan:`beer`

.. nekochan:: melty
```

![nekochan emoji with text](https://raw.githubusercontent.com/takanory/sphinx-nekochan/main/nekochan-emoji-with-text.gif)

## Customize emoji height and alt text

You can specify height and alt text with a semicolon(`;`) after the name of the `nekochan` role.

* markdown

````markdown
* Big bear nekochan {nekochan}`kuma-nya;2em`
* Huge hot-sprint nekochan {nekochan}`hot-spring;128px`
* Customize alt text for emoji {nekochan}`gohan-taberu;3em;Nekochan eating rice ball`


```{nekochan} lgtm
:alt: Looks Good To Me
:height: 3em
```
````

* reStructuredText

```rst
* Big bear nekochan :nekochan:`kuma-nya;2em`
* Huge hot-sprint nekochan :nekochan:`hot-spring;128px`
* Customize alt text for emoji :nekochan:`gohan-taberu;3em;Nekochan eating rice ball`


.. nekochan:: lgtm
   :alt: Looks Good To Me
   :height: 3em
```

![customize emoji height and alt text](https://raw.githubusercontent.com/takanory/sphinx-nekochan/main/custom-height-alt.png)

## Transform emoji

Also, you can specify transform option with a semicolon(`;`) after the alt text of the `nekochan` role.

* markdown

````markdown
* Skip {nekochan}`skip-nya;2em` rotated 90 degrees clockwise {nekochan}`skip-nya;2em;;rotate-90`
* Flip the left and right side of the {nekochan}`yoshi;2em` Yoshi emoji {nekochan}`yoshi;2em;;flip-horizontal`

```{nekochan} snake
:transform: flip-vertical
:height: 2em
```
````

* reStructuredText

```rst
* Skip :nekochan:`skip-nya;2em` rotated 90 degrees clockwise :nekochan:`skip-nya;2em;;rotate-90`
* Flip the left and right side of the :nekochan:`yoshi;2em` Yoshi emoji :nekochan:`yoshi;2em;;flip-horizontal`

.. nekochan:: snake
   :transform: flip-vertical
   :height: 2em
```

![Transform emoji](https://raw.githubusercontent.com/takanory/sphinx-nekochan/main/transform-emoji.png)

## License

* sphinx-nekochan is licensed under the MIT License.
* Please refer to the following guidelines for using Nekochan emojis.
  * [Guidelines for Using Cat Emojis](https://note.com/shikamatsu/n/n8818bb5ebea1#8b38f78f-1883-46c6-a596-63d9bf4c69da)
