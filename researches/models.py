from django.db import models
from django.utils import timezone


# Create your models here.

class Research(models.Model):
    title = models.CharField(max_length=100)
    content= models.TextField() 
    image= models.ImageField(upload_to='researches/static/images', height_field=None, width_field=None, max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
