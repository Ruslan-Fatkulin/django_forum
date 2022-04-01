from django.shortcuts import render, redirect
from .models import *
from .forms import AskQuestionForm


def home(request):
    questions = Question.objects.all()
    return render(request, 'questions_page.html', {'questions': questions})


def questions(request):
    questions = Question.objects.all()
    return render(request, 'questions.html', {'questions': questions})


def ask_question(request):
    form = AskQuestionForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return redirect('community:home')
    form = AskQuestionForm()
    return render(request, 'ask_question.html', {'form': form})
