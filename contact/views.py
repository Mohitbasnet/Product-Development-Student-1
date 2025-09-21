from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactInquiry
from .forms import ContactForm

def contact_view(request):
    """Contact page view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the inquiry
            inquiry = form.save()
            
            # Send email notification (optional)
            try:
                send_mail(
                    'New Contact Inquiry - AI-Solutions',
                    f'New inquiry from {inquiry.name} ({inquiry.email})\n\nCompany: {inquiry.company}\nJob Title: {inquiry.job_title}\n\nDetails:\n{inquiry.job_details}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
            except Exception as e:
                # Log error but don't fail the form submission
                print(f"Email sending failed: {e}")
            
            messages.success(request, 'Thank you for your inquiry! We will get back to you soon.')
            return redirect('contact:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'page_title': 'Contact Us',
        'page_description': 'Get in touch with our team to discuss your AI solution needs.',
    }
    return render(request, 'contact/contact.html', context)