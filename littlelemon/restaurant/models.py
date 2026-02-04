from django.db import models

# Create your models here.
class Booking (models.Model):
    id = models.IntegerField(primary_key=True,default= 11)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=6)
    booking_date = models.DateTimeField()

class Menu (models.Model):
    id = models.IntegerField(primary_key= True, default=5)
    title = models.CharField(max_length=255)



class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
