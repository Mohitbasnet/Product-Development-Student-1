from django.shortcuts import render, get_object_or_404
from .models import Event

def events_view(request):
    """Events page view"""
    event_type = request.GET.get('type', 'upcoming')
    
    events = Event.objects.all()
    if event_type == 'upcoming':
        events = events.filter(event_type='upcoming').order_by('date')
    elif event_type == 'past':
        events = events.filter(event_type='past').order_by('-date')
    
    context = {
        'events': events,
        'selected_type': event_type,
        'page_title': 'Events',
        'page_description': 'Join our upcoming events and explore our past activities.',
    }
    return render(request, 'events/events.html', context)

def event_detail_view(request, pk):
    """Event detail page view"""
    event = get_object_or_404(Event, pk=pk)
    
    # Get related events (same type, excluding current event)
    related_events = Event.objects.filter(
        event_type=event.event_type
    ).exclude(id=event.id)[:3]
    
    context = {
        'event': event,
        'related_events': related_events,
        'page_title': event.title,
        'page_description': event.description[:160],
    }
    return render(request, 'events/event_detail.html', context)