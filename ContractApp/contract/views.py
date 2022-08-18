from django.shortcuts import render
from django.http import HttpResponse
from .models import  Users


def home(request):
    return HttpResponse('<h1>Test page</h1>')
    # userslist = Users.objects.order_by('-created_at')
    # pass
    # return render(request, 'contract/home.html', {'name': userslist})


def test(request):
    return HttpResponse('<h1>Test page</h1>')
