# urls.py
from django.urls import path
from . import views

app_name="news_media"

urlpatterns = [
    path('new/', views.news_section, name='news_section'),
    path('new/<slug:slug>/', views.news_details, name='news_details'),
    
    path('media/', views.media_section, name='media_section'),
    path('media/<slug:slug>/', views.media_details, name='media_details'),
    
]
