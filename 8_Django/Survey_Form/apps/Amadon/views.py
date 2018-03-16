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
        print request.POST['product_id']
        #request.session['price'] = request.POST['']
        return redirect('/checkout')
    else:
        return redirect('/checkout')
