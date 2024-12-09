from modeltranslation.translator import register, TranslationOptions
from .models import About_Us , Card , BoardMember , Brands

@register(About_Us)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('description',) 
    
@register(Card)
class CardTranslationOptions(TranslationOptions):
    fields = ('title_card','description_card' ,'collapse_description' ) 
    
@register(BoardMember)
class CardTranslationOptions(TranslationOptions):
    fields = ('person_name','person_position',) 
    
@register(Brands)
class CardTranslationOptions(TranslationOptions):
    fields = ('brand_name',) 
