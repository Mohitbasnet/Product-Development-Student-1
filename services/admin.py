from django.contrib import admin
from django import forms
from .models import Service
from .widgets import FeaturesWidget

class ServiceForm(forms.ModelForm):
    """Custom form for Service with enhanced features field"""
    
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'features': FeaturesWidget(),
        }

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceForm
    list_display = ['title', 'category', 'is_featured', 'is_active', 'formatted_price', 'created_at']
    list_filter = ['category', 'is_featured', 'is_active', 'created_at']
    search_fields = ['title', 'description', 'short_description']
    list_editable = ['is_featured', 'is_active']
    ordering = ['title']
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Service Information', {
            'fields': ('title', 'slug', 'short_description', 'description', 'category', 'icon', 'image')
        }),
        ('Features', {
            'fields': ('features',)
        }),
        ('Pricing', {
            'fields': ('price_starting_from', 'currency')
        }),
        ('Display Options', {
            'fields': ('is_featured', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at', 'formatted_price']
