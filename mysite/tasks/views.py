from django.shortcuts import render

import tasks

# Create your views here.
tasks = ["foo", "bar", "baz"]
def index(request):
    return render(request, "tasks/index.html", {
    "tasks": tasks
    })
