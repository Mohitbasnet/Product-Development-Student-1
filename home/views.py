from django.shortcuts import render
from services.models import Service
from testimonials.models import Testimonial
from news.models import Article

def home_view(request):
    """Home page view with featured content"""
    from django.db import models
    
    # Get featured services
    featured_services = Service.objects.filter(
        is_featured=True, 
        is_active=True
    ).order_by('title')[:3]
    
    # Add rating information to each service
    for service in featured_services:
        testimonials = Testimonial.objects.filter(service=service, is_approved=True)
        avg_rating = testimonials.aggregate(avg_rating=models.Avg('rating'))['avg_rating'] or 0
        service.avg_rating = round(avg_rating, 1) if avg_rating else 0
        service.total_ratings = testimonials.count()
    
    # Get featured testimonials
    featured_testimonials = Testimonial.objects.filter(
        is_featured=True,
        is_approved=True
    ).order_by('-created_at')[:3]
    
    # Get recent articles
    recent_articles = Article.objects.filter(
        is_published=True
    ).order_by('-published_date')[:3]
    
    context = {
        'featured_services': featured_services,
        'featured_testimonials': featured_testimonials,
        'recent_articles': recent_articles,
    }
    
    return render(request, 'home/index.html', context)