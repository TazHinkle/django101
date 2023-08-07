from django.shortcuts import render

# Create your views here.
tasks = [
    "one",
    "two",
    "three",
]


def index(request):
    # python does not support JS shorthand for assigning key/value of the same name.
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
