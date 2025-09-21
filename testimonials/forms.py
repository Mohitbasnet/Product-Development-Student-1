from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    """Form for submitting testimonials with service rating"""
    
    class Meta:
        model = Testimonial
        fields = ['customer_name', 'company', 'job_title', 'rating', 'content']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name',
                'required': True
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Company',
                'required': True
            }),
            'job_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Job Title (Optional)'
            }),
            'rating': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Share your experience with this service...',
                'required': True
            }),
        }
        labels = {
            'customer_name': 'Your Name',
            'company': 'Company',
            'job_title': 'Job Title',
            'rating': 'Rating',
            'content': 'Your Review',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make job_title optional
        self.fields['job_title'].required = False
