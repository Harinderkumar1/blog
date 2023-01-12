from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=55)
    image = CloudinaryField('image')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.Name

class contact(models.Model):
    name=models.CharField(max_length=55)
    email=models.EmailField()
    suggestion=models.TextField()

    def __str__(self):
        return self.name


class profile(models.Model):
    username=models.CharField(max_length=55)
    name=models.CharField(max_length=55)
    email=models.EmailField()

    def __str__(self):
        return self.name