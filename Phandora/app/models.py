from django.db import models
from django import forms


class App(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255, blank=False)
    status = models.BooleanField(default=False)
    permission = models.CharField(max_length=1, choices=(('normal', 'normal user'),
                                                         ('super', 'super user')))