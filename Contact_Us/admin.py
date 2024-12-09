from django.contrib import admin
from .models import *
from modeltranslation.admin import  TranslationAdmin ,TranslationTabularInline ,TranslationStackedInline




class ContactInfoInline(TranslationStackedInline):  
    model = ContactInfo
    extra = 1
    
@admin.register(Image_Banner)
class ContactInfoAdmin(admin.ModelAdmin):
    inlines = [ContactInfoInline]
    list_display = ('image_tag',)

    class Media:
        js = (
            'modeltranslation/js/jQuery.js',
            'modeltranslation/js/jQuery_UI.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
        



@admin.register(ContactFormSubmission)
class ContactFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at')
    readonly_fields = ('name', 'email', 'phone', 'message', 'submitted_at')
    
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False  
    
    def has_delete_permission(self, request, obj=None): 
        return False  
