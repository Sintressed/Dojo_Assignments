# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from .models import User
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return render(request,"semi_users/index.html", {'users' :  User.objects.order_by("id")})
def new(request):
    return render(request,"semi_users/new.html")
def identify(request,userid):
    return render(request,"semi_users/id.html",{'userid': userid, 'id' : User.objects.get(id = userid)})
def edit(request,userid):
    return render(request,"semi_users/edit.html",{'userid': userid, 'id' : User.objects.get(id = userid)})
def destroy(request,userid):
    return HttpResponse("Destroy")
#---Post Routes---
def create(request):
    if request.method == 'POST':
        return redirect(reverse("index"))
    else:
        return redirect(reverse("index"))
def update(request):
    if request.method == 'POST':
        return redirect(reverse("index"))
    else:
        return redirect(reverse("index"))

    