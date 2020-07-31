from django.shortcuts import render
from rest_framework import viewsets 
from rest_api_app.serializers import StudentSerializers
from rest_api_app.models import Student
from rest_framework.authentication import TokenAuthentication 

# Create your views here.
class StudentViewSets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    authentication_class = TokenAuthentication
  