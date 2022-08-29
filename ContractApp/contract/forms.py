from django import forms
# from django.db.models import QuerySet
from django.core.exceptions import ValidationError

from .models import *


class AddContractForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = 'Не выбрано'


    class Meta:
        model = Contract
        # fields = '__all__'
        fields = ['name', 'do', 'po', 'author', 'type', 'blob']

    def clean_do(self):
        do = self.cleaned_data['do']

        # if do==po:
        #     raise ValidationError('ДО и ПО должны отличаться!')
        return do
    # name = forms.CharField(max_length=30, label='Предмет договора')
    # # blob = forms.FileField(required=False)
    # do = forms.ModelChoiceField(queryset=Org.objects.all(), label="ДО")
    # po = forms.ModelChoiceField(queryset=Org.objects.all(), label="ПО")
    # author = forms.ModelChoiceField(queryset=User.objects.all(), label="Автор")
    # contract_type = forms.ModelChoiceField(queryset=ContractType.objects.all(), label="Тип договора")
    # # created_at = forms.DateField()
