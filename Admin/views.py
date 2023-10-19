from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
# from .forms import EmployeeRegistrationForm
from .forms import Employee  # Import your new form
# from .models import EmployeeMongo
from .forms import EmployeeForm
from django.contrib import messages




def Login(request):
    return render(request, 'admin/admin_login.html')


def loginadmin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        context={
            "admin_name": username
        }

        if user is not None:
            # Authentication successful, log the user in.
            login(request, user)
            return redirect('admin_home', admin_name=username)
        else:
            # Authentication failed, display an error message.
            error_message = "Invalid username or password. Please try again."
            return render(request, 'admin/login_error.html', {'error_message': error_message})

    # If it's not a POST request or if authentication fails, show the login form.
    return render(request, 'admin/admin_login.html')

@login_required
def Admin_Home(request, admin_name):
    context = {"admin_name": admin_name}  # Create a dictionary with the admin_name variable
    return render(request, 'admin/AdminHome.html', context)


@login_required
def emp_register(request, admin_name):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Check if the entered password and password confirmation match
            password1 = form.cleaned_data['emppassword1']
            password2 = form.cleaned_data['emppassword2']
            if password1 == password2:
                # Passwords match, proceed to save
                employee = form.save(commit=False)
                # Hash the password using make_password
                employee.emppassword1 = make_password(password1)
                employee.emppassword2 = make_password(password2)
                employee.save()
                # You can add a success message or redirect to a different page upon successful registration.
                messages.success(request, 'Employee registration successful!')
                return redirect('employee', admin_name=admin_name) # Replace 'success_page' with the name of your success page URL.
            else:
                # Passwords do not match, display an error message
                messages.error(request, 'Passwords do not match. Please try again.')

    else:
        form = EmployeeForm()

    context = {
        "admin_name" : admin_name,
        'form': form,
    }
    print("3")
    return render(request, 'admin/emp_register.html', context)

@login_required
def Employee(request,admin_name):
    context = {"admin_name": admin_name}  # Create a dictionary with the admin_name variable
    return render(request, 'admin/myemployee.html', context)

def logout_success(request):
    return render(request, 'logout_success.html')



@login_required
def signout(request,admin_name):
    # Log the user out using Django's built-in logout function.
    logout(request)
    # Redirect to a page to display a logout success message.
    return redirect('logout_success')

# You can use the built-in LogoutView for the success message.
logout_success = LogoutView.as_view(
    template_name='admin/logout_success.html',
    next_page='loginadmin'  # Redirect to the login page after logout.
)


