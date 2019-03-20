'''Urls for the LoginFolio app'''
from django.conf.urls import url
from django.urls import path, re_path
from . import views as LoginFolio_views

urlpatterns = [
    path('', LoginFolio_views.home, name='home'),
    path('login', LoginFolio_views.login_user, name='login'),
    path('home', LoginFolio_views.home, name='home'),
    path('about', LoginFolio_views.about, name='about'),
    path('team', LoginFolio_views.team, name='team'),
    path('logout', LoginFolio_views.logout_user, name='logout'),
    path('register', LoginFolio_views.register_user, name='register')
]
