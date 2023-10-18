from django.contrib.auth.models import AbstractUser, Group, Permission
from djongo import models  # Import the models module
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    # Your custom fields and methods here

    # Add related_name to groups and user_permissions
    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='customuser_set'
    )



class Employee(models.Model):
    empid = models.CharField(max_length=255)
    empname = models.CharField(max_length=255)
    empgender = models.CharField(max_length=10, choices=[("male", "Male"), ("female", "Female"), ("other", "Other")])
    empcontactno = models.CharField(max_length=15)
    emergencycontact = models.CharField(max_length=15)
    empemail = models.EmailField(max_length=255)
    empaddress = models.TextField()
    empdob = models.DateField()
    emppassword1 = models.CharField(max_length=255)
    emppassword2 = models.CharField(max_length=255)
    empdesignation = models.CharField(max_length=255, choices=[("admin", "Admin"), ("user", "User")])
    emptype = models.CharField(max_length=255, choices=[("part-time", "Part Time"), ("full-time", "Full Time"), ("freelancer", "Freelancer")])
    empjoiningDate = models.DateField()
    empgridcheck1 = models.BooleanField(default=False)
