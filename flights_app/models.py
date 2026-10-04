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
    image = models.ImageField(upload_to='passenger_images/', blank=True, null=True)
    def __str__(self):
        return f"{self.first} {self.last}"
class FlightManifest(models.Model):
#primary_key=True makes flight both a foreign key and primary key of 
#FlightManifest that means Manifest id is the same as its flight id
#and each flight can have at least one manifest
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE,primary_key=True)
    notes = models.TextField()
    def __str__(self):
        return f"{self.flight} has {self.notes}"