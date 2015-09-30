"""Tweets model."""

from django.db import models


class Tweet(models.Model):

    """Tweet model."""

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
