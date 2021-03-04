import logging

from django.contrib.auth.models import User
from django.db import models

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your models here.


class Tip(models.Model):
    """
    A Model to store tweet details from Daily Python Tip
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tips')
    python_tip = models.TextField(blank=True)
    posted_by = models.CharField(max_length=20)
    is_published = models.BooleanField(default=True)
    likes = models.IntegerField(blank=True, null=True)  # allow empty values for db and forms
    retweets = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Tips"

    def __str__(self):
        return self.python_tip


class Link(models.Model):
    """
    A Model to store a tweet link in case a tweet has more than one link
    """
    tip = models.ForeignKey(Tip, on_delete=models.CASCADE, related_name='links', blank=True, null=True)
    tweet_link = models.URLField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Links"

    def __str__(self):
        return self.tweet_link
