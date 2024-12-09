from django.shortcuts import render
from .models import TenderCategory , Image_Banner_Tender

def tenders_view(request):
    image_banner_tender = Image_Banner_Tender.objects.first()
    categories = TenderCategory.objects.prefetch_related('tenders').all()
    return render(request, 'tenders_section.html', {
        'categories': categories,
        'image_banner_tender': image_banner_tender,
        })
