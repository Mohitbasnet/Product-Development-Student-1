from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from contact.models import ContactInquiry
from news.models import Article
from events.models import Event
from testimonials.models import Testimonial
from services.models import Service
from gallery.models import Photo

@staff_member_required
def analytics_dashboard(request):
    now = timezone.now()
    last_30_days = now - timedelta(days=30)
    last_7_days = now - timedelta(days=7)
    
    total_inquiries = ContactInquiry.objects.count()
    pending_inquiries = ContactInquiry.objects.filter(is_processed=False).count()
    recent_inquiries = ContactInquiry.objects.filter(created_at__gte=last_7_days).count()
    total_articles = Article.objects.count()
    published_articles = Article.objects.filter(is_published=True).count()
    draft_articles = Article.objects.filter(is_published=False).count()
    featured_articles = Article.objects.filter(is_featured=True).count()
    
    total_events = Event.objects.count()
    upcoming_events = Event.objects.filter(event_type='upcoming').count()
    past_events = Event.objects.filter(event_type='past').count()
    
    total_testimonials = Testimonial.objects.count()
    approved_testimonials = Testimonial.objects.filter(is_approved=True).count()
    featured_testimonials = Testimonial.objects.filter(is_featured=True).count()
    
    total_services = Service.objects.count()
    active_services = Service.objects.filter(is_active=True).count()
    featured_services = Service.objects.filter(is_featured=True).count()
    
    total_photos = Photo.objects.count()
    featured_photos = Photo.objects.filter(is_featured=True).count()
    
    recent_inquiries_list = ContactInquiry.objects.order_by('-created_at')[:5]
    recent_articles_list = Article.objects.order_by('-created_at')[:5]
    recent_events_list = Event.objects.order_by('-created_at')[:5]
    today_inquiries = ContactInquiry.objects.filter(created_at__date=now.date()).count()
    this_week_inquiries = ContactInquiry.objects.filter(created_at__gte=last_7_days).count()
    this_month_inquiries = ContactInquiry.objects.filter(created_at__gte=last_30_days).count()
    
    monthly_inquiries = []
    for i in range(6):
        month_start = now - timedelta(days=30*i)
        month_end = month_start + timedelta(days=30)
        count = ContactInquiry.objects.filter(
            created_at__gte=month_start,
            created_at__lt=month_end
        ).count()
        monthly_inquiries.append({
            'month': month_start.strftime('%b'),
            'count': count
        })
    monthly_inquiries.reverse()
    
    country_stats = ContactInquiry.objects.values('country').annotate(
        count=Count('country')
    ).order_by('-count')[:10]
    
    article_categories = Article.objects.values('category').annotate(
        count=Count('category')
    ).order_by('-count')
    service_categories = Service.objects.values('category').annotate(
        count=Count('category')
    ).order_by('-count')
    
    event_types = Event.objects.values('event_type').annotate(
        count=Count('event_type')
    ).order_by('-count')
    
    context = {
        'total_inquiries': total_inquiries,
        'pending_inquiries': pending_inquiries,
        'recent_inquiries': recent_inquiries,
        'total_articles': total_articles,
        'published_articles': published_articles,
        'draft_articles': draft_articles,
        'featured_articles': featured_articles,
        'total_events': total_events,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'total_testimonials': total_testimonials,
        'approved_testimonials': approved_testimonials,
        'featured_testimonials': featured_testimonials,
        'total_services': total_services,
        'active_services': active_services,
        'featured_services': featured_services,
        'total_photos': total_photos,
        'featured_photos': featured_photos,
        'today_inquiries': today_inquiries,
        'this_week_inquiries': this_week_inquiries,
        'this_month_inquiries': this_month_inquiries,
        'recent_inquiries_list': recent_inquiries_list,
        'recent_articles_list': recent_articles_list,
        'recent_events_list': recent_events_list,
        'monthly_inquiries': monthly_inquiries,
        'country_stats': country_stats,
        'article_categories': article_categories,
        'service_categories': service_categories,
        'event_types': event_types,
    }
    
    return render(request, 'admin/analytics_dashboard.html', context)
