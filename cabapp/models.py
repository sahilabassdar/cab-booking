from django.db import models
from django.contrib.auth.models import User


# ---------------- CAR MODEL ----------------
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    car_number = models.CharField(max_length=20)
    price_per_km = models.IntegerField()

    def __str__(self):
        return self.car_name


# ---------------- DRIVER MODEL ----------------
class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Hatchback', 'Hatchback'),
    ]

    car_type = models.CharField(max_length=20, choices=CAR_TYPES)
    vehicle_number = models.CharField(max_length=20)

    STATUS = [
        ('Available', 'Available'),
        ('Busy', 'Busy'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='Available'
    )

    def __str__(self):
        return self.name


# ---------------- BOOKING MODEL ----------------
class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    pickup = models.CharField(max_length=100)
    drop = models.CharField(max_length=100)
    date = models.DateField()

    STATUS = [
        ('Pending', 'Pending'),
        ('Assigned', 'Assigned'),
        ('Reached Destination', 'Reached Destination'),
        ('Cancelled', 'Cancelled'),
    ]

    status = models.CharField(
        max_length=30,
        choices=STATUS,
        default='Pending'
    )

    def __str__(self):
        return self.name