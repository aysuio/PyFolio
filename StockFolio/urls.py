'''Urls for the StockFolio app'''
from django.conf.urls import url
from django.urls import path
from . import views as StockFolio_views

urlpatterns = [
    path('portfolio', StockFolio_views.portfolio, name="portfolio")
]
