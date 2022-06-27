from django.contrib import admin
from .models import WaterBrand, WaterSource, TestHistory, Brand_Source

# Register your models here.
admin.site.register(WaterBrand)
admin.site.register(WaterSource)
admin.site.register(TestHistory)
admin.site.register(Brand_Source)