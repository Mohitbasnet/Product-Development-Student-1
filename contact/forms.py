from django import forms
from .models import ContactInquiry

class ContactForm(forms.ModelForm):
    """Contact form for customer inquiries"""
    
    class Meta:
        model = ContactInquiry
        fields = ['name', 'email', 'phone', 'company', 'country', 'job_title', 'job_details']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@company.com',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+44 123 456 7890',
                'required': True
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your company name',
                'required': True
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your country',
                'required': True
            }),
            'job_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your job title',
                'required': True
            }),
            'job_details': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Please describe your project requirements and how we can help...',
                'rows': 5,
                'required': True
            }),
        }
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'company': 'Company Name',
            'country': 'Country',
            'job_title': 'Job Title',
            'job_details': 'Project Details',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add form validation attributes
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': field.widget.attrs.get('class', '') + ' form-control'
            })
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            # Basic email validation
            if not email or '@' not in email:
                raise forms.ValidationError('Please enter a valid email address.')
        return email
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            # Basic phone validation - remove spaces and check for digits
            clean_phone = ''.join(filter(str.isdigit, phone))
            if len(clean_phone) < 7:
                raise forms.ValidationError('Please enter a valid phone number.')
        return phone
