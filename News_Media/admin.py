from django.contrib import admin 
from .models import *
from modeltranslation.admin import  TranslationAdmin ,TranslationTabularInline ,TranslationStackedInline



class NewsDetailsInline(TranslationStackedInline):
    model = NewsDetails
    exclude = ('slug',)
    extra = 1



class NewsInline(TranslationStackedInline):
    model = News
    extra = 0


@admin.register(ImageBannerNews)
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsInline , NewsDetailsInline]
    list_display = ('image_tag' ,)
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
        
        
        

# Media-------------------------------
class MediatailsInline(TranslationStackedInline):
    model = MediaDetails
    exclude = ('slug',)
    extra = 1

class MediaInline(TranslationStackedInline):
    model = Media
    extra = 1


@admin.register(ImageBannerMedia)
class MediasAdmin(admin.ModelAdmin):
    inlines = [MediaInline,MediatailsInline]
    list_display = ('image_tag',)
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
        
        
        

