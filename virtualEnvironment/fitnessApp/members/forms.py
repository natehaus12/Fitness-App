from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from .models import Profile

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class SearchForm(forms.ModelForm):
    class Meta:
        model = models.Food
        fields = ['food_name']

        
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    first_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class UpdateProfileForm(forms.ModelForm):

    height = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))   
    weight = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))                                               
    goal = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['height', 'weight', 'goal']