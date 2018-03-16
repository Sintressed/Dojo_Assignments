# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
# Create your views here.
def index(request):
    request.session['item_list'] = [['0','Dojo Tshirt','19.99'],['1','Dojo Sweater','29.99'],['2','Dojo Cup','4.99'],['3','Algorithm Book','49.99']]
    return render(request, 'Amadon/index.html')
def checkout(request):
    return render(request,'Amadon/checkout.html')
def process(request):
    if request.method == 'POST':
        for item in request.session['item_list']:
            if item[0] == request.POST['product_id']:
                request.session['price'] = float(item[2]) * float(request.POST['actions'])
                if not "items" in request.session:
                    request.session['items'] = 0
                    request.session['items'] += 1
                else:
                    request.session['items'] = request.session['items'] + 1
                if not "total" in request.session:
                    request.session['total'] = 0
                    request.session['total'] = request.session['total'] + float(item[2])
                else: 
                    request.session['total'] = request.session['total'] + float(item[2])
        return redirect('/checkout')
    else:
        return redirect('/checkout')
