#!/bin/bash

# プロダクションビルド用スクリプト
echo "🏗 Building for production..."

# 依存関係の確認
echo "📚 Checking dependencies..."
pip check

# テンプレートとアセットの確認
echo "🔍 Validating templates and assets..."
if [ ! -d "views" ]; then
    echo "❌ Views directory not found!"
    exit 1
fi

if [ ! -d "assets" ]; then
    echo "❌ Assets directory not found!"
    exit 1
fi

# ブログコンテンツの確認
if [ ! -d "content/posts" ]; then
    echo "❌ Blog content directory not found!"
    exit 1
fi

echo "✅ Production build ready!"
echo "📍 Ready to deploy with: gunicorn app:app"
