from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Vehicle(models.Model):
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    year = models.IntegerField()
    service_interval = models.IntegerField(default=0, blank=True)
    next_service = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['make', 'year']

    def __str__(self):
        return self.make

class Car(Vehicle):
    seats = models.IntegerField(default=2)
    color = models.CharField(max_length=30)
    vin = models.CharField(max_length=30, blank=True)
    current_mileage = models.IntegerField(default=0)

class Truck(Car):
    bed_length = models.IntegerField(default=5)

class Boat(Vehicle):
    length = models.IntegerField(default=10)
    width = models.IntegerField(default=10)
    hin = models.CharField(max_length=30, blank=True)
    current_hours = models.IntegerField(default=0)