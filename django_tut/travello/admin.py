from django.contrib import admin
from .models import Destination,Booking

# Register your models here.
admin.site.register(Destination)

class BookingAdmin(admin.ModelAdmin):

    list_display = ('id','full_name','name','p_phone','depart_date','return_date','booked_on')

admin.site.register(Booking,BookingAdmin)

