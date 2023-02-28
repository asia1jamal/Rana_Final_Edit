from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from contextlib import _RedirectStream
from pstats import Stats
import statistics
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.http import *
from django.contrib import auth
from rest_framework.response import Response 
from rest_framework import decorators,viewsets
from django.http import HttpResponse
from rest_framework.decorators import  api_view
from doctor.models import *
from .serilizers import *
from rest_framework.views import APIView
from rest_framework.permissions import *
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authentication import *
from rest_framework.permissions import *
from rest_framework.authtoken.models import Token
from django.contrib import messages
from django.contrib.auth import *
from django.db.models import Q
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework.authentication import *
from django.contrib.auth import authenticate
from rest_framework.decorators import *
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

# Create your views here.

def get_type(user):
    data = UserInfo.objects.get(user_id=user)
    return data.account_type


@api_view(['POST'])
@permission_classes([AllowAny])
def create_new_user(request):
    firstName=request.data['firstName']
    middleName=request.data['middleName']
    lastName=request.data['lastName']
    email=request.data['email']
    userName=request.data['userName']
    password=request.data['password']
    accountType=request.data['accountType']
    age=request.data['age']

    user = authenticate(username=userName, password=password)
    if user:
        return Response("user is already exist")
    else:
        user = User.objects.create_user(username=userName, password=password, email=email)
    if user:
        user.save()
    else:
        return Response("there is problem with create user")
    user = authenticate(username=userName, password=password)
    if user:
        Token.objects.create(user=user)
    else:
        return Response("there is problem with create token")

    userInfo=UserInfo(user_id=user,firstName=firstName,middleName=middleName,lastName=lastName,account_type=accountType)
    if userInfo:
        userInfo.save()
        if accountType=="patient":
            patient=Patient(
                idNum=user,
                Image="null",
                gender="null",
                phoneNum="null",
                #location="الخرطوم",
            )
            if patient:
                patient.save()
            else:
                return Response("wrong with Patient")
        else:
            doctor=Doctor(
            idNum=user,
            EducationsLiences ="null",
            Image = "null",
            phoneNum = "null",
           gender = "null"
            )
            if doctor:
                doctor.save()
            else:
                return Response("worng with Doctor")
        return Response("Welcome"+firstName+middleName+LastName)
    else:
        return Response("some thing is wrong")

"""
{
    "firstName":"asia",
    "middleName":"jamal",
    "lastName":"lastName",
    "email":"email@gmail.com",
    "userName":"rihap",
    "password":"1233",
    "accountType":"patient"
    }"""






@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def UpdateProfile(request):
    currentUser = request.user.id
    accountType=get_type(currentUser)
    info = None
    if request.method=='GET':
        if accountType=="patient":
            patient=Patient.objects.get(idNum=currentUser)
            ser=Patientserilizers(patient)
            return Response(ser.data)
        else:
            doctor=Doctor.objects.get(idNum=currentUser)
            ser=doctorsserilizer(doctor)
            return Response(ser.data)
    else:
        if accountType=="patient":
            patient = Patient.objects.get(idNum=currentUser)
            dataPatient ={
              "idNum":currentUser,
              "Image":request.data[' Image'],
              "phoneNum":request.data['phoneNum'],              
              "gender":request.data['gender']
            }
            ser = Patientserilizers(patient,data=dataPddatient)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)
        else:
            doctor = Doctor.objects.get(idNum=currentUser)
            dataDoctor={
              "idNum":currentUser,
              "Image":request.data[' Image'],
              "phoneNum":request.data['phoneNum'],              
              "gender":request.data['gender'],
             "EducationsLiences":request.data['EducationsLiences']
              
            }
            ser = doctorsserilizer(doctor,data=dataIDoctor)
            if ser.is_valid():
                ser.save()
                return Response(ser.data)


