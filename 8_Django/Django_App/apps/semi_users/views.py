# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from .models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
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
    User.objects.get(id = userid).delete()
    return redirect(reverse("index"))
#---Post Routes---
def create(request):
    if request.method == 'POST':
        User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email_address = request.POST['email_address'],id = User.objects.count() + 1)
        return redirect(reverse("index"))
    else:
        return redirect(reverse("index"))
def update(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect(reverse('edit', kwargs={'userid': request.POST['id']}))
        else:
            x = User.objects.get(id = request.POST['id'])
            x.first_name = request.POST['first_name']
            x.last_name = request.POST['last_name']
            x.email_address = request.POST['email_address']
            x.save()
            return redirect(reverse("index"))
    else:
        return redirect(reverse("index"))

    