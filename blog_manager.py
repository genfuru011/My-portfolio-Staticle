import os
import markdown
import frontmatter
import datetime
from flask import url_for

class BlogManager:
    """ブログ記事を管理するクラス"""

    def __init__(self, posts_dir):
        """
        初期化

        Args:
            posts_dir: マークダウンファイルが格納されているディレクトリのパス
        """
        self.posts_dir = posts_dir
        self.posts = []
        self.load_posts()

    def load_posts(self):
        """マークダウンファイルを読み込んでpostリストに追加する"""
        self.posts = []

        # ディレクトリが存在しない場合は空リストを返す
        if not os.path.exists(self.posts_dir):
            return []

        # ディレクトリ内のマークダウンファイルを読み込む
        for filename in os.listdir(self.posts_dir):
            if filename.endswith('.md'):
                post_path = os.path.join(self.posts_dir, filename)
                post = self._parse_post(post_path, filename)
                if post:
                    self.posts.append(post)

        # 日付でソート（新しい順）
        self.posts.sort(key=lambda x: x.get('date', datetime.datetime.now()), reverse=True)
        return self.posts

    def _parse_post(self, post_path, filename):
        """マークダウンファイルをパースする"""
        try:
            with open(post_path, 'r', encoding='utf-8') as file:
                # frontmatterとmarkdownを解析
                post = frontmatter.load(file)

                # slugを生成（ファイル名からの自動生成）
                slug = os.path.splitext(filename)[0]

                # HTMLに変換
                html_content = markdown.markdown(
                    post.content,
                    extensions=['fenced_code', 'codehilite', 'tables', 'toc']
                )

                # 必要な情報を辞書に格納
                post_dict = {
                    'title': post.get('title', 'No Title'),
                    'date': post.get('date', datetime.datetime.now()),
                    'author': post.get('author', 'Anonymous'),
                    'category': post.get('category', ''),
                    'tags': post.get('tags', []),
                    'excerpt': post.get('excerpt', ''),
                    'content': html_content,
                    'slug': slug,
                    'url': f'/blog/{slug}'
                }

                # 日付が文字列の場合はdatetimeオブジェクトに変換
                if isinstance(post_dict['date'], str):
                    try:
                        post_dict['date'] = datetime.datetime.strptime(post_dict['date'], '%Y-%m-%d')
                    except ValueError:
                        post_dict['date'] = datetime.datetime.now()

                # フォーマット済みの日付文字列を追加
                post_dict['formatted_date'] = post_dict['date'].strftime('%Y年%m月%d日')

                return post_dict

        except Exception as e:
            logging.error(f"Error parsing {filename}: {str(e)}")
            return None

    def get_all_posts(self):
        """すべての投稿を取得"""
        return self.posts

    def get_post_by_slug(self, slug):
        """特定のスラッグを持つ投稿を取得"""
        for post in self.posts:
            if post['slug'] == slug:
                return post
        return None

    def get_posts_by_category(self, category):
        """特定のカテゴリの投稿を取得"""
        return [post for post in self.posts if post['category'].lower() == category.lower()]

    def get_posts_by_tag(self, tag):
        """特定のタグを持つ投稿を取得"""
        return [post for post in self.posts if tag.lower() in [t.lower() for t in post['tags']]]

    def get_categories(self):
        """すべてのカテゴリを取得"""
        categories = {}
        for post in self.posts:
            category = post.get('category', '').lower()
            if category:
                categories[category] = categories.get(category, 0) + 1
        return categories

    def get_tags(self):
        """すべてのタグを取得"""
        tags = {}
        for post in self.posts:
            for tag in post.get('tags', []):
                tag = tag.lower()
                tags[tag] = tags.get(tag, 0) + 1
        return tags

    def get_related_posts(self, post, max_posts=3):
        """関連記事を取得する

        Args:
            post: 対象となる記事
            max_posts: 取得する関連記事の最大数

        Returns:
            関連性スコアの高い順に並べられた記事のリスト
        """
        if not post:
            return []

        # 現在の記事のカテゴリとタグ
        current_category = post.get('category', '').lower()
        current_tags = [tag.lower() for tag in post.get('tags', [])]
        current_slug = post.get('slug', '')

        # 関連スコアを計算
        related_posts = []
        for other_post in self.posts:
            # 同じ記事はスキップ
            if other_post.get('slug') == current_slug:
                continue

            score = 0

            # 同じカテゴリなら+5点
            if other_post.get('category', '').lower() == current_category:
                score += 5

            # 共通するタグがあれば1つにつき+3点
            other_tags = [tag.lower() for tag in other_post.get('tags', [])]
            for tag in current_tags:
                if tag in other_tags:
                    score += 3

            # スコアが0より大きい場合のみ追加
            if score > 0:
                related_posts.append({
                    'post': other_post,
                    'score': score
                })

        # スコア順にソート
        related_posts.sort(key=lambda x: x['score'], reverse=True)

        # 必要な数だけ取得
        return [item['post'] for item in related_posts[:max_posts]]
