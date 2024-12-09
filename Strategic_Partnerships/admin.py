from django.contrib import admin 
from .models import *
from modeltranslation.admin import  TranslationAdmin ,TranslationTabularInline ,TranslationStackedInline




class PartnerInline(TranslationStackedInline):  
    model = Partner
    exclude = ('slug',)
    extra=1
    
class Partner_BrandsInline(admin.StackedInline):  
    model = Partner_Brands
    extra=1
    
class TestimonialInline(TranslationStackedInline):  
    model = Testimonial
    extra=1

@admin.register(ImageBannerStrategic)
class TestimonialAdmin(admin.ModelAdmin):
    
    inlines = [Partner_BrandsInline,TestimonialInline,PartnerInline]
    list_display = ("image_tag",)
    # def has_add_permission(self, request):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False
    class Media:
        js = (
            'modeltranslation/js/jQuery.js',
            'modeltranslation/js/jQuery_UI.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        
