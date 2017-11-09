# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.shortcuts import render,get_object_or_404
from django.utils import timezone

from .models import Bookstore, profile


def index(request):
   books = Bookstore.objects.all()
   context = {
      'books':books
   }
   return render(request,'bookstore/index.html',context)

def create(request):
    today = datetime.date.today()
    print "request is",request.POST
    if "cancel" in request.POST:
        print "inside cancel"
        return redirect('/')
    else:
        print "inside else"
        book = Bookstore(name=request.POST['name'],description=request.POST['description'],Author=request.POST['Author'],created_at = today)
        book.save()
        return redirect('/')


def Delete(request,id):
    book = Bookstore.objects.get(id=id)
    book.delete()
    return redirect('/')


def Edit(request,id):
   book = Bookstore.objects.get(id=id)
   context = {
       'book': book
   }
   return render(request, 'bookstore/edit.html', context)


def update(request,id):
    if "cancel" in request.POST:
        return redirect('/')
    else:
        book = Bookstore.objects.get(id=id)
        book.name = request.POST['name']
        book.description = request.POST['description']
        book.Author = request.POST['Author']
        book.save()
        return redirect('/')

def register(request):
    return render(request,'bookstore/registration.html')


def Createbook(request):
   return render(request,'bookstore/Createbook.html')