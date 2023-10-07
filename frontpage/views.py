from django.shortcuts import render

# Create your views here.
def FrontPage(request):
    return render(request,"frontpage.html")