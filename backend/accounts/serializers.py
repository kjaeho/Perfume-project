from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Clothes, User

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "gender",
            "age",
            "is_superuser",
            "is_staff",
            "is_active",
        )


class ClothesSerializer(serializers.ModelSerializer):
    lineList = serializers.SerializerMethodField()
    adjectiveList = serializers.SerializerMethodField()
    tagList = serializers.SerializerMethodField()
    
    def get_lineList(self,obj):
        if obj.lines == None:
            return ''
        else:
            return obj.lines.split(',')

    def get_adjectiveList(self,obj):
        if obj.adjectives == None:
            return ''
        else:
            return obj.adjectives.split(',')
    
    def get_tagList(self,obj):
        if obj.tag == None:
            return ''
        else:
            return obj.tag.split('#')

    class Meta:
        model = Clothes
        # fields = ("id", "image", "created_at", "perfume", "user")
        fields = ('id','image','lineList','adjectiveList','tagList','created_at','diary','perfume','spo','user')
