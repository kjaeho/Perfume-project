from django.contrib import admin
from .models import User, Clothes

# Register your models here.

admin.site.register(Clothes)
admin.site.register(User)