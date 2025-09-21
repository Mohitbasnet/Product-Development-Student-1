import django_filters
from .models import ContactInquiry
class ContactInquiryFilter(django_filters.FilterSet):
    """Custom filter for ContactInquiry admin"""
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name contains')
    company = django_filters.CharFilter(lookup_expr='icontains', label='Company contains')
    country = django_filters.CharFilter(lookup_expr='icontains', label='Country contains')
    job_title = django_filters.CharFilter(lookup_expr='icontains', label='Job title contains')
    created_after = django_filters.DateFilter(
        field_name='created_at', 
        lookup_expr='gte', 
        label='Created after'
    )
    created_before = django_filters.DateFilter(
        field_name='created_at', 
        lookup_expr='lte', 
        label='Created before'
    )
    class Meta:
        model = ContactInquiry
        fields = ['name', 'company', 'country', 'job_title', 'is_processed', 'created_after', 'created_before']