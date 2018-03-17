# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    response = "placeholder to display a new form to create a new blog" 
    return HttpResponse(response)
def create(request):
    #if request.method == "POST":
        #print "*"*50
        #print request.POST
        #print request.POST['name']
        #print request.POST['desc']
        #request.session['name'] = "test"  # more on session below
        #print "*"*50
        #request.session['name'] = request.POST['name']
        #request.session['counter'] = 100
        #return redirect("/")
    #else:
    return redirect("/")
def show(request,number):
    response = "placeholder to display blog "
    return HttpResponse(response + str(number))
def edit(request,number):
    response = "placeholder to edit blog "
    return HttpResponse(response + str(number))
def destroy(request,number):
    return redirect("/")

