from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def my_walks(request):
    return HttpResponse("Hello, Walker!")