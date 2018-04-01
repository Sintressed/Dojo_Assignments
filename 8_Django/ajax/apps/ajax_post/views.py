# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers
from .models import *

# Create your views here.
def index(request):
    return render(request, "ajax_post/index.html")
def notes(request):
    return render(request ,"ajax_post/notes.html",{'notes': Notes.objects.all()})
def create(request):
    Notes.objects.create(note = request.POST['note'])
    return render(request, "ajax_post/notes.html", {'notes': Notes.objects.all()})
