from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from Home.views import home_section_view

urlpatterns = [
    path('i18n/', include ('django.conf.urls.i18n'))
]

urlpatterns += i18n_patterns(       
    path('admin/', admin.site.urls ),
    path('', home_section_view , name='home'),
    path('Dmsco/', include('Dmsco.urls') ),
    path('Al-Dawaa/', include('Al_Dawaa.urls') ),
    path('innovations/', include('Innovation_Expansion.urls') ),
    path('tenders/', include('Tenders.urls') ),
    path('strategic/', include('Strategic_Partnerships.urls') ),
    path('news/', include('News_Media.urls') ),
    path('Contact_Us/', include('Contact_Us.urls') ),
    
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)