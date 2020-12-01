from django.db import models

# Create your models here.


class Perfume(models.Model):
    name = models.TextField()
    image = models.TextField()
    year = models.IntegerField(null=True)
    gender = models.IntegerField()
    state = models.IntegerField()
    brand = models.CharField(max_length=300)
    info = models.TextField(null=True)
    top = models.TextField(null=True)
    mid = models.TextField(null=True)
    base = models.TextField(null=True)
    line = models.TextField(null=True)
