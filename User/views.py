from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
# Create your views here.


def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        context={
            "user_name": username
        }

        if user is not None:
            # Authentication successful, log the user in.
            login(request, user)
            return redirect('User_Home', user_name=username)
        else:
            # Authentication failed, display an error message.
            error_message = "Invalid username or password. Please try again."
            return render(request, 'user/login_error.html', {'error_message': error_message})

    # If it's not a POST request or if authentication fails, show the login form.
    return render(request, 'user/user_login.html')

@login_required
def User_Home(request, user_name):
    context = {"user_name": user_name}  # Create a dictionary with the admin_name variable
    return render(request, 'user/userdash.html', context)


@login_required
def User_addbatch(request, user_name):
    context = {"user_name": user_name}
    return render(request, 'user/add_batch.html', context)


@login_required
def User_viewbatch(request, user_name):
    context = {"user_name": user_name}
    return render(request, 'user/viewbatch.html', context)

@login_required
def signout(request,user_name):
    # Log the user out using Django's built-in logout function.
    logout(request)
    # Redirect to a page to display a logout success message.
    return redirect('logout_successful')

# You can use the built-in LogoutView for the success message.
logout_successful = LogoutView.as_view(
    template_name='user/logout_success.html',
    next_page='loginuser'  # Redirect to the login page after logout.
)