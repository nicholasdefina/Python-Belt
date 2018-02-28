 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone

from django.db import models
from django.db.models import Q

from ..login_app.models import User
from datetime import datetime, date, time

from time import strptime,strftime
import pytz

import re
import datetime

class QuoteManager(models.Manager):
    def validate (self,data):
        errors ={}
            
        if len(data["quoted_by"]) < 3:
            errors["tasks"] = "Quoted by field  must be more than 3 characters."  
        if len(data["quote"]) < 10:
            errors["tasks"] = "Quoted by field  must be more than 10 characters."      
        
        
        return errors
        


class Quote(models.Model):
    quoted_by = models.CharField(max_length=15)
    quote = models.CharField(max_length=150)
    poster = models.ForeignKey(User, related_name="userposts")
    favorites = models.ManyToManyField(User, related_name="userfaves") #model for letting users favorite courses
    objects = QuoteManager()
# Create your models here.
