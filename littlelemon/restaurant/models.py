from django.db import models

# Create your models here.
class Booking (models.Model):
    id = models.IntegerField(primary_key=True,default= 11)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=6)
    BookingDate = models.DateTimeField

class Menu (models.Model):
    id = models.IntegerField(primary_key= True, default=5)
    title = models.CharField(max_length=255)
