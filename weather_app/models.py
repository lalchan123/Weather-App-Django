from django.db import models
from django.db.models.base import Model

# Create your models here.

    
class City(models.Model):
        name = models.CharField(max_length=200)
        
        def __str__(self):
            return self.name
        
  