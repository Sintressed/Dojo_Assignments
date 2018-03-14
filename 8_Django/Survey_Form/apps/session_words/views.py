# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from time import gmtime

# Create your views here.
def index(request):
    font = ''
    return render(request,'session_words/index.html')
def add(request):
    if request.method == 'POST':
        if request.POST['color'] == 'on':
            font = 'yes'
        else:
            font = 'no'
        if not "wlist" in request.session:
            request.session['wlist'] = []
            request.session['wlist'].append({request.POST['word'],request.POST['color'],font})
        else:
            request.session['wlist'].append({request.POST['word'],request.POST['color'],font})
        #print request.session['list']
        return redirect('/')
    else:
        print 'no'
        return redirect('/')
def delete(request):
    if request.method == 'POST':
        return redirect('/')
    else:
        return redirect('/')
