from django.contrib import admin
from .models import *


admin.site.register(Contract)
admin.site.register(ContractRole)
admin.site.register(ContractUsers)
admin.site.register(Interaction)
admin.site.register(Users)
admin.site.register(Role)
admin.site.register(Org)
# admin.site.register(Users, Org, Interaction, Contract, Role, ContractRole, ContractUsers)
# Register your models here.
