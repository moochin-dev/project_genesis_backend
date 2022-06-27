from django.shortcuts import render
from .models import WaterBrand, WaterSource, TestHistory, Brand_Source
from rest_framework import viewsets
from .serializers import WaterBrandSerializer, WaterSourceSerializer, TestHistorySerializer, Brand_SourceSerializer

class WaterBrandSet(viewsets.ModelViewSet) :
    queryset = WaterBrand.objects.all()
    serializer_class = WaterBrandSerializer

class WaterSourceSet(viewsets.ModelViewSet) :
    queryset = WaterSource.objects.all()
    serializer_class = WaterSourceSerializer

class TestHistorySet(viewsets.ModelViewSet) :
    queryset = TestHistory.objects.all()
    serializer_class = TestHistorySerializer

class BrandSourceSet(viewsets.ModelViewSet) :
    queryset = Brand_Source.objects.all()
    serializer_class = Brand_SourceSerializer