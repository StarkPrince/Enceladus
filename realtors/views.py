from django.shortcuts import render


def index(request):
    return render(request, "<h1>Hello</h1>")
