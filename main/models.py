from django.db import models

# Create your models here.

class Project(models.Model):
    headline = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to ='images/', default="project1.png")
    color = models.CharField(max_length=7)