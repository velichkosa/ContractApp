from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .utils import *


# !!!! login_url = '/admin/'
# login_url = reverse_lazy(home)   перенаправление
# raise_exception = True
# @login_required   для функций


class Authentication(LoginView):
    form_class = AuthenticationForm
    template_name = 'contract/login.html'

    def get_success_url(self):
        return reverse_lazy(home)

def index(request):
    return render(request, 'contract/login.html')


def contract(request):
    posts = Contract.objects.all()
    return render(request, 'contract/contract.html', {'posts': posts})


def home(request):

    # return HttpResponse('<h1>Test page</h1>')
    # userslist = Users.objects.order_by('-created_at')
    # pass
    return render(request, 'contract/home.html')


def test(request):
    return HttpResponse('<h1>Test page</h1>')
