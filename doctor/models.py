from django.db import models

# Create your models here.
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver #جهة مستقبلة للتعليمات
from rest_framework.authtoken.models import Token 
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import django.utils.timezone
from django.conf import settings

# Create your models here.


class Patient(models.Model):
    idNum=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    firstName=models.CharField(default=" ", blank=False, null=False, max_length=35)
    middleName=models.CharField(default=" ", blank=False, null=False, max_length=35)
    lastName=models.CharField(default=" ", blank=False, null=False, max_length=35)
    #email=models.EmailField(blank=True,null=True)
    birthdate=models.DateField(blank=True,null=True)
    #password=models.CharField(max_length=10)
    Image=models.ImageField(upload_to='images')
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phoneNum=models.IntegerField()



#class PatientInfo(models.Model):
   


class UserInfo(models.Model):
    user_id=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firstName=models.CharField(default=" ", blank=False, null=False, max_length=35)
    middleName=models.CharField(default=" ", blank=False, null=False, max_length=35)
    lastName=models.CharField(default=" ", blank=False, null=False, max_length=35)
    account_type=models.CharField(blank=False,null=False,max_length=10)
    age=models.IntegerField(default="1")


class Doctor(models.Model):
    idNum=models.OneToOneField(User,on_delete=models.CASCADE)
    firstName=models.CharField(default=" ", blank=False, null=False, max_length=35)
    middleName=models.CharField(default=" ", blank=False, null=False, max_length=35)
    lastName=models.CharField(default=" ", blank=False, null=False, max_length=35)
    #email=models.EmailField(blank=True,null=True)
    #birthdate=models.DateField(blank=True,null=True)
    #password=models.CharField(max_length=10)
    EducationsLiences=models.TextField(max_length=1000)
    Image=models.ImageField(upload_to='images')
    phoneNum=models.IntegerField() 
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

class DoctorsAvailablesAppointment(models.Model):
    DoctorName=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    DateOfAppoiment=models.DateField(blank=True,null=True)
    Hosbital=models.CharField(max_length=30)
    privateClinical=models.CharField(max_length=255)
    #date=models.DateField(blank=True,null=True)
    begin_time=models.DateTimeField(blank=True,null=True)
    finish_date=models.DateTimeField(blank=True,null=True)
    Place=(('HOSPITAL','HOSPITAL'),
         ('PRIVATECLINIC','CLINIC'))
    Online=models.BooleanField()
    location=models.CharField(max_length=30)


class BookedAppoiments(models.Model):
    doctorName=models.ForeignKey(Doctor,related_name='appointment',on_delete=models.CASCADE)
    PatientName=models.ForeignKey(Patient,related_name='appointment',on_delete=models.CASCADE)
    location=models.CharField(max_length=30)
    #Date=models.DateField(blank=True,null=True)
    DateANDtime=models.DateTimeField(blank=True,null=True)


class Vaccine(models.Model):
    #VaccID=models.IntegerField(primary_key=True)
    Title=models.CharField(max_length=255)
    Age=models.IntegerField()
    WhatBefor=models.CharField(max_length=255)
    WhatAfter=models.CharField(max_length=255)
    WhatToDo=models.CharField(max_length=255)
    Symptoms=models.CharField(max_length=255)
    location=models.CharField(max_length=30)
    Centers=models.CharField(default="h",max_length=255)

class VaccineLocations(models.Model):
    Khartoum=models.CharField(max_length=255)
    Bahri=models.CharField(max_length=255)
    Omdurman=models.CharField(max_length=255)



