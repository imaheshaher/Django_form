from django.db import models

# Create your models here.

class Register(models.Model):
  first_name=models.CharField(max_length=20)
  last_name=models.CharField(max_length=20,blank=True)
  address=models.CharField(max_length=20,blank=True)