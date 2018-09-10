from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def input(request):
    return render(request,'base.html')
def add(request):
    x=int(request.GET['t1'])
    y=int(request.GET['t2'])
    z=x+y
    request.session['z']=z
    request.session.set_expiry(30)
    return HttpResponse('Data successfully submitted')
def display(request):
    if request.session.has_key('z'):
        z=request.session['z']
        return HttpResponse(z)
    else:
        return render(request,'base.html')