from django import forms
# from django.db.models import QuerySet
from django.core.exceptions import ValidationError
from django.template.context_processors import request

from .models import *
from .views import *


class AddContractForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['type'].empty_label = 'Не выбрано'
        self.fields['do'].empty_label = 'Не выбрано'
        self.fields['po'].empty_label = 'Не выбрано'
        self.fields['author'].label = ""

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
                'disabled': True
            }),
            'date_at': forms.DateInput(attrs={'type': 'date'}),
            'date_to': forms.DateInput(attrs={'type': 'date'}),
            'do': forms.Select(attrs={
                # 'class': 'js-selectize',
                'placeholder': 'до',
                'style': "width: 325px;",
                'disabled': True
                }),
            'po': forms.Select(attrs={
                # 'class': 'js-selectize',
                'placeholder': 'по',
                'style': "width: 325px;",
                'disabled': True
            }),
            # 'do': forms.TextInput(attrs={'type': 'text'}),
            # 'po': forms.TextInput(attrs={'type': 'text'}),
            'author': forms.Select(attrs={
                # 'class': 'js-selectize',
                'placeholder': 'по',
                'style': "width: 325px;",
                'disabled': False,
                'hidden': 'hidden'
            })
        }

    # po = forms.ModelChoiceField(
    #     # queryset = Org.objects.values('name',).filter(id__exact='21'),
    #     queryset = Org.objects.all().filter(id__exact='21')
    # )

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
