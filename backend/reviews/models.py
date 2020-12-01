from django.db import models
from django.conf import settings
from perfumes.models import Perfume

# Create your models here.
class Review(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    diary= models.TextField(null=True)
    photo = models.ImageField(upload_to="image")
    spo = models.BooleanField()
    tag = models.TextField(null=True)
    perfume= models.ManyToManyField(Perfume,blank=True,related_name='perfume')

