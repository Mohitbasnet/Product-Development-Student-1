from django.db import models
from django.utils import timezone

class Article(models.Model):
    """
    Model to store news/blog articles.
    Supports publishing workflow and categorization.
    """
    CATEGORY_CHOICES = [
        ('ai_news', 'AI News'),
        ('company_news', 'Company News'),
        ('technology', 'Technology'),
        ('industry_insights', 'Industry Insights'),
        ('case_studies', 'Case Studies'),
        ('announcements', 'Announcements'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200, help_text="Article title")
    slug = models.SlugField(max_length=200, unique=True, help_text="URL-friendly version of title")
    content = models.TextField(help_text="Article content")
    excerpt = models.TextField(max_length=300, help_text="Short article summary")
    image = models.ImageField(upload_to='news/', blank=True, help_text="Article featured image (optional)")
    author = models.CharField(max_length=100, help_text="Article author")
    category = models.CharField(
        max_length=50, 
        choices=CATEGORY_CHOICES, 
        default='other',
        help_text="Article category"
    )
    is_published = models.BooleanField(default=False, help_text="Whether the article is published")
    is_featured = models.BooleanField(default=False, help_text="Show in featured section")
    published_date = models.DateTimeField(
        default=timezone.now, 
        help_text="When the article was published"
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the article was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the article was last updated")
    view_count = models.PositiveIntegerField(default=0, help_text="Number of times article was viewed")
    tags = models.CharField(
        max_length=500, 
        blank=True, 
        help_text="Comma-separated tags for the article"
    )
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-published_date']
    
    def __str__(self):
        return f"{self.title} - {self.author}"
    
    @property
    def image_url(self):
        """Return the URL of the article image"""
        if self.image:
            return self.image.url
        return None
    
    @property
    def tag_list(self):
        """Return tags as a list"""
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',')]
        return []
    
    @property
    def reading_time(self):
        """Estimate reading time in minutes"""
        words_per_minute = 200
        word_count = len(self.content.split())
        return max(1, round(word_count / words_per_minute))
    
    def increment_view_count(self):
        """Increment the view count"""
        self.view_count += 1
        self.save(update_fields=['view_count'])
