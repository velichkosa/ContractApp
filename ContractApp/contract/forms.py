from django import forms
# from django.db.models import QuerySet

from .models import *


class AddContractForm(forms.Form):
    name = forms.CharField(max_length=30, label='Предмет договора')
    blob = forms.CharField(max_length=50, label='Файл договора (.pdf)')
    do = forms.ModelChoiceField(queryset=Org.objects.all(), label="ДО")
    po = forms.ModelChoiceField(queryset=Org.objects.all(), label="ПО")
    author = forms.ModelChoiceField(queryset=User.objects.all(), label="Автор")
