from django import forms
from .models import Service
from testimonials.models import Testimonial


class ServiceRatingForm(forms.ModelForm):
    """Form for rating a service"""
    
    class Meta:
        model = Testimonial
        fields = ['customer_name', 'company', 'job_title', 'rating', 'content']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name',
                'required': True
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your company name',
                'required': True
            }),
            'job_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your job title (optional)'
            }),
            'rating': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Share your experience with this service...',
                'rows': 4,
                'required': True
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rating'].choices = Testimonial.RATING_CHOICES
        self.fields['rating'].label = 'Rating'
        self.fields['content'].label = 'Your Review'
