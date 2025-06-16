#!/bin/bash

# Render デプロイ用スクリプト
echo "🚀 Preparing for Render deployment..."

# 依存関係のインストール
echo "📚 Installing dependencies..."
pip install -r requirements.txt

echo "✅ Ready for Render deployment!"
echo "📍 Make sure to set up the following in Render:"
echo "  - Build Command: pip install -r requirements.txt"
echo "  - Start Command: gunicorn app:app"
echo "  - Environment: Python 3.11"
