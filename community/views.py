from django.shortcuts import render
from .models import *


def questions_page(request):
    questions = Question.objects.all()
    return render(request, 'questions_page.html', {'questions': questions})
