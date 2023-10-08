from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from .forms import EmployeeRegistrationForm
from .forms import Employee  # Import your new form
# from .models import EmployeeMongo




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
def Register_admin(request,admin_name):
    context = {"admin_name": admin_name}  # Create a dictionary with the admin_name variable
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



# def register_employee(request, admin_name):
#     if request.method == 'POST':
#         form = Employee(request.POST)
#         if form.is_valid():
#             # Create a new EmployeeMongo instance and save it
#             employee = form.save(commit=False)
#             employee.save()
#             return redirect('employee', admin_name=admin_name)
#     else:
#         form = Employee()
#     return render(request, 'myemployee.html', {'form': form, 'admin_name': admin_name})


def register_employee(request, admin_name):
    if request.method == 'POST':
        print("4")
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            # Create an Employee instance from the form data
            employee = Employee(
                empid=form.cleaned_data['empid'],
                empname=form.cleaned_data['empname'],
                empgender=form.cleaned_data['empgender'],
                empcontactno=form.cleaned_data['empcontactno'],
                empemail = form.cleaned_data['empemail'],
                empaddress = form.cleaned_data['empaddress'],
                empdob =  form.cleaned_data['empdob'],
                emppassword =  form.cleaned_data['emppassword'],
                empdesignation = form.cleaned_data['empdesignation'],
                emptype =  form.cleaned_data['emptype'],
                empjoiningDate = form.cleaned_data['empjoiningDate'],
            )
            # Save the Employee instance to MongoDB
            employee.save()
            print("12")

            # Redirect to a success page or perform other actions
            return redirect('employee')
    else:
        print("2")
        form = EmployeeRegistrationForm()

    context = {
        "admin_name" :admin_name,
        'form': form,
    }
    print("3")
    return render(request, 'admin/emp_register.html', context)