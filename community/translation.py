from modeltranslation.translator import translator, TranslationOptions
from .models import Question


class QuestionTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Question, QuestionTranslationOptions)
