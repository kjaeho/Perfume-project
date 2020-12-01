from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# from imagekit.models import ProcessedImageField
# from imagekit.processors import Thumbnail
from django_resized import ResizedImageField


# Create your models here.


class User(AbstractUser):
    email = models.CharField(max_length=255, unique=True)
    gender = models.BooleanField(null=True)
    age = models.IntegerField(null=True)
    first_name = None
    last_name = None
    last_login = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class Clothes(models.Model):
    # image = models.ImageField(upload_to="clothes", blank=False)
    image = ResizedImageField(
        size=[2000, 2000], quality=80, upload_to="clothes", blank=False
    )
    # image = ProcessedImageField(
    #     upload_to="clothes",
    #     processors=[Thumbnail(256, 256)],  # 처리할 작업 목룍
    #     format="JPEG",  # 최종 저장 포맷
    #     options={"quality": 60},
    # )  # 저장 옵션

    created_at = models.DateTimeField(auto_now_add=True)
    adjectives = models.CharField(max_length=500, blank=True)
    lines = models.CharField(max_length=500, blank=True)
    perfume = models.ManyToManyField(settings.PERFUME_MODEL, blank=True)
    diary = models.TextField(null=True)
    spo = models.BooleanField()
    tag = models.TextField(null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="clothes",
        blank=True,
        default=1,
    )