from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Photo

def gallery_view(request):
    """Gallery page view"""
    category = request.GET.get('category')
    
    photos = Photo.objects.all()
    if category:
        photos = photos.filter(category=category)
    
    photos = photos.order_by('-created_at')
    
    # Pagination - 9 photos per page
    paginator = Paginator(photos, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Get unique categories for filter
    categories = Photo.CATEGORY_CHOICES
    
    context = {
        'photos': page_obj,
        'categories': categories,
        'selected_category': category,
        'page_title': 'Gallery',
        'page_description': 'Explore our collection of photos showcasing our work and events.',
    }
    return render(request, 'gallery/gallery.html', context)