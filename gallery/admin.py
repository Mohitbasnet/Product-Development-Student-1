from django.contrib import admin
from .models import Photo
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'created_at']
    list_filter = ['category', 'is_featured', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_featured']
    ordering = ['-created_at']
    fieldsets = (
        ('Photo Information', {
            'fields': ('title', 'image', 'description', 'category')
        }),
        ('Display Options', {
            'fields': ('is_featured',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']