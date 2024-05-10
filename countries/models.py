from django.db import models

# Create your models here.
class Country(models.Model):

    name        = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=200, blank=False)
    code        = models.CharField(max_length=5, blank=True, default=True, null=True)

