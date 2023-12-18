from django.shortcuts import render
from .models import Student
from .seriallizers import Studetserializer
from rest_framework import jSONRenderer
from django.http import HttpResponse
# Create your views here.

def student_details(request):
    stu = Student.objects.get(roll = 2)
    seraliser = Studetserializer(stu)
    json_data = jSONRenderer().render(seraliser.data)
    return HttpResponse(json_data,content_type ="application/json")