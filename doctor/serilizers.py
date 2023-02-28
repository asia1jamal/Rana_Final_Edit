from rest_framework import serializers
from doctor.models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator
class bookedAppoimentserilizers(serializers.ModelSerializer):
    class Meta():
        model=BookedAppoiments
        fields='__all__'


class UserInfoserilizers(serializers.ModelSerializer):
    class Meta():
        model=UserInfo
        fields='__all__'
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')
"""

class Patientserilizers(serializers.ModelSerializer):
    class Meta():
        model= Patient
        fields='__all__'

class doctorsserilizer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields='__all__'

"""class doctorinfoserilizer(serializers.ModelSerializer):
    class Meta:
        model=DoctorInfo
        fields='__all__'"""


"""class patientinfoserilizer(serializers.ModelSerializer):
    class Meta:
        model=PatientInfo()
        fields='__all__'
"""
class UserInfoserilizer(serializers.ModelSerializer):
    class Meta:
        model=UserInfo()
        fields='__all__'


class DoctorsAppointmentserilizer(serializers.ModelSerializer):
    class Meta:
        model= DoctorsAvailablesAppointment
        fields='__all__'

class Vaccineserilizer(serializers.ModelSerializer):
    class Meta:
        model=Vaccine
        fields='__all__'


class VaccineLocationsserilizer(serializers.ModelSerializer):
    class Meta:
        model=VaccineLocations
        fields = '__all__' 
