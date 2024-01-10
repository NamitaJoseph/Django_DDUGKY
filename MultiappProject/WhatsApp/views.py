from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,'wapp/whsignup.html')

def signin(request):
    return render(request,'wapp/whsignin.html')

def sendmail(request):
    return render(request,'wapp/whmsg.html')
