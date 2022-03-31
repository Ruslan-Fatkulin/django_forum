from django.shortcuts import render
from .models import *


def questions_page(request):
    questions = Question.objects.all()
    return render(request, 'questions_page.html', {'questions': questions}git remote add origin https://github.com/neruslvn/django4.git)
