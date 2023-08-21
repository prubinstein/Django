from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)