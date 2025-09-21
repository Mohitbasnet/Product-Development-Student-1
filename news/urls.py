from django.urls import path
from . import views
app_name = 'news'
urlpatterns = [
    path('', views.news_view, name='news'),
    path('<slug:slug>/', views.article_detail_view, name='article_detail'),
]