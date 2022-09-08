from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import *
from .utils import *
# from collections import namedtuple
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

from django.utils import timezone

now = timezone.now()

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
        return reverse_lazy('home')


def index(request):
    return render(request, 'contract/login.html')


def contract(request):
    posts = Contract.objects.all()
    return render(request, 'contract/contract.html', {'posts': posts})


class ContractHome(ListView):
    model = Contract
    template_name = 'contract/home.html'
    # context_object_name = 'contract'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        context['title'] = 'Главная страница'
        context['selected'] = 0
        context['time_now'] = now
        return context

    def get_queryset(self):
        org = self.request.user.userprofile.org
        return Contract.objects.filter(do_id=org.id).union(Contract.objects.filter(po_id=org.id))


# def home(request):
#     org = request.user.userprofile.org
#     get_contract = Contract.objects.filter(do_id=org.id).union(Contract.objects.filter(po_id=org.id))
#     return render(request, 'contract/home.html', {'menu': menu, 'contract': get_contract})


def test(request):
    return HttpResponse('<h1>Test page</h1>')


def contract_view(request, contract_id):
    return HttpResponse(f'DOGOVOR s ID= {contract_id}')


# class AddContract(ListView):
#     model = Contract

class AddContract(CreateView):
    model = Contract
    form_class = AddContractForm
    template_name = 'contract/addcontract.html'
    success_url = reverse_lazy('home')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        context['title'] = 'Добавление договора'
        # context['selected'] = 1
        return context




# def addcontract(request):
#     if request.method == 'POST':
#         form = AddContractForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # noinspection PyBroadException
#             form.save()
#             return redirect('home')
#
#     else:
#         form = AddContractForm()
#     po_list = Org.objects.all()
#     contract_type = ContractType.objects.all()
#     return render(request, 'contract/addcontract.html', {'menu': menu, 'form': form, 'po_list': po_list, 'contract_type': contract_type})


