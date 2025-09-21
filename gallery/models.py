from django.db import models
from django.utils import timezone

class Photo(models.Model):
    """
    Model to store photos for the gallery page.
    Supports categorization and descriptions for promotional events.
    """
    CATEGORY_CHOICES = [
        ('events', 'Events'),
        ('team', 'Team'),
        ('office', 'Office'),
        ('promotional', 'Promotional'),
        ('conferences', 'Conferences'),
        ('awards', 'Awards'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200, help_text="Photo title")
    image = models.ImageField(upload_to='gallery/', blank=True, help_text="Photo file (optional)")
    description = models.TextField(blank=True, help_text="Photo description")
    category = models.CharField(
        max_length=50, 
        choices=CATEGORY_CHOICES, 
        default='other',
        help_text="Photo category"
    )
    is_featured = models.BooleanField(default=False, help_text="Show in featured section")
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the photo was uploaded")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the photo was last updated")
    
    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"
    
    @property
    def image_url(self):
        """Return the URL of the image"""
        if self.image:
            return self.image.url
        return None
