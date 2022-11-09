from django.db import models
from django.utils import timezone


# Create your models here.

class User(models.Model):

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.firstname


class Research(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    content= models.TextField() 
    image= models.ImageField(upload_to='images', height_field=None, width_field=None)
    created_at = models.DateTimeField(default=timezone.now)
