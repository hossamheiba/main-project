from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(InnovationExpansion)
class We_AldawaaTranslationOptions(TranslationOptions):
    fields = ('innovation_title', 'innovation_description', ) 
    
@register(InnovationMainPage)
class FeatureTranslationOptions(TranslationOptions):
    fields = ('detsils_innovation_title', 'detsils_innovation_description',) 
    
