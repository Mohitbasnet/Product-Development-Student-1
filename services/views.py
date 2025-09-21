from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import JsonResponse
from django.db import models
from .models import Service, PastSolution
from .forms import ServiceRatingForm
from testimonials.models import Testimonial

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
    
    # Add rating information to each service after pagination
    for service in page_obj:
        testimonials = Testimonial.objects.filter(service=service, is_approved=True)
        avg_rating = testimonials.aggregate(avg_rating=models.Avg('rating'))['avg_rating'] or 0
        service.avg_rating = round(avg_rating, 1) if avg_rating else 0
        service.total_ratings = testimonials.count()
    
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
    
    # Get testimonials for this service
    service_testimonials = Testimonial.objects.filter(
        service=service,
        is_approved=True
    ).order_by('-created_at')[:5]
    
    # Handle rating form submission
    if request.method == 'POST':
        form = ServiceRatingForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.service = service
            testimonial.is_approved = False  # Require approval
            testimonial.save()
            messages.success(request, 'Thank you for your rating! Your review will be published after approval.')
            return redirect('services:service_detail', slug=service.slug)
    else:
        form = ServiceRatingForm()
    
    # Calculate average rating
    avg_rating = service_testimonials.aggregate(
        avg_rating=models.Avg('rating')
    )['avg_rating'] or 0
    
    context = {
        'service': service,
        'related_services': related_services,
        'service_testimonials': service_testimonials,
        'rating_form': form,
        'avg_rating': round(avg_rating, 1) if avg_rating else 0,
        'total_ratings': service_testimonials.count(),
        'page_title': service.title,
        'page_description': service.short_description,
    }
    return render(request, 'services/service_detail.html', context)


def past_solutions_view(request):
    """Past solutions page view"""
    category = request.GET.get('category')
    
    solutions = PastSolution.objects.filter(is_published=True)
    if category:
        solutions = solutions.filter(category=category)
    
    solutions = solutions.order_by('-completion_date')
    
    # Pagination - 6 solutions per page
    paginator = Paginator(solutions, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'solutions': page_obj,
        'selected_category': category,
        'page_title': 'Past Solutions',
        'page_description': 'Explore our portfolio of completed AI-powered solutions and successful projects.',
    }
    return render(request, 'services/past_solutions.html', context)


def past_solution_detail_view(request, slug):
    """Past solution detail page view"""
    solution = get_object_or_404(PastSolution, slug=slug, is_published=True)
    
    # Get related solutions (same category, excluding current solution)
    related_solutions = PastSolution.objects.filter(
        category=solution.category,
        is_published=True
    ).exclude(id=solution.id)[:3]
    
    context = {
        'solution': solution,
        'related_solutions': related_solutions,
        'page_title': solution.title,
        'page_description': solution.short_description,
    }
    return render(request, 'services/past_solution_detail.html', context)