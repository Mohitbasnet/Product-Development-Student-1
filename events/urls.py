from django.urls import path
from . import views
app_name = 'events'
urlpatterns = [
    path('', views.events_view, name='events'),
    path('<int:pk>/', views.event_detail_view, name='event_detail'),
]