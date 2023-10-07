from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Employee

class EmployeeRegistrationForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Employee
        fields = ('empid', 'empname', 'empgender', 'empcontactno', 'emergencycontact', 'empemail', 'empaddress',
                  'empdob', 'emppassword', 'empdesignation', 'emptype', 'empjoiningDate')
        widgets = {
            'emppassword': forms.PasswordInput(),
        }

    def clean_password(self):
        # Always return the initial password value
        return self.initial.get('password')
