from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf.urls import url
from users import views

app_name = 'users'
urlpatterns = [
    url(r'^index/', views.index,name='index'),
    url(r'^register/', views.register,name='register'),
    url(r'^login/', views.login,name='login'),
    url(r'^logout/', login_required(views.logout),name='logout')
]
