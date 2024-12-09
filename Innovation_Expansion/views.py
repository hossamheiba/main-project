# views.py
from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404

def innovation_expansion_view(request):
    imagebannerinnovation = ImageBannerInnovation.objects.first()
    entries = InnovationExpansion.objects.all()
    return render(request, 'innovation.html', {
        'entries': entries,
        'imagebannerinnovation': imagebannerinnovation
        })




def innovation_expansion(request, slug):
    cardinnovation = get_object_or_404(InnovationMainPage, slug=slug)
    return render(request, 'innovation/pageinnovation.html', {
        'cardinnovation': cardinnovation,
        'image_banner_inside_page': cardinnovation.image_banner_inside_page,
    })



