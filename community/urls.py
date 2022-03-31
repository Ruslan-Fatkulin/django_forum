from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.questions_page, name='questions_page'),
]