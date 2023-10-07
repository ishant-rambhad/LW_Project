from django.shortcuts import render

# Create your views here.


def loginuser(request):
    return render(request,'admin/admin_login.html')