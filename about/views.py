from django.shortcuts import render

def about_view(request):
    """About us page view"""
    context = {
        'page_title': 'About Us',
        'page_description': 'Learn more about AI-Solutions and our mission to transform digital employee experience.',
    }
    return render(request, 'about/about.html', context)