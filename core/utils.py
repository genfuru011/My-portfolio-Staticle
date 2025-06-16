"""
ユーティリティ関数モジュール

共通で使用される便利な関数を提供
"""

import re
import datetime
from typing import List, Dict, Any
from markupsafe import Markup

def slugify(text: str) -> str:
    """テキストをスラッグに変換"""
    # 英数字以外を'-'に置換
    text = re.sub(r'[^\w\s-]', '', text.lower())
    # 空白を'-'に置換
    text = re.sub(r'[-\s]+', '-', text)
    # 先頭と末尾の'-'を削除
    return text.strip('-')

def truncate_text(text: str, length: int = 150, suffix: str = '...') -> str:
    """テキストを指定された長さで切り詰める"""
    if len(text) <= length:
        return text
    return text[:length].rsplit(' ', 1)[0] + suffix

def format_date(date: datetime.datetime, format_str: str = '%Y年%m月%d日') -> str:
    """日付をフォーマット"""
    if isinstance(date, str):
        try:
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return date
    return date.strftime(format_str)

def reading_time(content: str, words_per_minute: int = 200) -> int:
    """読了時間を計算（分）"""
    # HTMLタグを除去
    text = re.sub(r'<[^>]+>', '', content)
    word_count = len(text.split())
    return max(1, round(word_count / words_per_minute))

def generate_toc(content: str) -> List[Dict[str, Any]]:
    """見出しから目次を生成"""
    toc = []
    heading_pattern = re.compile(r'<h([1-6])(?:[^>]*)>(.*?)</h[1-6]>', re.IGNORECASE)
    
    for match in heading_pattern.finditer(content):
        level = int(match.group(1))
        title = re.sub(r'<[^>]+>', '', match.group(2))  # HTMLタグを除去
        anchor = slugify(title)
        
        toc.append({
            'level': level,
            'title': title,
            'anchor': anchor
        })
    
    return toc

def highlight_search_terms(text: str, query: str) -> str:
    """検索語をハイライト"""
    if not query:
        return text
    
    pattern = re.compile(re.escape(query), re.IGNORECASE)
    highlighted = pattern.sub(f'<mark class="bg-yellow-200 dark:bg-yellow-600">\\g<0></mark>', text)
    return Markup(highlighted)

def get_file_extension(filename: str) -> str:
    """ファイル拡張子を取得"""
    return os.path.splitext(filename)[1].lower()

def is_image_file(filename: str) -> bool:
    """画像ファイルかどうかチェック"""
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg'}
    return get_file_extension(filename) in image_extensions

def sanitize_filename(filename: str) -> str:
    """ファイル名をサニタイズ"""
    # 危険な文字を除去
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    # 連続するドットを削除
    filename = re.sub(r'\.{2,}', '.', filename)
    return filename.strip()

class PaginationHelper:
    """ページネーション支援クラス"""
    
    def __init__(self, total_items: int, page: int = 1, per_page: int = 10):
        self.total_items = total_items
        self.page = max(1, page)
        self.per_page = per_page
        self.total_pages = max(1, (total_items + per_page - 1) // per_page)
        
        if self.page > self.total_pages:
            self.page = self.total_pages
    
    @property
    def has_prev(self) -> bool:
        return self.page > 1
    
    @property
    def has_next(self) -> bool:
        return self.page < self.total_pages
    
    @property
    def prev_page(self) -> int:
        return self.page - 1 if self.has_prev else None
    
    @property
    def next_page(self) -> int:
        return self.page + 1 if self.has_next else None
    
    @property
    def start_index(self) -> int:
        return (self.page - 1) * self.per_page
    
    @property
    def end_index(self) -> int:
        return min(self.start_index + self.per_page, self.total_items)
    
    def get_page_range(self, window: int = 5) -> List[int]:
        """ページ番号のリストを取得"""
        start = max(1, self.page - window // 2)
        end = min(self.total_pages + 1, start + window)
        
        if end - start < window:
            start = max(1, end - window)
        
        return list(range(start, end))
