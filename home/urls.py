from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [

     path('', views.home, name='home'),
     path('get_all_exchange_data/', views.get_all_exchange_data, name='get_all_exchange_data'),


]
