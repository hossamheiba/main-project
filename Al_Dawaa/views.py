from django.shortcuts import render, get_object_or_404
from .models import (
    We_Aldawaa, ImageBannerDepartment, AlDawaaDepartmentCard, Department_Inside_Page,
    Social_Responsibility, Card_Social_Responsibility, Social_Responsibility_details,
    Image_Banner_Program
)

def get_first_object_with_prefetch(model, related_field):
    return model.objects.prefetch_related(related_field).first()

# We_Aldawaa
def we_aldawaa_view(request):
    aldawaa = get_first_object_with_prefetch(We_Aldawaa, 'process_icon')
    return render(request, 'we_aldawaa.html', {"aldawaa": aldawaa})

# Departments
def departments_view(request):
    image_banner_department = ImageBannerDepartment.objects.first()
    departments = AlDawaaDepartmentCard.objects.prefetch_related('department').all()
    return render(request, 'Al_Dawaa_Departments.html', {
        'departments': departments,
        'image_banner_department': image_banner_department
    })

def department_detail(request, slug):
    department = get_object_or_404(Department_Inside_Page, slug=slug)
    departments = Department_Inside_Page.objects.all()
    return render(request, 'department/department.html', {
        'department': department,
        'departments': departments,
        'image_banner_inside_page': department.image_banner_inside_page,
    })

# Social Responsibility
def social_responsibility(request):
    page_social_responsibility = Social_Responsibility.objects.first()
    card_social_responsibility = Card_Social_Responsibility.objects.prefetch_related('social_responsibility_details').all()
    return render(request, 'Social_Responsibility.html', {
        "page_social_responsibility": page_social_responsibility,
        "card_social_responsibility": card_social_responsibility,
    })

def social_responsibility_details(request, slug):
    details_social_responsibility = get_object_or_404(Social_Responsibility_details, slug=slug)
    return render(request, 'Social_Responsibility/Social_Responsibility_details.html', {
        "details_social_responsibility": details_social_responsibility,
        "image_banner": details_social_responsibility.image_banner,
    })

# Programs
def programs_view(request):
    image_banner_program = get_first_object_with_prefetch(Image_Banner_Program, 'process_image')
    return render(request, 'our_program.html', {"image_banner_program": image_banner_program})
