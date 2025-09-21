from django.shortcuts import render, get_object_or_404
from .models import Article

def news_view(request):
    """News/Blog page view"""
    category = request.GET.get('category')
    
    articles = Article.objects.filter(is_published=True)
    if category:
        articles = articles.filter(category=category)
    
    articles = articles.order_by('-published_date')
    
    # Get unique categories for filter
    categories = Article.CATEGORY_CHOICES
    
    context = {
        'articles': articles,
        'categories': categories,
        'selected_category': category,
        'page_title': 'News & Blog',
        'page_description': 'Stay updated with the latest news and insights from AI-Solutions.',
    }
    return render(request, 'news/news.html', context)

def article_detail_view(request, slug):
    """Article detail page view"""
    article = get_object_or_404(Article, slug=slug, is_published=True)
    
    # Increment view count
    article.increment_view_count()
    
    # Get related articles (same category, excluding current article)
    related_articles = Article.objects.filter(
        category=article.category,
        is_published=True
    ).exclude(id=article.id)[:3]
    
    # Get recent articles for sidebar
    recent_articles = Article.objects.filter(
        is_published=True
    ).exclude(id=article.id)[:5]
    
    context = {
        'article': article,
        'related_articles': related_articles,
        'recent_articles': recent_articles,
        'page_title': article.title,
        'page_description': article.excerpt,
    }
    return render(request, 'news/article_detail.html', context)