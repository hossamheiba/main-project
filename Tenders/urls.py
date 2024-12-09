from django.urls import path
from . import views

app_name='Tenders'
urlpatterns = [
    path('', views.tenders_view, name='tenders'),
]
