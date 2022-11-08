from django.db import models
from django.utils import timezone


# Create your models here.

class Research(models.Model):
    title = models.CharField(max_length=100)
    content= models.TextField() 
    created_at = models.DateTimeField(default=timezone.now)