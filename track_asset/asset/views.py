from django.shortcuts import render
from.models import (Company,Employee,Device,DeviceLog)
from .serializers import (CompanySerializer,EmployeeSerializer,DeviceSerializer,DeviceLogSerializer)
from rest_framework import generics
# Create your views here.

class CompanyListView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer
class EmployeeListView(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
class DeviceListView(generics.ListCreateAPIView):
    queryset=Device.objects.all()
    serializer_class=DeviceSerializer
class DeviceLogListView(generics.ListCreateAPIView):
    queryset=DeviceLog.objects.all()
    serializer_class=DeviceLogSerializer
