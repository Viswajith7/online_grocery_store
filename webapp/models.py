from django.db import models

# Create your models here.
class user_reg(models.Model):
    Name=models.CharField(max_length=34,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    Password=models.CharField(max_length=40,null=True,blank=True)
    Cpassword=models.CharField(max_length=45,null=True,blank=True)

class cartdb(models.Model):
    Pname=models.CharField(max_length=34,null=True,blank=True)
    Pprice=models.IntegerField(null=True,blank=True)
    PQ=models.IntegerField(null=True,blank=True)
    Ptotal_price=models.IntegerField(null=True,blank=True)
    User=models.CharField(max_length=45,null=True,blank=True)
