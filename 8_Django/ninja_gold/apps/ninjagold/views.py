# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
import random
from time import gmtime,strftime

# Create your views here.
def index(request):
    return render(request,'ninjagold/index.html')
def process(request):
    if request.method == "POST":
        gold = 0
        x = 'yes'
        if not "gold" in request.session:
            request.session['gold'] = 0
        if request.POST['action'] == 'farm':
            gold = random.randint(10, 20)
            place = 'farm'
            request.session['gold']  = request.session['gold'] + gold
        elif request.POST['action'] == 'cave':
            place = 'cave'
            gold = random.randint(5,10)
            request.session['gold']  = request.session['gold'] + gold
        elif request.POST['action'] == 'house':
            gold = random.randint(2,5)
            place = 'house'
            request.session['gold']  = request.session['gold'] + gold
        elif request.POST['action'] == 'casino':
            gold = random.randint(0,50)
            place = 'casino'
            take_give = random.randint(0,1)
            if take_give == 1:
                phrase = 'lost'
                x = 'no'
                
                request.session['gold']  = request.session['gold'] - gold
            else:
                phrase = 'won'
                request.session['gold']  = request.session['gold'] + gold
        if not "quote" in request.session:
            request.session['quote'] = []
            if not x == 'no':
                request.session['quote'].append(['Earned ' + str(gold) + ' golds from the ' + place + '!' + strftime(" (%Y/%m/%d %H:%M %p) ", gmtime()),'green'])
            else:
                request.session['quote'] = request.session['quote']
                request.session['quote'].append(['Entered a ' + place + ' and ' + phrase + str(gold) + ' golds... Ouch...' + strftime(" (%Y/%m/%d %H:%M %p) ", gmtime()),'red'])
        else:
            if not x == 'no':
                request.session['quote'] = request.session['quote']
                request.session['quote'].append(['Earned ' + str(gold) + ' golds from the ' + place + '!' + strftime(" (%Y/%m/%d %H:%M %p) ", gmtime()),'green'])
            else:
                request.session['quote'] = request.session['quote']
                request.session['quote'].append(['Entered a ' + place + ' and ' + phrase +' ' + str(gold) + ' golds... Ouch...' + strftime(" (%Y/%m/%d %H:%M %p) ", gmtime()), 'red'])
        return redirect('/')
    else:
        print 'not post'
        return redirect('/')     
