from django.http import HttpResponse
from django.template import loader
import requests
from django.http import JsonResponse
from . import forms
from fatsecret import Fatsecret
from . import models
from django.shortcuts import render, get_object_or_404

    
def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm, SearchForm


# Create your views here.
# Home page
def index(request):
    return render(request, 'index.html')

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:  
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

def food_search (request):

    consumer_key = '434d43581c294b6587358f705f6247db'
    consumer_secret = '2df0aec6cece4d81b8ba010f1c349320'

    fs = Fatsecret(consumer_key, consumer_secret)


    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            food_name = form.cleaned_data['food_name']
            foods = fs.foods_search(str(food_name))
            food_description = format(len(foods))
            food_description2 = format(foods)
         
            
            return render(request, 'food_search_results.html', {
                    'food_name': str(food_name),
                    'description': str(food_description),
                    'description2': str(food_description2)
                })


        
    else:
        form = SearchForm()

       
    return render(request, 'food_search.html', { 'form': form} )


# def food_search_results (food_name):

     
#     consumer_key = '434d43581c294b6587358f705f6247db'
#     consumer_secret = '2df0aec6cece4d81b8ba010f1c349320'

#     fs = Fatsecret(consumer_key, consumer_secret)

#     # Test Calls w/o authentication

#     print("\n\n ---- No Authentication Required ---- \n\n")

#     foods = fs.foods_search("Tacos")
#     print("Food Search Results: {}".format(len(foods)))
#     print("{}\n".format(foods))
#     return render(food_name, 'food_search_results.html')



