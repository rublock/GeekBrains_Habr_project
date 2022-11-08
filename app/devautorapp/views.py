from django.shortcuts import render
from .models import DevAuthor
from mainapp.models import Category

menu = Category.objects.all()


def dev_authors(request):
    dev_autor = DevAuthor.objects.all()
    return render(request, "authors.html", {"dev_autor": dev_autor, 'menu': menu.filter(active=True)})
