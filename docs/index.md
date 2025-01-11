# sphinx-nekochan {nekochan}`smile`

A Sphinx extension for adding the **Nekochan(cat) emoji** to documents.

````{only} builder_html
```{hint}
See <project:japanese.md>.
日本語の説明は <project:japanese.md> を参照してください。
```

``` {hint}
[**Sample slide**](https://sphinx-nekochan.readthedocs.io/slides/) with Nekochan emoji (using [sphinx-revealjs](https://sphinx-revealjs.readthedocs.io/)).
```
````

## Get Started {nekochan}`think-nya`

### 1. Installation {nekochan}`ok-nya`

You can install `sphinx-nekochan` with `pip`:


```
pip install sphinx-nekochan
```

### 2. Enable extension {nekochan}`good-nya`

In your `conf.py` configuration file, add `sphinx_nekochan` to your extensions list:

```python
extensions = [
    ...
    "sphinx_nekochan",
    ...
]
```

### 3. Use `nekochan` role {nekochan}`clap-nya`

When you use the `nekochan` roll, you will see any Nekochan emoji.

````{tab-set-code}
```{literalinclude} ./snippets/simple.md
:language: markdown
```
```{literalinclude} ./snippets/simple.rst
:language: rst
```
````

```{revealjs-break}
```

```{include} ./snippets/simple.md
```


### 4. Customize emoji height and alt text  {nekochan}`memo-nya`

You can specify height and alt text with a semicolon(`;`) after the name of the `nekochan` role.

````{tab-set-code}
```{literalinclude} ./snippets/with-height-alt.md
:language: markdown
```
```{literalinclude} ./snippets/with-height-alt.rst
:language: rst
```
````

```{revealjs-break}
```

```{include} ./snippets/with-height-alt.md
```

## License {nekochan}`ok2`

* sphinx-nekochan is licensed under the MIT License.
* Please refer to the following guidelines for using Nekochan emojis.
  * [Guidelines for Using Cat Emojis](https://note.com/shikamatsu/n/n8818bb5ebea1#8b38f78f-1883-46c6-a596-63d9bf4c69da)

## Enjoy!! {nekochan}`choo-choo-train`

* {fas}`globe` [sphinx-nekochan.readthedocs.io](https://sphinx-nekochan.readthedocs.io)
* {fab}`github` [takanory/sphinx-nekochan](https://github.com/takanory/sphinx-nekochan)
* {fab}`python` [pypi.org/project/sphinx-nekochan](https://pypi.org/project/sphinx-nekochan/)

## Table of Contents {nekochan}`tunda`

```{toctree}
:maxdepth: 1

nekochan_emojis
about
background
japanese
```
