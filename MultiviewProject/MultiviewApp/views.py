from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,'mview/signup.html')

def signin(request):
    return render(request,'mview/signin.html')

def sendmail(request):
    return render(request,'mview/sendmail.html')
