from django import forms

from community.models import Question, Answer, Feedback


class AskQuestionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    text = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'textarea', 'size': '20'})
    )

    class Meta:
        model = Question
        fields = ['title', 'text']


class AnswerForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}),
                           label='leave your Answer here')

    class Meta:
        model = Answer
        fields = ['text']


class FeedbackForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}),
                           label='Опишите свою проблему')

    class Meta:
        model = Feedback
        fields = ['text']
