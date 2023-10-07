from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("myadmin/", include('Admin.urls')),
    path("myuser/",include('User.urls')),
    path("",include('frontpage.urls')),
]
