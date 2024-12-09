from modeltranslation.translator import register, TranslationOptions
from .models import *


# We_Aldawaa-----------------------------------------------
@register(ContactInfo)
class We_AldawaaTranslationOptions(TranslationOptions):
    fields = ('card_title', 'pragraph_link' , 'address_title' ) 
