from django.urls import path
from . import views
urlpatterns = [
     path('company/', views.CompanyListView.as_view(), name='company_list_create'),
     path('employee/', views.EmployeeListView.as_view(), name='employee_list_create'),
     path('device/', views.DeviceListView.as_view(), name='device_list_create'),
     path('devicelog/', views.DeviceLogListView.as_view(), name='devicelog_list_create'),
]
