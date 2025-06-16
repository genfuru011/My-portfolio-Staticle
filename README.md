# Staticle - Modern Blog Platform

A modern, lightweight, and interactive blog platform built with **Flask**, **HTMX**, and **TailwindCSS**. Optimized for easy deployment on **Render**.

## 🚀 Features

- **Lightning Fast**: HTMX provides instant interactions without SPA complexity
- **Simple & Reliable**: Flask backend with proven stability
- **Beautiful Design**: TailwindCSS with dark mode support
- **Developer Friendly**: Clean Python code with modular architecture
- **Interactive**: Smooth filtering and dynamic content loading
- **SEO Friendly**: Server-side rendering with progressive enhancement
- **Easy Deployment**: Ready for Render with one-click deployment

## 🛠 Tech Stack

### Frontend

- **HTMX** - Dynamic HTML interactions
- **TailwindCSS** - Utility-first CSS framework
- **Alpine.js** - Minimal JavaScript for interactivity

### Backend

- **Flask** - Simple and reliable Python web framework
- **Gunicorn** - Production WSGI server
- **Jinja2** - Template engine
- **Python-Frontmatter** - Markdown with metadata support

### Deployment

- **Render** - Cloud hosting platform
- **Gunicorn** - Production server

## 📁 Project Structure

```text
staticle/
├── app.py                  # Flask application (main entry point)
├── Procfile               # Render deployment config
├── runtime.txt            # Python version specification
├── requirements.txt        # Python dependencies
├── scripts/               # Build and development scripts
│   ├── start.sh          # Development server
│   ├── setup.sh          # Environment setup
│   ├── build.sh          # Production build
│   └── deploy-render.sh  # Render deployment
├── core/                  # Core application modules
│   ├── __init__.py       # Package initialization
│   ├── blog_manager.py   # Blog content management
│   ├── config.py         # Application configuration
│   └── utils.py          # Utility functions
├── views/                 # Template files
│   ├── base.html         # Base template
│   ├── index.html        # Homepage
│   ├── blog.html         # Blog listing
│   ├── blog_post.html    # Individual post
│   ├── portfolio.html    # Portfolio page
│   ├── 404.html          # Error page
│   └── components/       # Reusable components
├── assets/               # Static files
│   ├── js/              # JavaScript files
│   └── img/             # Images
└── content/             # Blog content
    └── posts/           # Markdown blog posts
```

## 🚀 Quick Start

### Local Development

```bash
# Clone the repository
git clone <your-repository-url>
cd staticle

# Set up development environment
chmod +x scripts/*.sh
./scripts/setup.sh

# Start development server
./scripts/start.sh
```

### Manual Setup

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start Flask development server
python app.py
```

### Access Points

- **Main Site**: <http://localhost:5001>
- **Blog**: <http://localhost:5001/blog>
- **Portfolio**: <http://localhost:5001/portfolio>

## 📝 Adding Content

Create markdown files in `content/posts/` with frontmatter:

```markdown
---
title: "Your Post Title"
date: 2025-06-16
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

### Flask Benefits

- Simple and reliable Python framework
- Easy to understand and maintain
- Extensive ecosystem and community support
- Perfect for content-driven websites

### Modular Design

- Clean separation of concerns
- Reusable components in `core/` directory
- Easy to extend and maintain

## � Deployment

### Render (Recommended)

1. **Connect Repository**: Link your GitHub repository to Render
2. **Auto-Deploy**: Render will automatically detect the Flask app
3. **Environment**: Python 3.11.0 (specified in `runtime.txt`)
4. **Build Command**: `pip install -r requirements.txt`
5. **Start Command**: `gunicorn app:app` (from `Procfile`)

### Manual Deployment Script

```bash
# Deploy to Render
./scripts/deploy-render.sh
```

### Production Build Validation

```bash
# Test production build locally
./scripts/build.sh
```

## 🔧 Development

### Adding New Features

1. **Backend**: Add routes in `app.py`
2. **Core Logic**: Create modules in `core/` directory
3. **Frontend**: Create templates in `views/`
4. **Components**: Add HTMX components in `views/components/`
5. **Styling**: Use TailwindCSS classes
6. **Content**: Add markdown files to `content/posts/`

### Project Scripts

```bash
# Development server
./scripts/start.sh

# Environment setup
./scripts/setup.sh

# Production build test
./scripts/build.sh

# Deploy to Render
./scripts/deploy-render.sh
```

## 🧪 Testing

```bash
# Start development server
python app.py

# Test blog functionality
curl http://localhost:5001/blog

# Test individual post
curl http://localhost:5001/blog/your-post-slug
```

## 🔄 Migration Notes

This project has been migrated from FastAPI to Flask for:

- Simpler deployment on Render
- Better compatibility with traditional hosting
- Easier maintenance and understanding
- Faster development cycle

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 🛟 Support

- Create an issue for bug reports
- Discussions for feature requests
- Check existing issues before creating new ones

---

Built with ❤️ using Flask, HTMX, and TailwindCSS. Ready for deployment on Render.
