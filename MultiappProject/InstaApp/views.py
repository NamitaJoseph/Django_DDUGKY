from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,'iapp/insignup.html')

def signin(request):
    return render(request,'iapp/insignin.html')

def sendmail(request):
    return render(request,'iapp/inmsg.html')
