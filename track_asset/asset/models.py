from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    name=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=100,default='01****')
    email=models.EmailField(default='company@example.com')
    def __str__(self) -> str:
        return str(self.name)

class Employee(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return str(self.user)
    
class Device(models.Model):
    device_name=models.CharField(max_length=100)
    desc=models.TextField()
    condition=models.CharField(max_length=100)
    def __str__(self) -> str:
        return str(self.device_name)
class DeviceLog(models.Model):
    device=models.ForeignKey(Device,on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    checkedout=models.DateTimeField()
    return_checktime=models.DateTimeField()
    check_condition=models.CharField(max_length=100)
    return_check_condition=models.CharField(max_length=100)
    def __str__(self) -> str:
        return str(self.device)

class Subscription(models.Model):
    company=models.OneToOneField(Company,on_delete=models.CASCADE)
    detail=models.TextField()
    start_plan_set=models.DateTimeField(auto_now_add=True)
    end_plan_date=models.DateTimeField()

