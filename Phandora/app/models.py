from django.db import models


class App(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    email = models.EmailField(max_length=255, unique=True)
    status = models.BooleanField(default=False)
    permission = models.CharField(max_length=1, choices=(('normal', 'normal user'),
                                                         ('super', 'super user')))