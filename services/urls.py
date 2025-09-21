from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.services_view, name='services'),
    path('past-solutions/', views.past_solutions_view, name='past_solutions'),
    path('past-solutions/<slug:slug>/', views.past_solution_detail_view, name='past_solution_detail'),
    path('<slug:slug>/', views.service_detail_view, name='service_detail'),
]
