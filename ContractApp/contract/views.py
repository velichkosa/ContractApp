from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import *
from .utils import *
# from collections import namedtuple
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

menu = [
    {'title': "На главную", 'url_name': 'home'},
    {'title': "Добавить договор", 'url_name': 'addcontract'}
]


# def namedtuplefetchall(cursor):
#     "Return all rows from a cursor as a namedtuple"
#     desc = cursor.description
#     nt_result = namedtuple('Result', [col[0] for col in desc])
#     return [nt_result(*row) for row in cursor.fetchall()]
#
#
# def dictfetchall(cursor):
#     "Return all rows from a cursor as a dict"
#     columns = [col[0] for col in cursor.description]
#     return [
#         dict(zip(columns, row))
#         for row in cursor.fetchall()
#     ]


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
    org = request.user.userprofile.org
    get_contract = Contract.objects.filter(do_id=org.id).union(Contract.objects.filter(po_id=org.id))
    return render(request, 'contract/home.html', {'menu': menu, 'contract': get_contract})


def test(request):
    return HttpResponse('<h1>Test page</h1>')


def contract_view(request, contract_id):
    return HttpResponse(f'DOGOVOR s ID= {contract_id}')


def addcontract(request):
    if request.method == 'POST':
        form = AddContractForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # noinspection PyBroadException
            try:
                Contract.objects.create(**form.cleaned_data)
                return redirect('home')
            except Exception:
                form.add_error(None, 'Ошибка добавления договора')
    else:
        form = AddContractForm()
    po_list = Org.objects.all()
    contract_type =
    return render(request, 'contract/addcontract.html', {'menu': menu, 'form': form, 'po_list': po_list})
