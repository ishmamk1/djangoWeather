from django.db import models

# Create your models here.
class Weather(models.Model):
    city = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    icon = models.CharField(max_length=20)
    favorite = models.BooleanField(default=False)