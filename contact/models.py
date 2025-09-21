from django.db import models
from django.utils import timezone
class ContactInquiry(models.Model):
    """
    Model to store customer inquiries from the contact form.
    Includes all required fields as specified in the requirements.
    """
    name = models.CharField(max_length=100, help_text="Customer's full name")
    email = models.EmailField(help_text="Customer's email address")
    phone = models.CharField(max_length=20, help_text="Customer's phone number")
    company = models.CharField(max_length=100, help_text="Customer's company name")
    country = models.CharField(max_length=100, help_text="Customer's country")
    job_title = models.CharField(max_length=100, help_text="Customer's job title")
    job_details = models.TextField(help_text="Detailed description of job requirements")
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the inquiry was submitted")
    is_processed = models.BooleanField(default=False, help_text="Whether the inquiry has been processed")
    notes = models.TextField(blank=True, help_text="Internal notes about the inquiry")
    class Meta:
        verbose_name = "Contact Inquiry"
        verbose_name_plural = "Contact Inquiries"
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.name} - {self.company} ({self.created_at.strftime('%Y-%m-%d')})"
    @property
    def short_job_details(self):
        """Return truncated job details for admin display"""
        return self.job_details[:100] + "..." if len(self.job_details) > 100 else self.job_details