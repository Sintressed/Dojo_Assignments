# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse, redirect
# Create your views here.

def index(request):
    request.session['times'] = 0
    return render(request,'survey/index.html')
def result(request):
    return render(request,'survey/result.html')
def process(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['loc']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['tet']
        request.session['times'] = request.session['times'] + 1
        return redirect('/result/')
    else:
        return redirect('/result/')