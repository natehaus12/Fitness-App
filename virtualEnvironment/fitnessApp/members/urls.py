from django.urls import path
from . import views
from .views import user_profile

urlpatterns = [
    path('members/', views.members, name='members'),
    path('index/', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path ('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),

    path('food_search/', views.food_search, name='food_search'),
    path('user_profile/', views.user_profile, name='user_profile'),
    # path('food_search_results/', views.food_search_results, name='food_search_results'),

]