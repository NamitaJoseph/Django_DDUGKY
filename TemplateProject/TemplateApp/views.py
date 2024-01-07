from django.shortcuts import render
import datetime

# Create your views here.
def temp_view(request):
    time=datetime.datetime.now()
    dict={'time':time}
    return render(request,'hello.html',dict)