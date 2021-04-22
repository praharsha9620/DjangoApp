from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('test',views.index, name='test'),
    path('',views.Handle_error, name='Error'),
    url('test_get', views.TestRestFramework.as_view(), name='test_get'),
    url('add_device', views.AddDevice.as_view(), name='add')
]
