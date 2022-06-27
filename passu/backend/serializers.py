#backend/serializers.py
from rest_framework import serializers
from .models import WaterBrand, WaterSource, TestHistory, Brand_Source

class WaterBrandSerializer(serializers.ModelSerializer):
    class Meta :
        model = WaterBrand
        fields = '__all__'
        
class WaterSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterSource
        fields = '__all__'
        
class TestHistorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = TestHistory
        fields = '__all__'

class Brand_SourceSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Brand_Source
        fields = '__all__'