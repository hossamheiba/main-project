from django.urls import path
from . import views

app_name = "Dmsco"

urlpatterns = [
    path("about_us/",views.about_us,name="about_us"),
    path('board-of-directors/', views.board_of_directors, name='board_of_directors'),
    path('our-brands/', views.our_brands, name='our_brands'),
] 


