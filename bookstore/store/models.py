# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import User

from bookstore import settings


def upload_location4(instance, filename):
    return "%s/%s" % (instance.id, filename)


class Bookstore(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200)
    Author = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    def __str__(self):
        return str(self.name)


class profile(models.Model):
    name = models.CharField(max_length=100)
    emailid = models.EmailField()
    contactnumber = models.IntegerField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)




