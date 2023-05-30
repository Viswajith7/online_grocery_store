from django.db import models

# Create your models here.
class catagorydb(models.Model):
    Catagoryname=models.CharField(max_length=17,null=True,blank=True)
    Description=models.CharField(max_length=500,null=True,blank=True)
    Image=models.ImageField(upload_to="photos",null=True,blank=True)


class productdb(models.Model):
    Category_name=models.CharField(max_length=17,null=True,blank=True)
    Productname=models.CharField(max_length=23,null=True,blank=True)
    Quantity = models.CharField(max_length=100, null=True, blank=True)
    Descriptions = models.CharField(max_length=1000, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Images = models.ImageField(upload_to="profile", null=True, blank=True)

