"""Tweets views."""

from django.shortcuts import render
from models import Tweet


def home(request):
    """Home View for / URL."""
    context = {
        'tweets': Tweet.objects.all()
    }
    return render(request, 'index.html', context)
