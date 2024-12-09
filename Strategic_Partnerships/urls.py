from django.urls import path
from .views import *


app_name='Strategic'
urlpatterns = [
    path('', partner_view, name='partner'),
    path('<slug:slug>/', partners_view, name='partners'),
]
