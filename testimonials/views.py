from django.shortcuts import render
from .models import Testimonial

def testimonials_view(request):
    """Testimonials page view"""
    testimonials = Testimonial.objects.filter(is_approved=True).order_by('-created_at')
    
    context = {
        'testimonials': testimonials,
        'page_title': 'Testimonials',
        'page_description': 'Hear what our clients say about our AI-powered solutions.',
    }
    return render(request, 'testimonials/testimonials.html', context)