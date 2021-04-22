from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


# Create your views here.
def index(request):
    return HttpResponse("Index Api")
def Handle_error(request):
    return HttpResponse("check URL")

class TestRestFramework(APIView):
    def get(self, request):
        return Response({"message": "GET call made"})
    def post(self, request):
        sum_vars = request.data.get("sum_vars")
        var1 = sum_vars["var1"]
        var2 = sum_vars["var2"]
        return Response({"messge": "POST call made. Sum of var1 and var2 is: %s" % (var1+var2)})
        #{"sum_vars":{"var1":1,"var2":2}}

class AddDevice(APIView):
    def post(self,request):
        serializer_obj = RawDeviceSerializer(data=request.data)
        if serializer_obj.is_valid():
            create_obj = DeviceStats.objects.create(**serializer_obj.data)
            return Response({"message": "Inserted data for %s" % serializer_obj.data.get("device_id")})
        else:
            return Response({"error_message": serializer_obj.errors})
