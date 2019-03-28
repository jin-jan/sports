from django.conf import settings
from django.db import models
from django.utils import timezone

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
