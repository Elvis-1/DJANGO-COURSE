from django.db import models


# Create your models here.


class Person(models.Model): 
    last_name = models.TextField() 
    first_name = models.TextField() 

    def __str__(self): 
        return f"{self.last_name}, {self.first_name}" 


class Reservations(models.Model):
    # name,contact,time,count,note
    name = models.CharField(max_length=200)
    contact = models.CharField('Phone number', max_length=300,default='')
    time = models.DateTimeField(null = True, blank=True)
    count = models.IntegerField(default=0)
    note = models.CharField(max_length=300, blank=True)


    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    # name,contact,time,count,note
    name = models.CharField(max_length=200)
    contact = models.CharField('Phone number', max_length=300,default='')
    time = models.DateTimeField(null = True, blank=True)
    count = models.IntegerField(default=0)
    note = models.CharField(max_length=300, blank=True)


    def __str__(self):
        return f"{self.name}"

