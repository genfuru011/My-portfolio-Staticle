"""
設定管理モジュール

アプリケーションの設定を一元管理
"""

import os
from typing import Dict, Any

class Config:
    """アプリケーション設定クラス"""
    
    # 基本設定
    DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # サーバー設定
    HOST = os.environ.get('HOST', '0.0.0.0')
    PORT = int(os.environ.get('PORT', 5001))
    
    # ブログ設定
    BLOG_TITLE = os.environ.get('BLOG_TITLE', 'Staticle')
    BLOG_DESCRIPTION = os.environ.get('BLOG_DESCRIPTION', 'Modern Blog with HTMX and Flask')
    BLOG_AUTHOR = os.environ.get('BLOG_AUTHOR', 'Anonymous')
    
    # ディレクトリ設定
    CONTENT_DIR = 'content'
    POSTS_DIR = 'content/posts'
    VIEWS_DIR = 'views'
    ASSETS_DIR = 'assets'
    
    # ページネーション設定
    POSTS_PER_PAGE = int(os.environ.get('POSTS_PER_PAGE', 10))
    
    # SEO設定
    SITE_URL = os.environ.get('SITE_URL', 'http://localhost:5001')
    
    @classmethod
    def get_config(cls) -> Dict[str, Any]:
        """設定辞書を返す"""
        return {
            'debug': cls.DEBUG,
            'secret_key': cls.SECRET_KEY,
            'host': cls.HOST,
            'port': cls.PORT,
            'blog_title': cls.BLOG_TITLE,
            'blog_description': cls.BLOG_DESCRIPTION,
            'blog_author': cls.BLOG_AUTHOR,
            'content_dir': cls.CONTENT_DIR,
            'posts_dir': cls.POSTS_DIR,
            'views_dir': cls.VIEWS_DIR,
            'assets_dir': cls.ASSETS_DIR,
            'posts_per_page': cls.POSTS_PER_PAGE,
            'site_url': cls.SITE_URL,
        }
