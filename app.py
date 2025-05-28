from flask import Flask, render_template, request
from blog_manager import BlogManager
import os

app = Flask(__name__)

# BlogManagerのインスタンスを作成
posts_dir = os.path.join(os.path.dirname(__file__), 'content', 'posts')
blog_manager = BlogManager(posts_dir)

@app.route('/')
def index():
    """トップページを表示します。"""
    return render_template('index.html')


@app.route('/blog')
def blog():
    """Blogページを表示します。"""
    # 全ての投稿、カテゴリ、タグ情報を取得
    posts = blog_manager.get_all_posts()
    categories = blog_manager.get_categories()
    tags = blog_manager.get_tags()

    # 現在選択されているカテゴリとタグの取得（デフォルトはNone）
    current_category = request.args.get('category')
    current_tag = request.args.get('tag')

    return render_template(
        'blog.html',
        posts=posts,
        categories=categories,
        tags=tags,
        current_category=current_category,
        current_tag=current_tag
    )


@app.route('/blog/category/<category>')
def blog_category(category):
    """特定カテゴリのブログ記事を表示します。"""
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
    """特定タグのブログ記事を表示します。"""
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


@app.route('/blog/<slug>')
def blog_post(slug):
    """個別のブログ記事を表示します。"""
    # 指定されたスラッグの投稿を取得
    post = blog_manager.get_post_by_slug(slug)

    # 投稿が見つからない場合は404エラー
    if not post:
        return page_not_found()

    # 関連記事を取得
    related_posts = blog_manager.get_related_posts(post)

    return render_template('blog_post.html', post=post, related_posts=related_posts)


@app.errorhandler(404)
def page_not_found(e=None):
    """404エラーページを表示します。"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    # 開発サーバーをデバッグモードで起動
    # ポート番号は必要に応じて変更してください (例: port=5001)
    app.run(debug=True, port=5000)
