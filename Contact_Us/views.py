from django.shortcuts import render, redirect
from .models import ContactInfo, ContactFormSubmission , Image_Banner
from django.contrib import messages


def contact_us(request):
    image_banner = Image_Banner.objects.first()
    contact_info = ContactInfo.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        message = request.POST.get('message')
        
        ContactFormSubmission.objects.create(name=name, email=email, phone=phone, message=message)
        
        messages.success(request, "Your message has been sent successfully!")
        
        return redirect('/Contact_Us')
    return render(request, 'contact_us.html', {
        'contact_info': contact_info,
        'image_banner': image_banner,
        })  