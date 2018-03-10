# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.utils.crypto import get_random_string
# Create your views here.

def index(request):
    return render(request,'random_word/index.html')
def process(request):
#random_word generator code
    if request.method == 'POST':
        request.session['generate'] = request.session['generate'] + 1
        request.session['word'] = get_random_string(length=14)
        return redirect('/')
    else:
        return redirect('/')
