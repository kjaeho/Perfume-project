from rest_framework import serializers
from .models import Perfume

class PerfumeSerializer(serializers.ModelSerializer):
    topList = serializers.SerializerMethodField()
    midList = serializers.SerializerMethodField()
    baseList = serializers.SerializerMethodField()
    lineList = serializers.SerializerMethodField()
    
    def get_topList(self,obj):
        if obj.top == None:
            return ''
        else:
            return obj.top.split(',')
    
    def get_midList(self,obj):
        if obj.mid == None:
            return ''
        else:
            return obj.mid.split(',')
    
    def get_baseList(self,obj):
        if obj.base == None:
            return ''
        else:
            return obj.base.split(',')

    def get_lineList(self,obj):
        if obj.line == None:
            return ''
        else:
            return obj.line.split(',')

    class Meta:
        model = Perfume
        fields = ["id",'name','image','year','gender','state','brand','info','topList','midList','baseList','lineList']