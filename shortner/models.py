from django.db import models


class Url(models.Model):
    link = models.CharField(max_length=250)
    uuid = models.CharField(max_length=10)
