from django.urls import path
from .views import *


urlpatterns = [
    path('', Authentication.as_view(), name='login'),
    path('test/', test),
    path('contract/', contract),
    # path('home/', home, name='home'),
    path('home/', ContractHome.as_view(), name='home'),
    path('contract_view/<int:contract_id>/', contract_view, name='contract_view'),
    # path('addcontract/', addcontract, name='addcontract'),
    path('addcontract/', AddContract.as_view(), name='addcontract'),
]
