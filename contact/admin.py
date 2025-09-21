from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import ContactInquiry

@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'email', 'country', 'created_at', 'is_processed', 'actions_column']
    list_filter = ['is_processed', 'country', 'created_at']
    search_fields = ['name', 'email', 'company', 'job_title']
    readonly_fields = ['created_at', 'actions_column']
    list_editable = ['is_processed']
    ordering = ['-created_at']
    actions = ['mark_as_processed', 'mark_as_unprocessed', 'export_contact_info', 'send_follow_up_email']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone', 'company', 'country', 'job_title')
        }),
        ('Job Details', {
            'fields': ('job_details',)
        }),
        ('Status', {
            'fields': ('is_processed', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related()
    
    def actions_column(self, obj):
        """Custom actions column with quick action buttons"""
        if obj.is_processed:
            return format_html(
                '<span class="badge badge-success">Processed</span>'
            )
        else:
            return format_html(
                '<a href="{}" class="btn btn-sm btn-primary">Process</a>',
                reverse('admin:contact_contactinquiry_change', args=[obj.pk])
            )
    actions_column.short_description = 'Actions'
    actions_column.allow_tags = True
    
    def mark_as_processed(self, request, queryset):
        """Mark selected inquiries as processed"""
        updated = queryset.update(is_processed=True)
        self.message_user(
            request,
            f'Successfully marked {updated} inquiry(ies) as processed.',
            messages.SUCCESS
        )
    mark_as_processed.short_description = "Mark selected inquiries as processed"
    
    def mark_as_unprocessed(self, request, queryset):
        """Mark selected inquiries as unprocessed"""
        updated = queryset.update(is_processed=False)
        self.message_user(
            request,
            f'Successfully marked {updated} inquiry(ies) as unprocessed.',
            messages.SUCCESS
        )
    mark_as_unprocessed.short_description = "Mark selected inquiries as unprocessed"
    
    def export_contact_info(self, request, queryset):
        """Export contact information to CSV"""
        import csv
        from django.http import HttpResponse
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="contact_inquiries.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Name', 'Email', 'Phone', 'Company', 'Country', 'Job Title', 'Created At', 'Processed'])
        
        for inquiry in queryset:
            writer.writerow([
                inquiry.name,
                inquiry.email,
                inquiry.phone,
                inquiry.company,
                inquiry.country,
                inquiry.job_title,
                inquiry.created_at.strftime('%Y-%m-%d %H:%M'),
                'Yes' if inquiry.is_processed else 'No'
            ])
        
        self.message_user(
            request,
            f'Successfully exported {queryset.count()} inquiry(ies) to CSV.',
            messages.SUCCESS
        )
        return response
    export_contact_info.short_description = "Export selected inquiries to CSV"
    
    def send_follow_up_email(self, request, queryset):
        """Send follow-up email to selected inquiries"""
        # This would typically integrate with an email service
        count = queryset.count()
        self.message_user(
            request,
            f'Follow-up email would be sent to {count} inquiry(ies). (Email service not configured)',
            messages.INFO
        )
    send_follow_up_email.short_description = "Send follow-up email"
