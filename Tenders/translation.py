from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(TenderCategory)
class FeatureTranslationOptions(TranslationOptions):
    fields = ('tender_title',) 
    

@register(Tender)
class We_AldawaaTranslationOptions(TranslationOptions):
    fields = ('category_title', 'category_description', ) 
    