from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('You are in Members')
def gallery(request):
    return HttpResponse('You are in gallery')