#API FOR ADMIN + PATIENT   
@api_view(['GET'])
def getVacc(request):
    vacc=Vaccine.objects.all()
    ser = Vaccineserilizer(vacc,many=True)
    return Response(ser.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserType(request):
    currentUser = request.user.id
    data = UserInfo.objects.get(user_id=currentUser)
    return Response(data.account_type)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def WitchVacc(request):
    current_user=request.user.id
    data=UserInfo.objects.get(user_id=current_usr)
    return Response(data.age) 



@api_view(['GET'])
def getVaccByID(request,pk):
    vacc=Vaccine.objects.get(id=pk)
    ser=Vaccineserilizer(vacc,many=False)
    return Response(ser.data)



#API FOR PATENT
@api_view(['GET'])
@authentication_classes([TokenAuthentication,BaseAuthentication,SessionAuthentication])
@permission_classes([IsAuthenticated])
def Show_my_Appointments(request):
    Current_Patient=request.user.id
    my_Appointments=BookedAppoiments.objects.filter(by_user=Current_Patient)
    p_ser=bookedAppoimentserilizers(my_Appointments)
    if p_ser :
        return Response(p_ser.data)
    else:
        return Response(" YOU HAVE NO APPOINTMENTS YET")


@api_view(["GET"])
def showDoctorAppointments(request,pk):
    current_Doctor=request.user.id
    AvailabeAppointments=DoctorsAppointment.objects.all()



#مفروض اعمل ليها API###############
@api_view(["POST"])
#@authentication_classes([TokenAuthentication,BaseAuthentication,SessionAuthentication])
#@permission_classes([IsAuthenticated])
def BookAppointment(request,id):
    current_Appointment=BookedAppoiments.objects.get(pk=id)
    current_Patient=request.user.id
    current_Date=current_Appointment.Date
    if current_Date is not None:
        ser= bookedAppoimentserilizers(current_Appointment)
        return Response(ser.data)
    else:
         return Response("APPOINTMENT NOT AVAILABLE")
    if online_chices is not None:
            current_Patient=request.user.id
            current_Date=current_Appointment.date


@api_view(['POST'])
#@authentication_classes([TokenAuthentication,BasicAuthentication,SessionAuthentication])
def createNewAppoinment(request):
    current_Doctor=request.user.id
    select_Location_Id=request.data['Location']
    Hospital=request.date['date']
    privateClinical=request.date['date']
    date=request.date['date']
    begin_time=request.data['begin_time']
    finish_time=request.data['finish_time']

    new_Appointment=DoctorsAppointment(
        by_Doctor_id=current_Doctor,
        LocationOfAppoiment=select_Location_Id,
        date=date,
        begin_time=begin_time,
        finish_time=finish_time
    )
    new_Appointment.save()
    App=DoctorsAppointmentserilizer(new_Appointment)
    return Response(App.data)









#API ADD FOR ADMIN
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addVacc(request):
    #VaccID=request.data['1']
    newVacc=Vaccine(
    Title=request.data['Title'],
    Age=request.data[' Age'],
    WhatBefor=request.data[' WhatBefor'],
    WhatAfter=request.data['WhatAfter'],
    WhatToDo=request.data['WhatToDo'],
    Symptoms=request.data[' Symptoms'],
    location=request.data['location']
    )
    if newVacc:
        newVacc.save()
    return Response("Done")


#FOR ADMIN API
@api_view(["GET"])
def tableForAllApoointment(request):
    all=BookedAppoiments.objects.all()
    all_ser=bookedAppoimentserilizers(all,many=True)
    return Response(all_ser.data)

#API FOR ADMIN 
@api_view(['GET'])
def GetPatients(request):
    patient=Patient.objects.all()
    patient_ser=patientinfoserilizer(patient,many=False)
    return Response(patient_ser.data)


#API FOR ADMIN + Patient
@api_view(['GET'])
def doctors_list(request):
    doctor_list=Doctor.objects.all()
    Doc_ser=doctorsserilizer(doctor_list,many=True)
    return Response(Doc_ser.data)