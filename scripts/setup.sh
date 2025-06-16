#!/bin/bash

# 開発環境セットアップスクリプト
echo "🛠 Setting up development environment..."

# 仮想環境の確認と作成
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv .venv
fi

# 仮想環境の有効化
echo "🔄 Activating virtual environment..."
source .venv/bin/activate

# 依存関係のインストール
echo "📚 Installing dependencies..."
pip install -r requirements.txt

echo "✅ Development environment ready!"
echo "📍 To start development server, run:"
echo "  ./scripts/start.sh"
