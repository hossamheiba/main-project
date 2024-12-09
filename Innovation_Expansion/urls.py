# urls.py
from django.urls import path
from . import views

app_name="innovations"

urlpatterns = [
    path('', views.innovation_expansion_view, name='innovation_expansion_view'),
    path('<slug:slug>/', views.innovation_expansion, name='innovation_expansion'),
]
