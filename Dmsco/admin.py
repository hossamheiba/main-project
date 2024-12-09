from django.contrib import admin 
from .models import *
from modeltranslation.admin import  TranslationAdmin ,TranslationTabularInline ,TranslationStackedInline

# About_Us-----------------------------------
class About_UsInline(TranslationStackedInline):  
    model = Card
    extra = 1  
    
@admin.register(About_Us)
class About_UsAdmin(TranslationAdmin):
    # group_fieldsets = True  
    # readonly_fields = ['image_tag'] 
    # def has_add_permission(self, request):
    #     return False

    # def has_delete_permission(self, request, obj=None):
    #     return False
    inlines = [About_UsInline]
    list_display = ("Years_Of_Experienced","image_tag")
    list_filter = ('Years_Of_Experienced' ,)
    class Media:
        js = (
            'modeltranslation/js/jQuery.js',
            'modeltranslation/js/jQuery_UI.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        


# board_of_directors-------------------------------------------
class ImageBannerInline(TranslationStackedInline):  
    model = BoardMember
    extra = 1  

    
@admin.register(Image_Banner)
class BoardMemberAdmin(admin.ModelAdmin):
    inlines = [ImageBannerInline]
    list_display = ("image_tag" ,)
    
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
        
# Brands-------------------------------------------

class BannerInline(TranslationStackedInline):  
    model = Brands
    extra = 1  

@admin.register(Image_Banner_Brand)
class Image_Banner_BrandAdmin(admin.ModelAdmin):
    inlines = [BannerInline]
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
        