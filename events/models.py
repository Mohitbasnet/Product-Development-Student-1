from django.db import models
from django.utils import timezone
class Event(models.Model):
    """
    Model to store upcoming and past events.
    Supports both event types as specified in requirements.
    """
    EVENT_TYPE_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('past', 'Past'),
    ]
    title = models.CharField(max_length=200, help_text="Event title")
    description = models.TextField(help_text="Event description")
    date = models.DateTimeField(help_text="Event date and time")
    location = models.CharField(max_length=200, help_text="Event location")
    image = models.ImageField(upload_to='events/', blank=True, help_text="Event image (optional)")
    event_type = models.CharField(
        max_length=20, 
        choices=EVENT_TYPE_CHOICES, 
        default='upcoming',
        help_text="Event type"
    )
    is_featured = models.BooleanField(default=False, help_text="Show in featured section")
    registration_url = models.URLField(blank=True, help_text="Event registration URL")
    max_attendees = models.PositiveIntegerField(null=True, blank=True, help_text="Maximum number of attendees")
    current_attendees = models.PositiveIntegerField(default=0, help_text="Current number of registered attendees")
    created_at = models.DateTimeField(auto_now_add=True, help_text="When the event was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="When the event was last updated")
    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['-date']
    def __str__(self):
        return f"{self.title} - {self.get_event_type_display()}"
    @property
    def is_upcoming(self):
        """Check if the event is upcoming"""
        return self.date > timezone.now()
    @property
    def is_past(self):
        """Check if the event is past"""
        return self.date <= timezone.now()
    @property
    def image_url(self):
        """Return the URL of the event image"""
        if self.image:
            return self.image.url
        return None
    @property
    def registration_status(self):
        """Get registration status text"""
        if self.max_attendees:
            if self.current_attendees >= self.max_attendees:
                return "Fully Booked"
            elif self.current_attendees > 0:
                return f"{self.current_attendees}/{self.max_attendees} Registered"
            else:
                return "Open for Registration"
        return "Open for Registration"