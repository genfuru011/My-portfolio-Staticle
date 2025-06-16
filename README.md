# Staticle - Modern Blog Platform

A modern, fast, and interactive blog platform built with **Flask**, **HTMX**, and **TailwindCSS**.

## 🚀 Features

- **Lightning Fast**: HTMX provides instant interactions without SPA complexity
- **Simple & Reliable**: Flask backend with proven stability
- **Beautiful Design**: TailwindCSS with dark mode support
- **Developer Friendly**: Simple Python with automatic reloading
- **Interactive**: Smooth filtering and dynamic content loading
- **SEO Friendly**: Server-side rendering with progressive enhancement

## 🛠 Tech Stack

### Frontend
- **HTMX** - Dynamic HTML interactions
- **TailwindCSS** - Utility-first CSS framework
- **Alpine.js** - Minimal JavaScript for interactivity

### Backend
- **Flask** - Simple and reliable Python web framework
- **Jinja2** - Template engine
- **Python-Frontmatter** - Markdown with metadata support

## 📁 Project Structure

```
staticle/
├── app.py                  # Flask application
├── blog_manager.py         # Blog content management
├── requirements.txt        # Python dependencies
├── Procfile               # Render deployment config
├── runtime.txt            # Python version specification
├── scripts/               # Build and development scripts
│   ├── start.sh          # Development server
│   ├── setup.sh          # Environment setup
│   ├── build.sh          # Production build
│   └── deploy-render.sh  # Render deployment
├── views/                 # Template files (formerly templates)
│   ├── base.html         # Base template
│   ├── index.html        # Homepage
│   ├── blog.html         # Blog listing
│   ├── blog_post.html    # Individual post
│   ├── portfolio.html    # Portfolio page
│   ├── 404.html          # Error page
│   └── components/       # Reusable components
├── assets/               # Static files (formerly static)
│   ├── css/             # Stylesheets
│   ├── js/              # JavaScript files
│   └── img/             # Images
└── content/             # Blog content
    └── posts/           # Markdown blog posts
├── app.py                  # Legacy Flask app (for migration)
├── blog_manager.py         # Blog content management
├── requirements.txt        # Python dependencies
├── start.sh               # Development server script
├── templates/
│   ├── base.html          # Base template with HTMX/TailwindCSS
│   ├── index_new.html     # Homepage
│   ├── blog_new.html      # Blog listing page
│   └── components/        # HTMX components
├── content/posts/         # Markdown blog posts
└── static/               # Static assets
```

## 🚀 Quick Start

### Development Setup

```bash
# Clone the repository
git clone <repository-url>
cd staticle

# Set up development environment
./scripts/setup.sh
```

### Development Server

```bash
# Start development server
./scripts/start.sh
```

Or manually:

```bash
# Activate virtual environment
source .venv/bin/activate

# Start Flask server
python app.py
```

### Production Build

```bash
# Validate build
./scripts/build.sh

# Deploy to Render
./scripts/deploy-render.sh
```

### Access Points

- **Main Site**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Interactive API**: http://localhost:8000/redoc

## 📝 Adding Content

Create markdown files in `content/posts/` with frontmatter:

```markdown
---
title: "Your Post Title"
date: 2025-01-15
category: "Technology"
tags: ["python", "web", "htmx"]
excerpt: "A brief description of your post"
---

# Your Post Content

Write your content in markdown here...
```

## 🎨 Architecture Highlights

### HTMX Integration
- Dynamic content loading without page refreshes
- Progressive enhancement approach
- Server-side rendering with client-side interactions

### FastAPI Benefits
- Automatic API documentation
- Type hints and validation
- High performance async support
- Easy testing and development

### TailwindCSS Design
- Utility-first CSS approach
- Responsive design out of the box
- Dark mode support
- Modern, clean aesthetics

## 🔄 Migration from Flask

This project supports gradual migration from Flask to FastAPI:

1. **Current**: Flask app in `app.py` (legacy)
2. **New**: FastAPI app in `main.py` (modern)
3. **Shared**: `blog_manager.py` works with both

## 📦 Deployment

### Vercel (Recommended)

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel --prod
```

### Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🔧 Development

### Adding New Features

1. **Backend**: Add routes in `main.py`
2. **Frontend**: Create HTMX components in `templates/components/`
3. **Styling**: Use TailwindCSS classes
4. **Content**: Add markdown files to `content/posts/`

### Testing

```bash
# Run FastAPI with auto-reload
uvicorn main:app --reload

# Test specific endpoints
curl http://localhost:8000/htmx/posts
```

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

Built with ❤️ using HTMX, FastAPI, and TailwindCSS.
