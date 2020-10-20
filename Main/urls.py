from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.urls import path
from Main import views

app_name = 'main'
urlpatterns = [
    url(r'^canteen_traffic/', views.main_page,name='canteen_traffic'),
    url(r'^canteen_principal/', views.canteen_principal,name='canteen_principal'),
    url(r'^CD/', views.consumption_data,name='CD'),
    url(r'^TA/', views.meals_average, name='TA'),
    url(r'^foodie/', views.foodie_resturant,name='foodie'),
    path('index/',login_required(views.main_page),name='index'),
]