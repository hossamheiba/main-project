from modeltranslation.translator import register, TranslationOptions
from .models import *


    
@register(Testimonial)
class FeatureTranslationOptions(TranslationOptions):
    fields = ('partner_title', 'partner_content') 

@register(Partner)
class We_AldawaaTranslationOptions(TranslationOptions):
    fields = ('partner_title', 'partner_description', 'first_person_name','first_person_position', 'second_person_name','second_person_position' ) 