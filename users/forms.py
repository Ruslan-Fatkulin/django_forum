from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .bulma_mixin import BulmaMixin


class SignUpForm(BulmaMixin, UserCreationForm):
    first_name = forms.CharField(label='Enter Your Name')
    username = forms.CharField(label='Create Any Username')
    email = forms.EmailField(label='Enter Your Email')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Create Any Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Repeat Password')

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2')


class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Enter your username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Enter your password')

    class Meta:
        model = User
        fields = ['username', 'password']


class EditProfileForm(BulmaMixin, forms.ModelForm):
    first_name = forms.CharField(label='Change name')
    username = forms.CharField(label='Change username')
    email = forms.EmailField(label='Change email')

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email']


class ResetPasswordForm(BulmaMixin, PasswordChangeForm):
    old_password = forms.PasswordInput()
    new_password1 = forms.PasswordInput()
    new_password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
