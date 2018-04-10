# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=300)


class Issue(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(User)
