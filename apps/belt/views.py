# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import *

from django.db.models import Q

from ..login_app.models import User

from django.contrib import messages
from datetime import datetime, date, time
from time import strptime,strftime
import datetime
import re


def index(request):
    currentUser=User.objects.get(id=request.session['userid']) #grabs the id of the current user in session
    quote=Quote.objects.all()
    favquote= currentUser.userfaves.all()

    context = {
        "quotes": quote,
        "favquotes": favquote
    }

    return render (request, "belt/index.html", context)


def add(request):
    
    errors= Quote.objects.validate(request.POST)
    currentUser = User.objects.get(id=request.session['userid'])
    
    if len(errors) > 0:
        for error in errors.iteritems():
            messages.error(request, error)
        return redirect (reverse('belt:index'))

    else:
           
        Quote.objects.create(quoted_by=request.POST["quoted_by"], quote=request.POST["quote"], poster=currentUser)
    return redirect (reverse("belt:index"))
        

def profile(request, id): 
    userposter= User.objects.get(id=id) # setting userposter to the idea of a poster
    quote = Quote.objects.filter(poster_id=userposter)  #setting quote to filter and check foreign key id and setting it to the userposter
    count = 0

    context = {
        "userposters": userposter,
        "quotes": quote,
        "count":0
    }
    
    return render (request, "belt/profile.html", context)


def addfave(request, id):
    currentUser = User.objects.get(id=request.session['userid'])  #grab object of current user via current user id
    fave = Quote.objects.get(id=id)        #grab object of specific quote id
    fave.favorites.add(currentUser)
    fave.save()
    
    return redirect ('belt:index')

def unfave (request, id):
    currentUser = User.objects.get(id=request.session['userid'])  #grab object of current user via current user id
    fave = Quote.objects.get(id=id)        #grab object of specific quote id
    fave.favorites.remove(currentUser)
    fave.save()

    return redirect ('belt:index')

# def edit(request, id):
    
#     context = {

#         "appt": Appt.objects.get(id=int(id))
#     }
#     return render (request, "belt/edit.html", context)
    
    
# def update(request,id):
#     errors = Appt.objects.validate(request.POST)
#     if len(errors) > 0:
#         for error in errors.iteritems():
#             messages.error(request, error)
#         return redirect(reverse('belt:edit', kwargs={'id':id}))
#     else:
#         Appt.objects.filter(id=int(id)).update(tasks=request.POST['tasks'], status=request.POST['status'],date=request.POST["date"], time=request.POST['time'])
#     return redirect (reverse('belt:index'))

# def destroy(request, id):
#     Appt.objects.get(id=int(id)).delete()
#     return redirect (reverse('belt:index'))

# Create your views here.
