# Sphinx-nekochan {nekochan}`smile`

A Sphinx extension for adding the **Nekochan(cat) emoji** to documents.

```{hint}
See <project:japanese.md>.
日本語の説明は <project:japanese.md> を参照してください。
```

## Get Started {nekochan}`think-nya`

### 1. Installation {nekochan}`ok-nya`

```{warning}
Can't install using pip yet.
```

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

When you use the `nekochan` roll, you will see any nekochan emoji.

`````{tab-set}

````{tab-item} Markdown
```markdown
Welcome to nekochan emoji {nekochan}`banzai` world!!

* Enjoy nekochan emoji {nekochan}`ok`
* I love {nekochan}`beer`
```
````

````{tab-item} reStructuredText
```rst
Welcome to nekochan emoji :nekochan:`banzai` world!!

* Enjoy nekochan emoji :nekochan:`ok`
* I love :nekochan:`beer`
```
````

`````

Welcome to nekochan emoji {nekochan}`banzai` world!!

* Enjoy nekochan emoji {nekochan}`ok`
* I love {nekochan}`beer`

---

```{toctree}
:maxdepth: 1

nekochan_emojis
japanese
```
