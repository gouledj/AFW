# fires/models.py

from django.db import models

class FireReport(models.Model):
    source = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField()
    verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class TwitterReport(models.Model):
    tweet_id = models.CharField(max_length=50, unique=True)
    user = models.CharField(max_length=100)
    content = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField()
