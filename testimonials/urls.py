from django.urls import path
from . import views
app_name = 'testimonials'
urlpatterns = [
    path('', views.testimonials_view, name='testimonials'),
    path('submit/', views.submit_testimonial, name='submit_testimonial'),
    path('submit/<int:service_id>/', views.submit_testimonial, name='submit_testimonial_service'),
]