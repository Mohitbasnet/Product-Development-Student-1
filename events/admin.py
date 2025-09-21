from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'date', 'location', 'is_featured', 'registration_status']
    list_filter = ['event_type', 'is_featured', 'date', 'created_at']
    search_fields = ['title', 'description', 'location']
    list_editable = ['is_featured']
    ordering = ['-date']
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Event Information', {
            'fields': ('title', 'description', 'date', 'location', 'image')
        }),
        ('Event Type & Status', {
            'fields': ('event_type', 'is_featured')
        }),
        ('Registration', {
            'fields': ('registration_url', 'max_attendees', 'current_attendees')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at', 'registration_status']
