from django.shortcuts import render
from .models import About_Us, Image_Banner, Image_Banner_Brand


def get_first_object_with_prefetch(model, related_field):
    return model.objects.prefetch_related(related_field).first()

def about_us(request):
    about_section = get_first_object_with_prefetch(About_Us, 'process_cards')
    return render(request, 'about_us.html', {"about_section": about_section})

def board_of_directors(request):
    image_banner = get_first_object_with_prefetch(Image_Banner, 'process_image')
    return render(request, 'board_of_directors.html', {"image_banner": image_banner})

def our_brands(request):
    image_banner_brand = get_first_object_with_prefetch(Image_Banner_Brand, 'process_image')
    return render(request, 'our_brands.html', {"image_banner_brand": image_banner_brand})