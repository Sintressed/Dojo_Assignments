# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse, reverse
from .models import *

# Create your views here.
def index(request):
    return render(request,"ajax_notes/index.html")
def notes(request):
    return render(request, "ajax_notes/notes.html",{'notes': Note.objects.all()})

##---Post Routes---##

def create(request):
    Note.objects.create(title = request.POST['title'], desc = "")
    return redirect(reverse('index'))
def update(request):
    if request.method == "POST":
        n = Note.objects.get(id = request.POST['noteid'])
        n.desc = request.POST['desc']
        n.save()
        return redirect(reverse("index"))
    else:
        print "update nope"
        return redirect(reverse("index"))
def delete(request):
    if request.method == "POST":
        Note.objects.get(id = request.POST['noteid']).delete()
        return redirect(reverse("index"))
    else:
        return redirect(reverse("index"))
   
    
