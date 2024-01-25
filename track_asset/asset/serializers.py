from rest_framework import serializers
from.models import (Company,Employee,Device,DeviceLog)

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fileds=['name','phonenumber','email']
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fileds=['user','company']
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Device
        fileds=['device_name','desc','condition']
class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=DeviceLog
        fileds='__all__'