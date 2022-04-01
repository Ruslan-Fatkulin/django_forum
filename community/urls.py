from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('ask_question/', views.ask_question, name='ask_question')
]