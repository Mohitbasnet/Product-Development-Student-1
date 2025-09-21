from django.contrib import admin
from .models import Testimonial
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'company', 'service', 'rating', 'is_featured', 'is_approved', 'created_at']
    list_filter = ['rating', 'is_featured', 'is_approved', 'service', 'created_at']
    search_fields = ['customer_name', 'company', 'content', 'service__title']
    list_editable = ['is_featured', 'is_approved']
    ordering = ['-created_at']
    fieldsets = (
        ('Customer Information', {
            'fields': ('customer_name', 'company', 'job_title', 'image')
        }),
        ('Service & Content', {
            'fields': ('service', 'rating', 'content')
        }),
        ('Display Options', {
            'fields': ('is_featured', 'is_approved')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']