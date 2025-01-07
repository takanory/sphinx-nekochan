# Description in Japanese {nekochan}`youkoso`

Sphinx-nekochanはSphinxドキュメントの中に**ネコチャン絵文字**を挿入するための拡張機能です。

```{hint}
See <project:index.md> for description in English.
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

Sphinx中に以下のように記述すると、指定された文字列に対応したネコチャン絵文字が表示されます。

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

## ネコチャン絵文字について {nekochan}`wao-nya`

この拡張機能で使用しているネコチャン絵文字は、**しかまつ**さんが作成して配布しているものです。
作者のtakanoryはしかまつさんに許可をとり、絵文字の画像を拡張機能に同梱して使用させてもらっています（ありがとうございます{nekochan}`bow-nya`）。

オリジナルのネコチャン絵文字は以下のnoteで配布されています。
ぜひSlackやDiscordで活用してください。

* [SlackやDiscordで使えるネコチャン絵文字を配布しています♪｜しかまつ(ネコチャン絵文字職人)](https://note.com/shikamatsu/n/nd217dc0617db)

ネコチャン絵文字の利用については、以下の規約を確認してください。

* [ネコチャン絵文字の利用に関するおやくそくなど｜しかまつ(ネコチャン絵文字職人)](https://note.com/shikamatsu/n/n8818bb5ebea1)

また、LINEを使っている方はネコちゃん絵文字のスタンプがあります。
こちらもぜひご活用ください。

* [しかまつのLINE スタンプ・絵文字一覧 | LINE STORE](https://store.line.me/stickershop/author/3740572/ja)

## この拡張機能を作成した背景 {nekochan}`kossori`

作者のtakanoryは会社のSlackに導入されたネコチャン絵文字を気に入っており、ヘビーに使いつつ自分が運営しているコミュニティのSlackにも導入して布教していました{nekochan}`ouen-nya`。

ある日しかまつさんのX(Twitter)で、プレゼン資料にネコチャン絵文字を使っている例が紹介されていました{nekochan}`miru-nya`。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">おおーー👏ネコチャンがあしらわれて楽しそうな資料ですﾆｬ <a href="https://t.co/m4edm3Fr4Z">https://t.co/m4edm3Fr4Z</a></p>&mdash; しかまつ👓ネコチャン絵文字配布中 (@shi_ka_ma_tsu) <a href="https://twitter.com/shi_ka_ma_tsu/status/1865545312775073951?ref_src=twsrc%5Etfw">December 7, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 

「なるほど、その手があったか！！{nekochan}`naruhodo`」と思い、早速パク...リスペクトしようと思いました。
ただ、毎回発表スライドに画像をコピーして指定するのはダルいなと思いました{nekochan}`mu-nya`。

私はスライドの作成にSphinxの拡張機能、[sphinx-revealjs](https://sphinx-revealjs.readthedocs.io/en/stable/)を使用しています（過去の発表スライド→[slides.takanory.net](https://slides.takanory.net/)）。
また、スライド中に[Font Awesome](https://fontawesome.com/)のアイコンを表示するために、[Sphinx Design](https://sphinx-design.readthedocs.io/en/latest/badges_buttons.html#fontawesome-icons)という拡張機能を使用しています。

同じように、シンプルな文字列（この場合は`nekochan`ロールと絵文字の名前）でネコチャン絵文字をスライドに表示できるといいなと思い、初めてのSphinx拡張作成に挑戦しました{nekochan}`kitaeru`。

この拡張機能を使用して、日本中、世界中でネコチャン絵文字入りのドキュメント、スライドが作成されたらうれしいです{nekochan}`kitai`！！


