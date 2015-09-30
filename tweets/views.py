"""Tweets views."""

from django.shortcuts import render


def home(request):
    """Home View for / URL."""
    context = {}
    return render(request, 'index.html', context)
