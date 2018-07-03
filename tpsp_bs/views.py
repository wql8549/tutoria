# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from quickstart import views as q_views

# Create your views here.
def hellojq(request):
    return render(request, 'helloejq1.html')
def hellojq1(request):
    return render(request, 'helloejq2.html')
def hellojq2(request):
    data=q_views.hello_world(request).getvalue()
    print data
    if type(data)=='string':
        pass

    else:
        return HttpResponse(request, data)

def hellotest(request,a):
    print a
    b={'a':0}
    b['a']=a
    print b
    return HttpResponse(request, b)