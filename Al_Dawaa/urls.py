from django.urls import path
from . import views

app_name="Al-Dawaa"

urlpatterns = [
    path("we_aldawaa/",views.we_aldawaa_view,name="we_aldawaa"),
    path('departments/', views.departments_view, name='departments'),
    path('departments/<slug:slug>/', views.department_detail, name='department_detail'),
    
    path("social_responsibility/",views.social_responsibility,name="social_responsibility"),
    path('social_responsibility/<slug:slug>/', views.social_responsibility_details, name='social_responsibility_details'),
    
    path('our_programs/', views.programs_view, name='our_programs'),
] 

