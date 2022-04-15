from django import forms
from .bulma_mixin import BulmaMixin

from community.models import Question, Answer, Feedback, Category


class AskQuestionForm(BulmaMixin, forms.ModelForm):
    title = forms.CharField(label='Ask Your Question')
    description = forms.CharField(label='ok')
    category = forms.ChoiceField(label='Choose Category')

    class Meta:
        model = Question
        fields = ['title', 'description', 'category']


class AnswerForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}),
                           label='leave your Answer here')
    code = forms.CharField(widget=forms.Textarea(attrs={'class': 'text'}),
                           label='Enter your code')

    class Meta:
        model = Answer
        fields = ['text', 'code']


class FeedbackForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}),
                           label='Опишите свою проблему')

    class Meta:
        model = Feedback
        fields = ['text']
