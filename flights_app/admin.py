from django.contrib import admin
from .models import Airport, Flight, Passenger,FlightManifest
# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)
    list_display = ("id","first","last",'image')
admin.site.register(Airport)
admin.site.register(Flight,FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
admin.site.register(FlightManifest)