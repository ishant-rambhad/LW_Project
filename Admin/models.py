from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models  # Import the models module
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
    empid = models.CharField(max_length=20)
    empname = models.CharField(max_length=100)
    empgender = models.CharField(max_length=10)
    empcontactno = models.CharField(max_length=15)
    emergencycontact = models.CharField(max_length=15)
    empemail = models.EmailField(max_length=100)
    empaddress = models.TextField()
    empdob = models.DateField()
    emppassword = models.CharField(max_length=128)
    empdesignation = models.CharField(max_length=20)
    emptype = models.CharField(max_length=20)
    empjoiningDate = models.DateField()

    class Meta:
        db_table = 'ishantcollection'