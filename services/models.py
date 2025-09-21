from django.db import models
from django.utils import timezone
import json

class Service(models.Model):
    """
    Model to store company services and solutions.
    Supports features list and service categorization.
    """
    CATEGORY_CHOICES = [
        ('ai_solutions', 'AI Solutions'),
        ('automation', 'Automation'),
        ('data_analytics', 'Data Analytics'),
        ('machine_learning', 'Machine Learning'),
        ('consulting', 'Consulting'),
        ('integration', 'Integration'),
        ('support', 'Support'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200, help_text="Service title")
    slug = models.SlugField(max_length=200, unique=True, help_text="URL-friendly version of title")
    description = models.TextField(help_text="Service description")
    short_description = models.CharField(
        max_length=300, 
        help_text="Short service description for cards"
    )
    icon = models.CharField(
        max_length=50, 
        help_text="Font Awesome icon class (e.g., 'fas fa-robot')"
    )
    category = models.CharField(
        max_length=50, 
        choices=CATEGORY_CHOICES, 
        default='other',
        help_text="Service category"
    )
    features = models.TextField(
        help_text="JSON string of features list",
        default='[]'
    )
    is_featured = models.BooleanField(default=False, help_text="Show in featured section")
    is_active = models.BooleanField(default=True, help_text="Whether service is currently offered")
    price_starting_from = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True,
        help_text="Starting price for the service"
    )
    currency = models.CharField(max_length=3, default='USD', help_text="Currency code")
    image = models.ImageField(
        upload_to='services/', 
        blank=True, 
        help_text="Service image"
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the service was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the service was last updated")
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['title']
    
    def __str__(self):
        return f"{self.title} - {self.get_category_display()}"
    
    @property
    def features_list(self):
        """Return features as a Python list"""
        try:
            return json.loads(self.features)
        except (json.JSONDecodeError, TypeError):
            return []
    
    def set_features_list(self, features_list):
        """Set features from a Python list"""
        self.features = json.dumps(features_list)
    
    @property
    def image_url(self):
        """Return the URL of the service image"""
        if self.image:
            return self.image.url
        return None
    
    @property
    def formatted_price(self):
        """Return formatted price string"""
        if self.price_starting_from:
            return f"From {self.currency} {self.price_starting_from:,.2f}"
        return "Contact for pricing"
