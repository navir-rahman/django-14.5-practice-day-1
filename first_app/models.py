from django.db import models

# Create your models here.
class myModel(models.Model):	
    name = models.CharField(max_length=10)
    roll = models.IntegerField(primary_key=True)
    