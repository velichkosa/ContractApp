from django.contrib import admin
from .models import *


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "do", "name", "blob", "created_at")

    # def date(self, obj):
    #     return obj.created_at.strftime("%d.%m.%Y")


    def do(self, obj):
        # return Interaction.objects.filter(id=obj.id)
        pass
    list_filter = ()
    # date.short_description = 'date'

@admin.register(Org)
class OrgAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


# admin.site.register(Contract)
admin.site.register(ContractRole)
admin.site.register(ContractUsers)
admin.site.register(Interaction)
# admin.site.register(Users)
# admin.site.register(Role)
# admin.site.register(Org)
# admin.site.register(Users, Org, Interaction, Contract, Role, ContractRole, ContractUsers)
# Register your models here.
