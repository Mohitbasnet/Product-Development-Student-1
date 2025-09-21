from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Testimonial
from .forms import TestimonialForm

def testimonials_view(request):
    """Testimonials page view"""
    testimonials = Testimonial.objects.filter(is_approved=True).order_by('-created_at')
    
    context = {
        'testimonials': testimonials,
        'page_title': 'Testimonials',
        'page_description': 'Hear what our clients say about our AI-powered solutions.',
    }
    return render(request, 'testimonials/testimonials.html', context)

def submit_testimonial(request, service_id=None):
    """Handle testimonial submission from service pages"""
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            if service_id:
                from services.models import Service
                try:
                    service = Service.objects.get(id=service_id)
                    testimonial.service = service
                except Service.DoesNotExist:
                    pass
            testimonial.is_approved = False  # Require approval
            testimonial.save()
            messages.success(request, 'Thank you for your review! It will be published after approval.')
            if service_id:
                return redirect('services:service_detail', slug=service.slug)
            else:
                return redirect('testimonials:testimonials')
    else:
        form = TestimonialForm()
    
    context = {
        'form': form,
        'service_id': service_id,
    }
    return render(request, 'testimonials/testimonial_form.html', context)