from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('news_title', 'news_description', ) 
    
@register(NewsDetails)
class NewsDetailsTranslationOptions(TranslationOptions):
    fields = ('news_page_title', 'news_page_description',) 
    
    
@register(Media)
class NewsTranslationOptions(TranslationOptions):
    fields = ('media_title', 'media_description', ) 
    
@register(MediaDetails)
class NewsDetailsTranslationOptions(TranslationOptions):
    fields = ('media_page_title', 'media_page_description',) 
    
