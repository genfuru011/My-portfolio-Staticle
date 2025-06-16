from flask import Flask, render_template, request, abort
from blog_manager import BlogManager
import os

# Flaskアプリケーションの初期化 - カスタムフォルダ名を指定
app = Flask(__name__,
            template_folder='views',  # templatesの代わりにviewsを使用
            static_folder='assets')   # staticの代わりにassetsを使用

# BlogManagerのインスタンスを作成
posts_dir = os.path.join(os.path.dirname(__file__), 'content', 'posts')
blog_manager = BlogManager(posts_dir)

@app.route('/')
def index():
    """トップページを表示"""
    # ブログ統計を取得
    stats = blog_manager.get_post_stats()
    
    return render_template('index.html', stats=stats)

@app.route('/blog')
def blog():
    """ブログページを表示"""
    category = request.args.get('category')
    tag = request.args.get('tag')
    
    if category:
        posts = blog_manager.get_posts_by_category(category)
    elif tag:
        posts = blog_manager.get_posts_by_tag(tag)
    else:
        posts = blog_manager.get_all_posts()
    
    categories = blog_manager.get_categories()
    tags = blog_manager.get_tags()
    
    return render_template(
        'blog.html',
        posts=posts,
        categories=categories,
        tags=tags,
        current_category=category,
        current_tag=tag
    )

@app.route('/portfolio')
def portfolio():
    """ポートフォリオページを表示"""
    return render_template('portfolio.html')

# HTMX専用エンドポイント
@app.route('/htmx/posts')
def htmx_posts():
    """HTMX用のブログ投稿一覧"""
    category = request.args.get('category')
    tag = request.args.get('tag')
    limit = request.args.get('limit', type=int)
    
    if category:
        posts = blog_manager.get_posts_by_category(category)
    elif tag:
        posts = blog_manager.get_posts_by_tag(tag)
    else:
        posts = blog_manager.get_all_posts()
    
    # limitが指定されている場合は制限
    if limit:
        posts = posts[:limit]
    
    return render_template('components/post-list.html', posts=posts)

@app.route('/htmx/search')
def htmx_search():
    """HTMX用の検索機能"""
    q = request.args.get('q', '')
    posts = blog_manager.search_posts(q) if q else []
    
    return render_template('components/post-list.html', posts=posts)

@app.route('/blog/<slug>')
def blog_post(slug):
    """個別ブログ投稿を表示"""
    post = blog_manager.get_post_by_slug(slug)
    if not post:
        abort(404)
    
    related_posts = blog_manager.get_related_posts(post)
    
    return render_template('blog_post.html', post=post, related_posts=related_posts)

# 従来のルートも維持（後方互換性）
@app.route('/blog/category/<category>')
def blog_category(category):
    """特定カテゴリのブログ記事を表示"""
    posts = blog_manager.get_posts_by_category(category)
    categories = blog_manager.get_categories()
    tags = blog_manager.get_tags()

    return render_template(
        'blog.html',
        posts=posts,
        categories=categories,
        tags=tags,
        current_category=category,
        current_tag=None
    )

@app.route('/blog/tag/<tag>')
def blog_tag(tag):
    """特定タグのブログ記事を表示"""
    posts = blog_manager.get_posts_by_tag(tag)
    categories = blog_manager.get_categories()
    tags = blog_manager.get_tags()

    return render_template(
        'blog.html',
        posts=posts,
        categories=categories,
        tags=tags,
        current_category=None,
        current_tag=tag
    )

@app.errorhandler(404)
def page_not_found(e):
    """404エラーページを表示"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    # 開発サーバーをデバッグモードで起動
    app.run(debug=True, host='0.0.0.0', port=5001)
