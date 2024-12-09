from django.shortcuts import render , get_object_or_404
from .models import Partner, Testimonial , Partner_Brands , ImageBannerStrategic

def partner_view(request):
    image_banner_strategic = ImageBannerStrategic.objects.first()
    testimonials = Testimonial.objects.all()
    partner_brands = Partner_Brands.objects.all()
    return render(request, 'testimonial.html', { 
        'testimonials': testimonials ,
        'partner_brands' : partner_brands,
        'image_banner_strategic' : image_banner_strategic,
        })




def partners_view(request , slug):
    partners = get_object_or_404(Partner, slug=slug)
    return render(request, 'details/partner_details.html', {
        'partners': partners,
        'image_banner_inside_page': partners.image_banner_inside_page,
        })



