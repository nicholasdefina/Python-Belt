# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from .models import *
from ..belt.models import *

from django.contrib  import messages
import bcrypt

def index(request):
    if "userid" in request.session:
        print "userid in session"
    if "first" in request.session:
        return render (request, 'login/success.html')

    else:
        print "userid not in session"
        return render (request, "login/index.html")

def success(request):
    print "login success"
    user = request.session["userid"]   
    return render (request, 'login/success.html')


def register(request, methods="POST"):
    errors = User.objects.validation(request.POST)  #errors set to be validation method of all posted data from form
    print errors
    if len(errors) > 0:                 
        for error in errors.iteritems():    #cycle through error list. iterate them all.
            messages.error(request, error)
        print messages
        return redirect('/')
    pwhash= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()) #hashing password and setting a variable for it
    newUser=User.objects.create(         #newUser set to be a query within a function.
        first = request.POST["first"],
        last = request.POST['last'],
        email = request.POST["email"],
        password = pwhash
    )   
    request.session["userid"] = newUser.id  #set session id to newuser id
    request.session["first"] = newUser.first

    return redirect("/success")

def log(request, methods="POST"):
    errors = User.objects.logvalidate(request.POST)
    if len(errors) > 0:
        for error in errors.iteritems():
            messages.error(request, error)
        print messages
        return redirect('/')
    else:
        user = User.objects.filter(email=request.POST['email'])[0]  #run query, check for email to equal POST. A list is returned. [0] calls that place in the list. Then you need to use key/value for dictionary
        request.session["userid"] = user.id
        request.session["first"] = user.first
        return redirect("/success")
    
    
def logout(request):
    request.session.clear()
    return redirect("/")

# Create your views here.
