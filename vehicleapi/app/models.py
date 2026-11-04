from django.db import models

# Create your models here.
class Vehicle(models.Model):
    vehicle_name=models.CharField(max_length=25)
    brand=models.CharField(max_length=10)
    model=models.CharField(max_length=20)
    price=models.IntegerField()
    fuel_type=models.CharField(max_length=20)
    image=models.ImageField(upload_to="vehicles",null=True)

