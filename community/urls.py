from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('questions/', views.questions, name='questions'),
    path('ask_question/', views.ask_question, name='ask_question')
]