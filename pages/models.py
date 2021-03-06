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
    python_tip = models.TextField(blank=True)
    posted_by = models.CharField(max_length=20)
    is_published = models.BooleanField(default=True)
    likes = models.IntegerField(blank=True, null=True)  # allow empty values for db and forms
    retweets = models.IntegerField(blank=True, null=True)
    tweet_link = models.URLField(max_length=200, blank=True, null=True)
    timestamp = models.DateTimeField(null=False)
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
    media_link = models.URLField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Links"

    def __str__(self):
        return self.media_link


class Contribution(models.Model):
    """
    A Model to mock @python_tip google form
    (https://docs.google.com/forms/d/e/1FAIpQLScsHklRH2-uplGYH_vxhtIin-zJS44bXQkAWCH7_N7nUdrGXw/viewform)
    """
    contributor = models.ForeignKey(User, on_delete=models.CASCADE)
    daily_tip = models.CharField(max_length=140, unique=True, blank=False, null=False)
    name_or_id = models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Contributors"

    def __str__(self):
        return self.daily_tip
