from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
import requests
from django.http import JsonResponse
from . import forms
from fatsecret import Fatsecret
from . import models
from django.shortcuts import render, redirect
from .forms import UpdateUserForm, UpdateProfileForm
from .models import Profile
from django.views import View
from django.contrib.auth.decorators import login_required

    
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


    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():

            food_name = form.cleaned_data['food_name']
            foods = fs.foods_search(food_name)

            food_label = foods[0].get("food_name")
            food_description = foods[0].get("food_description")
            food_id = foods[0].get("food_id")
            calories = fs.food_get(food_id)

            if type(calories.get("servings").get("serving")) is dict:

                food_calories = calories.get("servings").get("serving").get("calories")
                food_protein = calories.get("servings").get("serving").get("protein")
                food_carbs = calories.get("servings").get("serving").get("carbohydrate")
                food_fat = calories.get("servings").get("serving").get("fat")
            else:
                food_calories = calories.get("servings").get("serving")[1].get("calories")
                food_protein = calories.get("servings").get("serving")[1].get("protein")
                food_carbs = calories.get("servings").get("serving")[1].get("carbohydrate")
                food_fat = calories.get("servings").get("serving")[1].get("fat")


         


            food_label2 = foods[1].get("food_name")
            food_description2 = foods[1].get("food_description")
            food_id2 = foods[1].get("food_id")
            calories2 = fs.food_get(food_id2)

            if type(calories2.get("servings").get("serving")) is dict:

                food_calories2 = calories2.get("servings").get("serving").get("calories")
                food_protein2 = calories2.get("servings").get("serving").get("protein")
                food_carbs2 = calories2.get("servings").get("serving").get("carbohydrate")
                food_fat2 = calories2.get("servings").get("serving").get("fat")
            else:
                food_calories2 = calories2.get("servings").get("serving")[1].get("calories")
                food_protein2 = calories2.get("servings").get("serving")[1].get("protein")
                food_carbs2 = calories2.get("servings").get("serving")[1].get("carbohydrate")
                food_fat2 = calories2.get("servings").get("serving")[1].get("fat")



            food_label3 = foods[2].get("food_name")
            food_description3 = foods[2].get("food_description")
            food_id3 = foods[2].get("food_id")
            calories3 = fs.food_get(food_id3)

            if type(calories3.get("servings").get("serving")) is dict:

                food_calories3 = calories3.get("servings").get("serving").get("calories")
                food_protein3 = calories3.get("servings").get("serving").get("protein")
                food_carbs3 = calories3.get("servings").get("serving").get("carbohydrate")
                food_fat3 = calories3.get("servings").get("serving").get("fat")
            else:
                food_calories3 = calories3.get("servings").get("serving")[1].get("calories")
                food_protein3 = calories3.get("servings").get("serving")[1].get("protein")
                food_carbs3 = calories3.get("servings").get("serving")[1].get("carbohydrate")
                food_fat3 = calories3.get("servings").get("serving")[1].get("fat")

            food_label4 = foods[3].get("food_name")
            food_description4 = foods[3].get("food_description")
            food_id4 = foods[3].get("food_id")
            calories4 = fs.food_get(food_id4)

            if type(calories4.get("servings").get("serving")) is dict:

                food_calories4 = calories4.get("servings").get("serving").get("calories")
                food_protein4 = calories4.get("servings").get("serving").get("protein")
                food_carbs4 = calories4.get("servings").get("serving").get("carbohydrate")
                food_fat4 = calories4.get("servings").get("serving").get("fat")
            else:
                food_calories4 = calories4.get("servings").get("serving")[1].get("calories")
                food_protein4 = calories4.get("servings").get("serving")[1].get("protein")
                food_carbs4 = calories4.get("servings").get("serving")[1].get("carbohydrate")
                food_fat4 = calories4.get("servings").get("serving")[1].get("fat")


            food_label5 = foods[4].get("food_name")
            food_description5 = foods[4].get("food_description")
            food_id5 = foods[4].get("food_id")
            calories5 = fs.food_get(food_id5)

            if type(calories5.get("servings").get("serving")) is dict:

                food_calories5 = calories5.get("servings").get("serving").get("calories")
                food_protein5 = calories5.get("servings").get("serving").get("protein")
                food_carbs5 = calories5.get("servings").get("serving").get("carbohydrate")
                food_fat5 = calories5.get("servings").get("serving").get("fat")
            else:
                food_calories5 = calories5.get("servings").get("serving")[1].get("calories")
                food_protein5 = calories5.get("servings").get("serving")[1].get("protein")
                food_carbs5 = calories5.get("servings").get("serving")[1].get("carbohydrate")
                food_fat5 = calories5.get("servings").get("serving")[1].get("fat")
            
            return render(request, 'food_search_results.html', {
                    'food_name': str(food_name),

                    'food_label': str(food_label),
                    'description': str(food_description),
                    "food_calories" : str(food_calories),
                    "food_protein" : str(food_protein),
                    "food_carbs" : str(food_carbs),
                    "food_fat" : str(food_fat),



                    'food_label2': str(food_label2),
                    'description2': str(food_description2),
                    "food_calories2" : str(food_calories2),
                    "food_protein2" : str(food_protein2),
                    "food_carbs2" : str(food_carbs2),
                    "food_fat2" : str(food_fat2),

                    
                    'food_label3': str(food_label3),
                    'description3': str(food_description3),
                    "food_calories3" : str(food_calories3),
                     "food_protein3" : str(food_protein3),
                    "food_carbs3" : str(food_carbs3),
                    "food_fat3" : str(food_fat3),

                    
                    'food_label4': str(food_label4),
                    'description4': str(food_description4),
                    "food_calories4" : str(food_calories4),
                    "food_protein4" : str(food_protein4),
                    "food_carbs4" : str(food_carbs4),
                    "food_fat4" : str(food_fat4),


                    
                    'food_label5': str(food_label5),
                    'description5': str(food_description5),
                    "food_calories5" : str(food_calories5),
                    "food_protein5" : str(food_protein5),
                    "food_carbs5" : str(food_carbs5),
                    "food_fat5" : str(food_fat5),
                })


        
    else:
        form = SearchForm()

       
    return render(request, 'food_search.html', { 'form': form} )

@login_required
def user_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='user_profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'user_profile.html', {'user_form': user_form, 'profile_form': profile_form})

