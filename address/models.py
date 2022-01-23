from django.db import models
# Create your models here.
class Address(models.Model):
  name = models.CharField(max_length=50, blank=True, null=True)
  address = models.CharField(max_length=500)
  lat = models.FloatField(blank=True, null=True)
  long = models.FloatField(blank=True, null=True)
  date = models.DateField(blank=True, null=True)
