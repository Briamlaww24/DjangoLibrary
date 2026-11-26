from django.shortcuts import render

from catalog.classics import CLASSICS


def home(request):
    return render(request, "home/index.html", {"featuredBooks": CLASSICS[:3]})
