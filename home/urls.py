from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [

     path('', views.home, name='home'),
     path('get_all_exchange_data/', views.get_all_exchange_data, name='get_all_exchange_data'),
     # path('login', views.login_page, name='login'),
     # path('user_login', views.user_login, name='user_login'),
     # path('user_login_page', views.user_login_page, name='user_login_page'),

     # path('register_user/', views.register_user, name='register_user'),
     # path('verify_otp/<int:user_id>/', views.verify_otp, name='verify_otp'),
     # path('authenticated_home', views.authenticated_home, name='authenticated_home'),
     # path('logout/', views.logout_view, name='logout'),



]
