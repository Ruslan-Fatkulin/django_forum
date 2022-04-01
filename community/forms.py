from django import forms

from community.models import Question


class AskQuestionForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    text = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'textarea', 'size': '40'})
    )

    class Meta:
        model = Question
        fields = ['title', 'text']
