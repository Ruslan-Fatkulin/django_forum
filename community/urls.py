from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('ask_question/', views.ask_question, name='ask_question'),
    path('answer/<int:pk>', views.answer, name='answer'),
    path('question_detail/<int:pk>', views.question_detail, name='question_detail'),
    path('delete_question/<int:pk>', views.delete_question, name='delete_question'),
    path('feedback/', views.feedback, name='feedback')
]
