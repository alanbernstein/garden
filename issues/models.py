# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=300)

class Issue(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, realted_name = 'issues', on_delete=models.CASCADE)
    xcoord = models.FloatField()
    ycoord = models.FloatField()

class Parcel(models.Model):
    plot_id = models.IntegerField()
    gardener = models.ForeignKey(User, null = True, related_name = 'gardners', on_delete=models.CASCADE)