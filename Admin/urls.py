from django.contrib import admin
from django.urls import path,include
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin_login/', views.loginadmin, name='loginadmin'),
    path('<str:admin_name>/home/', login_required(views.Admin_Home), name='admin_home'),

    path('<str:admin_name>/registration/',  login_required(views.register_employee), name='Register_admin'),
    path('<str:admin_name>/myemployee/', login_required(views.Employee), name='employee'),
    # path('<str:admin_name>/myemployee/', login_required(views.Employee), name='employee'),

    path('<str:admin_name>/signout/', views.signout, name='signout'),
    # path("myadmin/<str:admin_name>/", include('Admin.urls')),


    # URL pattern for logout success
    path('logout_success/', views.logout_success, name='logout_success'),

    # path('<str:admin_name>/logout/', auth_views.LogoutView.as_view(next_page='logout_success'), name='logout'),

]
