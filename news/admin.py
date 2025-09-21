from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'is_published', 'is_featured', 'published_date', 'view_count', 'reading_time_display']
    list_filter = ['category', 'is_published', 'is_featured', 'published_date', 'created_at']
    search_fields = ['title', 'content', 'author', 'tags']
    list_editable = ['is_published', 'is_featured']
    ordering = ['-published_date']
    date_hierarchy = 'published_date'
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish_articles', 'unpublish_articles', 'feature_articles', 'unfeature_articles', 'export_articles']
    
    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'slug', 'author', 'category', 'image')
        }),
        ('Content', {
            'fields': ('excerpt', 'content', 'tags')
        }),
        ('Publishing', {
            'fields': ('is_published', 'is_featured', 'published_date')
        }),
        ('Statistics', {
            'fields': ('view_count',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at', 'view_count']
    
    def reading_time_display(self, obj):
        """Display reading time in minutes"""
        return f"{obj.reading_time} min"
    reading_time_display.short_description = 'Reading Time'
    
    def publish_articles(self, request, queryset):
        """Publish selected articles"""
        updated = queryset.update(is_published=True)
        self.message_user(
            request,
            f'Successfully published {updated} article(s).',
            messages.SUCCESS
        )
    publish_articles.short_description = "Publish selected articles"
    
    def unpublish_articles(self, request, queryset):
        """Unpublish selected articles"""
        updated = queryset.update(is_published=False)
        self.message_user(
            request,
            f'Successfully unpublished {updated} article(s).',
            messages.SUCCESS
        )
    unpublish_articles.short_description = "Unpublish selected articles"
    
    def feature_articles(self, request, queryset):
        """Feature selected articles"""
        updated = queryset.update(is_featured=True)
        self.message_user(
            request,
            f'Successfully featured {updated} article(s).',
            messages.SUCCESS
        )
    feature_articles.short_description = "Feature selected articles"
    
    def unfeature_articles(self, request, queryset):
        """Unfeature selected articles"""
        updated = queryset.update(is_featured=False)
        self.message_user(
            request,
            f'Successfully unfeatured {updated} article(s).',
            messages.SUCCESS
        )
    unfeature_articles.short_description = "Unfeature selected articles"
    
    def export_articles(self, request, queryset):
        """Export articles to CSV"""
        import csv
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="articles.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Title', 'Author', 'Category', 'Published', 'Featured', 'View Count', 'Reading Time', 'Published Date'])
        
        for article in queryset:
            writer.writerow([
                article.title,
                article.author,
                article.get_category_display(),
                'Yes' if article.is_published else 'No',
                'Yes' if article.is_featured else 'No',
                article.view_count,
                f"{article.reading_time} min",
                article.published_date.strftime('%Y-%m-%d %H:%M') if article.published_date else ''
            ])
        
        self.message_user(
            request,
            f'Successfully exported {queryset.count()} article(s) to CSV.',
            messages.SUCCESS
        )
        return response
    export_articles.short_description = "Export selected articles to CSV"
