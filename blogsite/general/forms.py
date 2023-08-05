from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email')




class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'password')



class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ('author',)
        fields = ('title', 'content', 'image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']