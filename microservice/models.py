from django.db import models

# Create your models here.


class UrlData(models.Model):
    url = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    negative_header = models.CharField(max_length=200)
