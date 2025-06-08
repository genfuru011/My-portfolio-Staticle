# Staticle - ポートフォリオ & ブログ

「AIとペン先から、未来のWebを紡ぐ。思考の跡が、デジタルの美を際立たせる。」

StaticleはRuby on Railsで構築された、シンプルで美しいポートフォリオ兼ブログサイトです。

## 機能

- **レスポンシブデザイン**: モバイルからデスクトップまで様々なデバイスに対応
- **ダークモード/ライトモード**: ユーザーの好みに合わせたテーマ切り替え
- **ブログ機能**: マークダウンでコンテンツを簡単に管理
  - カテゴリとタグによる記事の整理
  - 関連記事の表示
- **シンプルな管理**: 記事はマークダウンファイルとして`content/posts/`に配置するだけ

## 技術スタック

- **バックエンド**: Ruby on Rails 8.0
- **フロントエンド**: HTML, CSS, JavaScript
- **CSS フレームワーク**: [PicoCSS](https://picocss.com/)
- **マークダウン処理**: Redcarpet
- **フロントマター解析**: front_matter_parser
- **フォント**: Google Fonts (Inter, Lora, Noto Sans JP)

## プロジェクト構造

```
staticle/
├── app/
│   ├── controllers/         # Rails コントローラー
│   │   ├── pages_controller.rb    # ホームページ
│   │   └── blog_controller.rb     # ブログ機能
│   ├── services/           # サービスクラス
│   │   └── blog_manager.rb        # ブログ記事管理
│   ├── views/              # ERB テンプレート
│   │   ├── pages/          # ホームページビュー
│   │   └── blog/           # ブログビュー
│   └── assets/             # 静的アセット
├── content/                # コンテンツフォルダ
│   └── posts/              # マークダウン形式のブログ記事
├── config/                 # Rails設定
└── public/                 # 公開静的ファイル
```

## セットアップ方法

1. リポジトリをクローンする
   ```
   git clone <repository-url>
   cd staticle
   ```

2. Ruby 3.2.3以上がインストールされていることを確認する
   ```
   ruby --version
   ```

3. 依存パッケージをインストールする
   ```
   bundle install
   ```

4. アプリケーションを実行する
   ```
   rails server
   ```

5. ブラウザで `http://localhost:3000` にアクセスする

## ブログ記事の作成方法

1. `content/posts/` ディレクトリに `.md` 形式のマークダウンファイルを作成します
2. 記事のフロントマターに必要な情報を記載します：

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

- `app/assets/stylesheets/style.css` でスタイルをカスタマイズできます
- `app/views/` 内のERBファイルでレイアウトを変更できます
- `app/assets/javascripts/` 内のJavaScriptファイルで動的な機能を追加できます

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。

---

© 2025 Staticle
