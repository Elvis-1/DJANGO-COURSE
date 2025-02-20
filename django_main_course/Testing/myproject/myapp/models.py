from django.db import models

# Create your models here.

class Reservations(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    bookingTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.firstName
