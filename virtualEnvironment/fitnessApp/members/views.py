from django.http import HttpResponse
from django.template import loader
import requests
from django.http import JsonResponse
from fatsecret import Fatsecret

    
def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm


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
                login(request, user)    
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

    # Test Calls w/o authentication

    print("\n\n ---- No Authentication Required ---- \n\n")

    foods = fs.foods_search("Tacos")
    print("Food Search Results: {}".format(len(foods)))
    print("{}\n".format(foods))

    food = fs.food_get("1345")
    print("Food Item 1345")
    print("{}\n".format(food))

    recipes = fs.recipes_search("Tomato Soup")
    print("Recipe Search Results:")
    print("{}\n".format(recipes))

    recipe = fs.recipe_get("88339")
    print("Recipe 88339")
    print("{}\n".format(recipe))

    # Test Calls with 3 Legged Oauth

    print("\n\n ------ OAuth Example ------ \n\n")

    print(fs.get_authorize_url())
    session_token = fs.authenticate(input("\nPIN: "))

    foods = fs.foods_get_most_eaten()
    print("Most Eaten Food Results: {}".format(len(foods)))

    recipes = fs.recipes_search("Enchiladas")
    print("Recipe Search Results: {}".format(len(recipes)))

    profile = fs.profile_get()
    print("Profile: {}".format(profile))

def food_search_results (request):
     return render(request, 'food_search_results.html')

