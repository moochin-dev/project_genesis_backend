from django.db import models

# Create your models here.
class WaterBrand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    image_url = models.CharField(max_length=300)
    purchase_link = models.CharField(max_length=300)
    released_date = models.DateTimeField()
    price = models.IntegerField(null=True)
    rank = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class WaterSource(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Brand_Source(models.Model):
    id = models.AutoField(primary_key=True)
    brand = models.ForeignKey("WaterBrand", on_delete=models.DO_NOTHING)
    source = models.ForeignKey("WaterSource", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.brand.name + ' - ' + self.source.name
    
    
class TestHistory(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.ForeignKey("WaterSource", on_delete=models.DO_NOTHING)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.source.name + ' : ' + str(self.date.date())