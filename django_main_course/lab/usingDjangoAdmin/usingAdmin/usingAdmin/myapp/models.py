from django.db import models

# Create your models here.

class Employees(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()


    def __str__(self):
        return self.firstName
