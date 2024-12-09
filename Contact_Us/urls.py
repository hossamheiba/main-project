from django.urls import path
from . import views

app_name="Contact_Us"

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
]
