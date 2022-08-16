from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Hel wor</h1>')


def test(request):
    return HttpResponse('<h1>Test page</h1>')
