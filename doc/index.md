# Sphinx-nekochan {nekochan}`smile`

See <project:japanese.md>.
日本語の説明は <project:japanese.md> を参照してください。

```{todo}
About this extension
```

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
    'sphinx_copybutton'
    ...
]
```

### 3. Use nekochan role {nekochan}`clap-nya`

`````{tab-set}

````{tab-item} Markdown
```markdown
Welcome to nekochan emoji {nekochan}`banzai` world!!
```
````

````{tab-item} reStructuredText
```rst
Welcome to nekochan emoji :nekochan:`banzai` world!!
```
````

`````

Welcome to nekochan emoji {nekochan}`banzai` world!!

```{toctree}
:maxdepth: 1

nekochan_emojis
japanese
```
