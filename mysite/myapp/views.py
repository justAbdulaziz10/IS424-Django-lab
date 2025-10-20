from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "myapp/index.html")


def abdullah(request):
    return HttpResponse("Hello, Abdullah!")


def mohammed(request):
    return HttpResponse("Hello, Mohammed!")


def greet(request, name):
    return render(request, "myapp/greet.html", {"name": name.capitalize()})

