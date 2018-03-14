# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from time import gmtime,strftime
x = []
# Create your views here.
def index(request):
    font = ''
    return render(request,'session_words/index.html')
def add(request):
    if request.method == 'POST':
        if request.POST.get('font') == 'on':
            font = 'h1'
        else:
            font = 'h3'
        if not "wlist" in request.session:
            request.session['wlist'] = []
            request.session['wlist'].append([request.POST['word'],request.POST['color'],font,strftime("added on: %H:%M %p , %m-%d,%y", gmtime())]) 
        else:
            request.session['wlist'] = request.session['wlist']
            request.session['wlist'].append([request.POST['word'],request.POST['color'],font,strftime("added on: %H:%M %p , %m-%d,%y", gmtime())]) 
        return redirect('/')
    else:
        return redirect('/')
def delete(request):
    if request.method == 'POST':
        if not 'wlist' in request.session:
            return redirect('/')
        else:               
            del request.session['wlist']
            return redirect('/')
    else:
        return redirect('/')
