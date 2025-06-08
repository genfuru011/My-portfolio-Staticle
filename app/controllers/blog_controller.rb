class BlogController < ApplicationController
  before_action :initialize_blog_manager
  
  def index
    # Blog listing page - equivalent to Flask's /blog route
    @posts = @blog_manager.get_all_posts
    @categories = @blog_manager.get_categories
    @tags = @blog_manager.get_tags
    @current_category = params[:category]
    @current_tag = params[:tag]
    
    # Filter by category if specified
    if @current_category.present?
      @posts = @blog_manager.get_posts_by_category(@current_category)
    end
    
    # Filter by tag if specified
    if @current_tag.present?
      @posts = @blog_manager.get_posts_by_tag(@current_tag)
    end
  end

  def show
    # Individual blog post - equivalent to Flask's /blog/<slug> route
    @post = @blog_manager.get_post_by_slug(params[:slug])
    
    if @post.nil?
      render file: Rails.public_path.join('404.html'), status: :not_found, layout: false
      return
    end
    
    @related_posts = @blog_manager.get_related_posts(@post)
  end
  
  def category
    # Category filtering - equivalent to Flask's /blog/category/<category> route
    @posts = @blog_manager.get_posts_by_category(params[:category])
    @categories = @blog_manager.get_categories
    @tags = @blog_manager.get_tags
    @current_category = params[:category]
    @current_tag = nil
    
    render :index
  end
  
  def tag
    # Tag filtering - equivalent to Flask's /blog/tag/<tag> route  
    @posts = @blog_manager.get_posts_by_tag(params[:tag])
    @categories = @blog_manager.get_categories
    @tags = @blog_manager.get_tags
    @current_category = nil
    @current_tag = params[:tag]
    
    render :index
  end

  private
  
  def initialize_blog_manager
    @blog_manager = BlogManager.new
  end
end
