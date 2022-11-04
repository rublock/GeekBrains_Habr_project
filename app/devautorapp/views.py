from django.shortcuts import render
from .models import DevAuthor


def dev_authors(request):
    dev_autor = DevAuthor.objects.all()
    return render(request, "authors.html", {"dev_autor": dev_autor})
