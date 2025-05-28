# Staticle - ポートフォリオ & ブログ

「AIとペン先から、未来のWebを紡ぐ。思考の跡が、デジタルの美を際立たせる。」

StaticleはFlaskで構築された、シンプルで美しいポートフォリオ兼ブログサイトです。

## 機能

- **レスポンシブデザイン**: モバイルからデスクトップまで様々なデバイスに対応
- **ダークモード/ライトモード**: ユーザーの好みに合わせたテーマ切り替え
- **ブログ機能**: マークダウンでコンテンツを簡単に管理
  - カテゴリとタグによる記事の整理
  - 関連記事の表示
- **シンプルな管理**: 記事はマークダウンファイルとして`content/posts/`に配置するだけ

## 技術スタック

- **バックエンド**: Python/Flask
- **フロントエンド**: HTML, CSS, JavaScript
- **CSS フレームワーク**: [PicoCSS](https://picocss.com/)
- **フォント**: Google Fonts (Inter, Lora, Noto Sans JP)

## プロジェクト構造

```
staticle/
├── app.py                 # メインアプリケーションファイル
├── blog_manager.py        # ブログ記事管理クラス
├── requirements.txt       # 依存パッケージリスト
├── content/               # コンテンツフォルダ
│   └── posts/             # マークダウン形式のブログ記事
├── static/                # 静的ファイル
│   ├── css/               # スタイルシート
│   ├── img/               # 画像ファイル
│   └── js/                # JavaScriptファイル
└── templates/             # HTMLテンプレート
    ├── 404.html           # 404エラーページ
    ├── blog_post.html     # 個別ブログ記事テンプレート
    ├── blog.html          # ブログ一覧ページ
    └── index.html         # トップページ
```

## セットアップ方法

1. リポジトリをクローンする
   ```
   git clone <repository-url>
   cd staticle
   ```

2. 仮想環境を作成して有効化する
   ```
   python -m venv venv
   source venv/bin/activate  # Windowsの場合: venv\Scripts\activate
   ```

3. 依存パッケージをインストールする
   ```
   pip install -r requirements.txt
   ```

4. アプリケーションを実行する
   ```
   python app.py
   ```

5. ブラウザで `http://localhost:5000` にアクセスする

## ブログ記事の作成方法

1. `content/posts/` ディレクトリに `.md` 形式のマークダウンファイルを作成します
2. 記事のフロントマターに必要な情報を記載します:

```markdown
---
title: 記事のタイトル
date: YYYY-MM-DD
category: カテゴリ名
tags: [タグ1, タグ2, タグ3]
excerpt: 記事の概要（省略可能）
---

ここから本文を記載します。マークダウン形式で記述できます。
```

## カスタマイズ

- `static/css/style.css` でスタイルをカスタマイズできます
- `templates/` 内のHTMLファイルでレイアウトを変更できます
- `static/js/` 内のJavaScriptファイルで動的な機能を追加できます

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

---

© 2025 Staticle
