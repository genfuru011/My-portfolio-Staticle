# frozen_string_literal: true

require "front_matter_parser"
require "redcarpet"

class BlogManager
  attr_reader :posts_dir, :posts

  def initialize(posts_dir = Rails.root.join("content", "posts"))
    @posts_dir = posts_dir
    @posts = []
    load_posts
  end

  def load_posts
    @posts = []

    return [] unless Dir.exist?(@posts_dir)

    Dir.glob(File.join(@posts_dir, "*.md")).each do |post_path|
      filename = File.basename(post_path)
      post = parse_post(post_path, filename)
      @posts << post if post
    end

    # Sort by date (newest first)
    @posts.sort! { |a, b| b[:date] <=> a[:date] }
    @posts
  end

  def get_all_posts
    @posts
  end

  def get_post_by_slug(slug)
    @posts.find { |post| post[:slug] == slug }
  end

  def get_posts_by_category(category)
    @posts.select { |post| post[:category]&.downcase == category.downcase }
  end

  def get_posts_by_tag(tag)
    @posts.select do |post|
      post[:tags]&.map(&:downcase)&.include?(tag.downcase)
    end
  end

  def get_categories
    categories = {}
    @posts.each do |post|
      category = post[:category]&.downcase
      if category && !category.empty?
        categories[category] = categories.fetch(category, 0) + 1
      end
    end
    categories
  end

  def get_tags
    tags = {}
    @posts.each do |post|
      post[:tags]&.each do |tag|
        tag = tag.downcase
        tags[tag] = tags.fetch(tag, 0) + 1
      end
    end
    tags
  end

  def get_related_posts(post, max_posts = 3)
    return [] unless post

    current_category = post[:category]&.downcase
    current_tags = post[:tags]&.map(&:downcase) || []
    current_slug = post[:slug]

    related_posts = []

    @posts.each do |other_post|
      next if other_post[:slug] == current_slug

      score = 0

      # Same category: +5 points
      if other_post[:category]&.downcase == current_category
        score += 5
      end

      # Common tags: +3 points each
      other_tags = other_post[:tags]&.map(&:downcase) || []
      current_tags.each do |tag|
        score += 3 if other_tags.include?(tag)
      end

      if score > 0
        related_posts << {
          post: other_post,
          score: score
        }
      end
    end

    # Sort by score and return required number
    related_posts.sort! { |a, b| b[:score] <=> a[:score] }
    related_posts.first(max_posts).map { |item| item[:post] }
  end

  private

  def parse_post(post_path, filename)
    content = File.read(post_path, encoding: "utf-8")
    parsed = FrontMatterParser.parse(content)

    slug = File.basename(filename, ".md")

    # Convert markdown to HTML using Redcarpet
    renderer = Redcarpet::Render::HTML.new(
      filter_html: false,
      no_intra_emphasis: true,
      tables: true,
      fenced_code_blocks: true,
      autolink: true,
      strikethrough: true,
      space_after_headers: true,
      superscript: true,
      underline: true,
      highlight: true,
      quote: true
    )
    markdown = Redcarpet::Markdown.new(renderer, extensions = {})
    html_content = markdown.render(parsed.content)

    # Parse date
    date = parsed.front_matter["date"]
    if date.is_a?(String)
      begin
        date = Date.parse(date)
      rescue ArgumentError
        date = Date.current
      end
    else
      date ||= Date.current
    end

    {
      title: parsed.front_matter["title"] || "No Title",
      date: date,
      author: parsed.front_matter["author"] || "Anonymous",
      category: parsed.front_matter["category"] || "",
      tags: parsed.front_matter["tags"] || [],
      excerpt: parsed.front_matter["excerpt"] || "",
      content: html_content,
      slug: slug,
      url: "/blog/#{slug}",
      formatted_date: date.strftime("%Y年%m月%d日")
    }
  rescue => e
    Rails.logger.error "Error parsing #{filename}: #{e.message}"
    nil
  end
end