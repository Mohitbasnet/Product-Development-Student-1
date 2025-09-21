from django.db import models
from django.utils import timezone
class Testimonial(models.Model):
    """
    Model to store customer testimonials with ratings.
    Supports featured testimonials and company information.
    """
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    customer_name = models.CharField(max_length=100, help_text="Customer's name")
    company = models.CharField(max_length=100, help_text="Customer's company")
    job_title = models.CharField(max_length=100, blank=True, help_text="Customer's job title")
    service = models.ForeignKey(
        'services.Service', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True,
        help_text="Service being rated (optional)"
    )
    rating = models.IntegerField(
        choices=RATING_CHOICES, 
        default=5,
        help_text="Customer rating (1-5 stars)"
    )
    content = models.TextField(help_text="Testimonial content")
    image = models.ImageField(
        upload_to='testimonials/', 
        blank=True, 
        help_text="Customer photo (optional)"
    )
    is_featured = models.BooleanField(default=False, help_text="Show in featured section")
    is_approved = models.BooleanField(default=False, help_text="Whether testimonial is approved for display")
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the testimonial was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the testimonial was last updated")
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
        ordering = ['-created_at']
    def __str__(self):
        return f"{self.customer_name} - {self.company} ({self.rating} stars)"
    @property
    def image_url(self):
        """Return the URL of the customer image"""
        if self.image:
            return self.image.url
        return None
    @property
    def stars_display(self):
        """Return stars as HTML for display"""
        return "★" * self.rating + "☆" * (5 - self.rating)
    @property
    def short_content(self):
        """Return truncated content for admin display"""
        return self.content[:100] + "..." if len(self.content) > 100 else self.content