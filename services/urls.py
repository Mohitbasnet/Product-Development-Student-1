from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.services_view, name='services'),
    path('<slug:slug>/', views.service_detail_view, name='service_detail'),
]
