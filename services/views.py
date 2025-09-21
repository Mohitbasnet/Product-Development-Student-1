from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Service

def services_view(request):
    """Services page view"""
    category = request.GET.get('category')
    
    services = Service.objects.filter(is_active=True)
    if category:
        services = services.filter(category=category)
    
    services = services.order_by('title')
    
    # Pagination - 6 services per page
    paginator = Paginator(services, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'services': page_obj,
        'selected_category': category,
        'page_title': 'Our Services',
        'page_description': 'Discover our comprehensive AI-powered solutions for digital employee experience.',
    }
    return render(request, 'services/services.html', context)

def service_detail_view(request, slug):
    """Service detail page view"""
    service = get_object_or_404(Service, slug=slug, is_active=True)
    
    # Get related services (same category, excluding current service)
    related_services = Service.objects.filter(
        category=service.category,
        is_active=True
    ).exclude(id=service.id)[:3]
    
    context = {
        'service': service,
        'related_services': related_services,
        'page_title': service.title,
        'page_description': service.short_description,
    }
    return render(request, 'services/service_detail.html', context)