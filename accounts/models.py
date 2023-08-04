from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
# Create your models here.


      
class CustomUser(AbstractUser):
 name = models.CharField(null=True, blank=True, max_length=100)
 urlfoto = models.CharField(null=True, max_length=500, blank=True)
 tienefoto = models.BooleanField(default=False)
