from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request,'fapp/fbsignup.html')

def signin(request):
    return render(request,'fapp/fbsignin.html')

def sendmail(request):
    return render(request,'fapp/fbmsg.html')
