# Description in Japanese {nekochan}`youkoso`

Sphinx-nekochanはSphinxドキュメントの中に**ネコチャン絵文字**を挿入するための拡張機能です。

```{hint}
See <project:index.md> for description in English.
```

```{todo}
ネコチャン絵文字についての説明を追加する

<https://note.com/shikamatsu>
```

## はじめかた {nekochan}`think-nya`

### 1. インストール {nekochan}`ok-nya`

```{warning}
まだpipインストールできません
```

`sphinx-nekochan`は`pip`コマンドでインストールできます。

```
pip install sphinx-nekochan
```

### 2. 拡張の有効化 {nekochan}`good-nya`

設定ファイル`conf.py`の拡張のリストに`sphinx_nekochan`を追加します。

```python
extensions = [
    ...
    "sphinx_nekochan",
    ...
]
```

### 3. `nekochan`ロール使用する {nekochan}`clap-nya`

Sphinx中に以下のように記述すると、指定された文字列に対応した絵文字が表示されます。

`````{tab-set}

````{tab-item} Markdown
```markdown
ネコチャン絵文字 {nekochan}`banzai` の世界へようこそ！！

* ネコチャン絵文字を楽しんでください {nekochan}`ok`
* 私は {nekochan}`beer` が好きです
```
````

````{tab-item} reStructuredText
```rst
ネコチャン絵文字 :nekochan:`banzai` の世界へようこそ！！

* ネコチャン絵文字を楽しんでください :nekochan:`ok`
* 私は :nekochan:`beer` が好きです
```
````

`````

ネコチャン絵文字 {nekochan}`banzai` の世界へようこそ！！

* ネコチャン絵文字を楽しんでください {nekochan}`ok`
* 私は {nekochan}`beer` が好きです
