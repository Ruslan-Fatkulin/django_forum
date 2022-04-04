from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True, max_length=3000)

    def __str__(self):
        return f'{self.user} -> {self.question.author}'


class Feedback(models.Model):
    text = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f'{self.user} - {self.text[:20]}'
