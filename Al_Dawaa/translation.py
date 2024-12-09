from modeltranslation.translator import register, TranslationOptions
from .models import *


# We_Aldawaa-----------------------------------------------
@register(We_Aldawaa)
class We_AldawaaTranslationOptions(TranslationOptions):
    fields = ('section_title', 'section_description', ) 
    
@register(Feature)
class FeatureTranslationOptions(TranslationOptions):
    fields = ('feature_title',) 
    
    
@register(TimelineEvent)
class TimelineEventTranslationOptions(TranslationOptions):
    fields = ('Time_line_description',) 
    
    
# Departmens-----------------------------------------------    
@register(AlDawaaDepartmentCard)
class DepartmentsTranslationOptions(TranslationOptions):
    fields = ('department_title','department_description') 
    
    
@register(Department_Inside_Page)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('section_title', 'section_description') 
    
    
    
# Social_Responsibility--------------------------------------------    
@register(Social_Responsibility)
class Card_Social_ResponsibilityTranslationOptions(TranslationOptions):
    fields = ('page_title','page_description',) 
    
@register(Card_Social_Responsibility)
class Card_Social_ResponsibilityTranslationOptions(TranslationOptions):
    fields = ('card_title','card_description',) 
    
@register(Social_Responsibility_details)
class Details_Social_ResponsibilityTranslationOptions(TranslationOptions):
    fields = ('title_details_social','description_details_social',) 
    
    
    
# Programs-----------------------------------------------    
@register(Program)
class ProgramTranslationOptions(TranslationOptions):
    fields = ('program_title','program_description',) 
    
