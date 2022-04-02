from django.shortcuts import render, redirect
from .models import *
from . import forms


def home(request):
    questions = Question.objects.all()
    return render(request, 'home.html', {'questions': questions})


def ask_question(request):
    form = forms.AskQuestionForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('community:home')
    form = forms.AskQuestionForm()
    return render(request, 'ask_question.html', {'form': form})


def answer(request, pk):
    question = Question.objects.get(pk=pk)
    answerr = Answer.objects.all()
    if request.method == "POST":
        form = forms.AnswerForm(data=request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.user = request.user
            new_answer.question = question
            new_answer.save()
            return redirect('community:question_detail', pk=pk)
    form = forms.AnswerForm()
    return render(request, 'answers.html', {'form': form, 'question': question, 'answerr': answerr})


def question_detail(request, pk):
    question = Question.objects.get(pk=pk)
    answers = Answer.objects.filter(question=pk)
    return render(request, 'question_detail.html', {'question': question, 'answers': answers})