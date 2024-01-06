from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish(request):
    response='<html><body><h1>Hello Django</h1></body></html>'
    return HttpResponse(response)