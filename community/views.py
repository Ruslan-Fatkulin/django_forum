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
        instance.author = request.user
        instance.save()
        return redirect('community:home')
    form = forms.AskQuestionForm()
    return render(request, 'ask_question.html', {'form': form})


def answer(request, pk):
    question = Question.objects.get(pk=pk)
    answer = Answer.objects.filter(user=request.user)

    if request.method == "POST":
        form = forms.AnswerForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.user = request.user
            rating.question = question
            rating.save()
            return redirect('community:question_detail', pk=pk)
    form = forms.AnswerForm()
    return render(request, 'answers.html', {'form': form, 'question': question, 'answer': answer})


def question_detail(request, pk):
    question = Question.objects.get(pk=pk)
    answers = Answer.objects.filter(question=pk)
    return render(request, 'question_detail.html', {'question': question, 'answers': answers})


def delete_question(request, pk):
    question = Question.objects.get(pk=pk).delete()
    return redirect('community:home')


def feedback(request):
    form = forms.FeedbackForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('community:home')
    form = forms.FeedbackForm()
    return render(request, 'feedback.html', {'form': form})
