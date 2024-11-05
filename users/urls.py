from django.urls import path
from . import views

urlpatterns = [
    path('register', views.index),
    path('login', views.login),
    path('users/new', views.new),
    path('users.', views.users_),
    path('' , views.blogs)
]