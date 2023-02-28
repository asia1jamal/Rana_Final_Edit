from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(UserInfo)
admin.site.register(DoctorsAvailablesAppointment)
admin.site.register(BookedAppoiments)
admin.site.register(Vaccine)
admin.site.register(VaccineLocations)


# Register your models here.

