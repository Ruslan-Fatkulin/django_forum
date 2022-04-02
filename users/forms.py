from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .bulma_mixin import BulmaMixin


class SignUpForm(BulmaMixin, UserCreationForm):
    first_name = forms.CharField(label='Введите ваше имя')
    last_name = forms.CharField(label='Введите вашу фамилию')
    username = forms.CharField(label='Придумайте ник')
    email = forms.EmailField(label='Введите ваш email')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Придумайте пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Повторите пароль')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Введите ник')
    password = forms.CharField(widget=forms.PasswordInput(), label='Введите пароль')

    class Meta:
        model = User
        fields = ['username', 'password']


class EditProfileForm(BulmaMixin, forms.ModelForm):
    last_name = forms.CharField(label='Изменить фамилию')
    first_name = forms.CharField(label='Изменить имя')
    username = forms.CharField(label='Изменить ник')
    email = forms.EmailField(label='Изменить email')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ResetPasswordForm(BulmaMixin, PasswordChangeForm):
    old_password = forms.PasswordInput()
    new_password1 = forms.PasswordInput()
    new_password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
