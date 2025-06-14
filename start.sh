#!/bin/bash

# Staticle Development Server (FastAPI + HTMX + TailwindCSS)
echo "🚀 Starting Staticle Development Server (FastAPI + HTMX)..."

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

# FastAPIサーバーの起動
echo "🌟 Starting FastAPI server with HTMX support..."
echo "📍 Server will be available at: http://localhost:8000"
echo "📖 API documentation: http://localhost:8000/docs"
echo "🔧 Interactive API: http://localhost:8000/redoc"
echo ""
echo "🎨 Features enabled:"
echo "  - HTMX for dynamic interactions"
echo "  - TailwindCSS for modern styling"
echo "  - Dark mode support"
echo "  - Real-time search"
echo "  - Progressive enhancement"
echo ""
echo "Press Ctrl+C to stop the server"

uvicorn main:app --reload --host 0.0.0.0 --port 8000
