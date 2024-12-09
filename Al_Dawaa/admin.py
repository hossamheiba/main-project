from django.contrib import admin 
from .models import *
from modeltranslation.admin import  TranslationAdmin ,TranslationTabularInline ,TranslationStackedInline

# We_Aldawaa-----------------------------------------------
class FeatureInline(TranslationStackedInline):  
    model = Feature
    extra = 1
    
class TimelineEventInline(TranslationStackedInline):  
    model = TimelineEvent
    extra = 1
    
@admin.register(We_Aldawaa)
class We_AldawaaAdmin(TranslationAdmin):    
    inlines = [FeatureInline , TimelineEventInline]
    list_display = ("section_title",'image_tag')
    list_filter = ('section_title',)
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
        


# Departmens-----------------------------------------------


class DepartmentCategoryInline(TranslationStackedInline):
    model = AlDawaaDepartmentCard
    extra = 1
    
class DepartmentInline(TranslationStackedInline):
    model = Department_Inside_Page
    exclude = ('slug',)
    extra = 1
    

@admin.register(ImageBannerDepartment)
class DepartmentsAdmin(admin.ModelAdmin):
    inlines = [DepartmentCategoryInline , DepartmentInline]
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
        
        



# Social_Responsibility-----------------------------------------------
class Details_Social_ResponsibilityInline(TranslationStackedInline):  
    model = Social_Responsibility_details
    exclude = ('slug',)
    extra = 1
    
class Card_Social_ResponsibilityInline(TranslationStackedInline):  
    model = Card_Social_Responsibility
    extra = 1

@admin.register(Social_Responsibility)
class Social_ResponsibilityAdmin(TranslationAdmin):
    inlines = [Card_Social_ResponsibilityInline , Details_Social_ResponsibilityInline]
    list_display = ("page_title", 'image_tag')
    list_filter = ("page_title",)
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
        
        
        
        

# Programs-----------------------------------------------
class Image_Banner_ProgramInline(TranslationStackedInline):  
    model = Program
    extra= 1
    
@admin.register(Image_Banner_Program)
class ProgramAdmin(admin.ModelAdmin):
    inlines = [Image_Banner_ProgramInline]
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
        
        