
# views.py
from django.shortcuts import render
from .models import HomePgae

def home_section_view(request):
    homepgae = HomePgae.objects.first()  
    return render(request, 'home.html', {'homepgae': homepgae})

