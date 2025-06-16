#!/bin/bash

# Staticle Development Server (Flask + HTMX + TailwindCSS)
echo "🚀 Starting Staticle Development Server (Flask + HTMX)..."

# 仮想環境の確認
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

# 環境変数の設定（オプション）
export ENVIRONMENT="development"
export DEBUG="true"
export FLASK_DEBUG=1

# Flaskサーバーの起動
echo "🌟 Starting Flask server with HTMX support..."
echo "📍 Server will be available at: http://localhost:5001"
echo ""
echo "🎨 Features enabled:"
echo "  - HTMX for dynamic interactions"
echo "  - TailwindCSS for modern styling"
echo "  - Dark mode support"
echo "  - Real-time search"
echo "  - Progressive enhancement"
echo ""
echo "Press Ctrl+C to stop the server"

python app.py
