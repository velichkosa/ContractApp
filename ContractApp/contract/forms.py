from django import forms
# from django.db.models import QuerySet
from django.core.exceptions import ValidationError

from .models import *
from .views import *


class AddContractForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = 'Не выбрано'
        self.fields['author'].empty_label = '1'

    class Meta:
        model = Contract
        # fields = '__all__'
        fields = ['type', 'name', 'date_at', 'date_to', 'do', 'po', 'author', 'blob']
        widgets = {
            'type': forms.Select(attrs={
                # 'class': 'js-selectize',
                'style': "width: 325px;"}),
            'name': forms.TextInput(attrs={
                # 'class': 'form-control form-group col-md-6 form-row',
                'maxlength': 30,
                'style': "width: 300px;",
                'disabled': True}),
            'do': forms.Select(attrs={
                # 'class': 'js-selectize',
                'placeholder': 'до',
                'style': "width: 325px;",
                'disabled': True}),
            'po': forms.Select(attrs={
                # 'class': 'js-selectize',
                'placeholder': 'по',
                'style': "width: 325px;",
                'disabled': True}),
            # 'do': forms.TextInput(attrs={'type': 'text'}),
            # 'po': forms.TextInput(attrs={'type': 'text'}),
            'author': forms.Select(attrs={
                # 'class': 'js-selectize',
                'placeholder': 'по',
                'style': "width: 325px;",
                'disabled': True})
        }

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
