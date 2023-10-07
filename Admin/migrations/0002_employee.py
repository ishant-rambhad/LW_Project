# Generated by Django 4.1.11 on 2023-10-05 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(max_length=20)),
                ('empname', models.CharField(max_length=100)),
                ('empgender', models.CharField(max_length=10)),
                ('empcontactno', models.CharField(max_length=15)),
                ('emergencycontact', models.CharField(max_length=15)),
                ('empemail', models.EmailField(max_length=100)),
                ('empaddress', models.TextField()),
                ('empdob', models.DateField()),
                ('emppassword', models.CharField(max_length=128)),
                ('empdesignation', models.CharField(max_length=20)),
                ('emptype', models.CharField(max_length=20)),
                ('empjoiningDate', models.DateField()),
            ],
        ),
    ]