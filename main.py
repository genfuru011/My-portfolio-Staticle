from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from blog_manager import BlogManager
import os

# FastAPIアプリケーションのインスタンス
app = FastAPI(title="Staticle Blog", description="Modern blog with HTMX")

# 静的ファイルのマウント
app.mount("/static", StaticFiles(directory="static"), name="static")

# テンプレートエンジンの設定
templates = Jinja2Templates(directory="templates")

# BlogManagerのインスタンス
posts_dir = os.path.join(os.path.dirname(__file__), 'content', 'posts')
blog_manager = BlogManager(posts_dir)

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """トップページを表示"""
    # ブログ統計を取得
    stats = blog_manager.get_post_stats()
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "stats": stats
    })

@app.get("/blog", response_class=HTMLResponse)
async def blog(request: Request, category: str = None, tag: str = None):
    """ブログページを表示"""
    if category:
        posts = blog_manager.get_posts_by_category(category)
    elif tag:
        posts = blog_manager.get_posts_by_tag(tag)
    else:
        posts = blog_manager.get_all_posts()
    
    categories = blog_manager.get_categories()
    tags = blog_manager.get_tags()
    
    return templates.TemplateResponse("blog.html", {
        "request": request,
        "posts": posts,
        "categories": categories,
        "tags": tags,
        "current_category": category,
        "current_tag": tag
    })

# HTMX専用エンドポイント
@app.get("/htmx/posts", response_class=HTMLResponse)
async def htmx_posts(request: Request, category: str = None, tag: str = None, limit: int = None):
    """HTMX用のブログ投稿一覧"""
    if category:
        posts = blog_manager.get_posts_by_category(category)
    elif tag:
        posts = blog_manager.get_posts_by_tag(tag)
    else:
        posts = blog_manager.get_all_posts()
    
    # limitが指定されている場合は制限
    if limit:
        posts = posts[:limit]
    
    return templates.TemplateResponse("components/post-list.html", {
        "request": request,
        "posts": posts
    })

@app.get("/htmx/search", response_class=HTMLResponse)
async def htmx_search(request: Request, q: str = ""):
    """HTMX用の検索機能"""
    posts = blog_manager.search_posts(q) if q else []
    
    return templates.TemplateResponse("components/post-list.html", {
        "request": request,
        "posts": posts
    })

@app.get("/blog/{slug}", response_class=HTMLResponse)
async def blog_post(request: Request, slug: str):
    """個別ブログ投稿を表示"""
    post = blog_manager.get_post_by_slug(slug)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    related_posts = blog_manager.get_related_posts(post)
    
    return templates.TemplateResponse("blog_post.html", {
        "request": request,
        "post": post,
        "related_posts": related_posts
    })

@app.exception_handler(404)
async def custom_404_handler(request: Request, exc):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
