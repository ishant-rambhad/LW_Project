from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path("user_login/", views.loginuser, name='loginuser'),
    path('<str:user_name>/home/', login_required(views.User_Home), name='User_Home'),
    path('<str:user_name>/addbatch/', login_required(views.User_addbatch), name='User_addbatch'),
    path('<str:user_name>/viewbatch/', login_required(views.User_viewbatch), name='User_viewbatch'),
    path('<str:user_name>/signout/', views.signout, name='signout'),
    path('logout_success/', views.logout_success, name='logout_success'),

]