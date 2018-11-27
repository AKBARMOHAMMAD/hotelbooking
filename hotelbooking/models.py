from django.db import models
import datetime
# Create your models here.

#User Model
class Register(models.Model):
    name=models.CharField(max_length=50)
    email_id=models.EmailField(max_length=20,primary_key=True)
    password=models.CharField(max_length=50)
    contact_no=models.IntegerField()
    address=models.CharField(max_length=100)
class Check_Availability(models.Model):
    room_no=models.IntegerField()
    check_In=models.DateField()
    check_Out=models.DateField()
class Reserve_Room(models.Model):
    room_no=models.ForeignKey(Check_Availability,on_delete=models.CASCADE)
    room_type=models.CharField(max_length=50,primary_key=True)
    credit_card=models.IntegerField()
    debit_card=models.IntegerField()
    check_In=models.DateField()
    check_Out=models.DateField()
class Display(models.Model):
    user_name=models.CharField(max_length=50)
    cust_id=models.IntegerField()
    room_type=models.CharField(max_length=50,primary_key=True)
    room_no=models.ForeignKey(Reserve_Room,on_delete=models.CASCADE)
    check_In=models.DateField()
    check_Out=models.DateField()
    total_cost=models.FloatField()
class Cancle_Room(models.Model):
    user_name=models.CharField(max_length=50)
    room_no=models.ForeignKey(Display,on_delete=models.CASCADE)
    cust_id=models.IntegerField()


