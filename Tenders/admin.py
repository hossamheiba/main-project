from django.contrib import admin 
from .models import *
from modeltranslation.admin import  TranslationAdmin ,TranslationTabularInline ,TranslationStackedInline

class TenderInline(TranslationStackedInline):
    model = Tender
    extra = 1 

class TenderCategoryInline(TranslationStackedInline):
    model = TenderCategory
    extra = 1

@admin.register(Image_Banner_Tender)
class TenderAdmin(admin.ModelAdmin):
    inlines = [TenderCategoryInline , TenderInline]
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
