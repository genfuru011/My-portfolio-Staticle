#!/bin/bash

# 型チェックスクリプト
# mypy を使ってプロジェクト全体の型チェックを実行

echo "🔍 Python 型チェックを実行中..."

# 仮想環境をアクティベート
source .venv/bin/activate

# メインファイルの型チェック
echo "📁 app.py をチェック中..."
mypy app.py

echo "📁 core/ ディレクトリをチェック中..."
mypy core/

echo "✅ 型チェック完了！"
