from django.db import models

# Create your models here.
class Booking(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    guestCount = models.IntegerField()
    reserveTime = models.DateField(auto_now=True),
    comments = models.CharField(max_length=1000)


