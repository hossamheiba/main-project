# views.py
from django.shortcuts import render , get_object_or_404
from .models import *

def news_section(request):
    image_banner_news = ImageBannerNews.objects.first()
    news_items = News.objects.all()
    return render(request, 'news_section.html', {
                'news_items': news_items,
                'image_banner_news': image_banner_news,
            })



def news_details(request, slug):
    news_details_view = get_object_or_404(NewsDetails, slug=slug)
    return render(request, 'news/news_details.html', {
        'news_details_view': news_details_view,
        'image_banner_inside_page': news_details_view.image_banner_inside_page,
    })




def media_section(request):
    image_banner_media = ImageBannerMedia.objects.first()
    media_items = Media.objects.all()
    return render(request, 'media_section.html', {
        'media_items': media_items,
        'image_banner_media': image_banner_media,
        })



def media_details(request, slug):
    media_details_view = get_object_or_404(MediaDetails, slug=slug)
    return render(request, 'media/media_details.html', {
        'media_details_view': media_details_view,
        'image_banner_inside_page': media_details_view.image_banner_inside_page,
        
    })




