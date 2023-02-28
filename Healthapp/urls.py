from rest_framework.routers import DefaultRouter
from doctor import views
from rest_framework.authtoken.views import obtain_auth_token
#obtain_auth_token فيو بيعمل aceess للمودل حق الtokens 
from django.contrib.auth.views import LoginView , LogoutView
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('doctor.urls')),
    path('newUser/',views.create_new_user),
    path('getUserType/',views.getUserType),
    path('profileUpdate/',views.UpdateProfile),
    path('ShowVaccintaion/',views.getVacc),
    path('GetSpacificVacc/',views.getVaccByID),
    path('ShowAllDoctors/',views.doctors_list),#for admin + patient
    path('ShowPatientBookedAppointments/',views.Show_my_Appointments),
    path('ShowDoctorsAppointment/',views.showDoctorAppointments),
    path('createNewAppoinment',views.createNewAppoinment),         
    path('add',views.addVacc),
    path('tableOfAllApppintment',views.tableForAllApoointment),        
    path('ShowAllPatient/',views.GetPatients),
    path('ShowAllPatient/',views.GetPatients),
    path('api-token-auth/',views.obtain_auth_token),
    path('calenderVac/',views.WitchVacc)
       
]