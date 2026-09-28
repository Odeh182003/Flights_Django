from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.city} ({self.code})"
# Create your models here.
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name="Departures")#models.CharField(max_length=64)
    destination = models.ForeignKey(Airport,on_delete=models.CASCADE,related_name="Arrivals") #models.CharField(max_length=64)
    duration = models.IntegerField()
#String representation of the objects (toString in java)
    def __str__(self):
        return f"{self.origin} to {self.destination}"
class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
#blank=True means allow passenger to have no flights at all
    flights = models.ManyToManyField(Flight, blank=True,related_name="passenger")
    def __str__(self):
        return f"{self.first} {self.last}"