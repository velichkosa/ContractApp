from django.contrib import admin
from .models import *


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "do", "po", "name", "blob", "datecreated")
    list_display_links = ("id", "name")
    # search_fields = ("name", "interaction")

    def datecreated(self, obj):
        return obj.created_at

    def do(self, obj):
        inter = Interaction.objects.get(id=obj.interaction_id)
        doName = Org.objects.get(id=inter.do_id)
        return doName.name

    def po(self, obj):
        inter = Interaction.objects.get(id=obj.interaction_id)
        doName = Org.objects.get(id=inter.po_id)
        return doName.name

    list_filter = ()
    datecreated.short_description = 'datecreated'
    do.short_description = 'do'
    po.short_description = 'po'
    verbose_name = 'Договора'

@admin.register(Org)
class OrgAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("id", "Name", "organization", "role")
    list_display_links = ("id", "Name")
    search_fields = ("Firstname__startswith", "Lastname__startswith", "org__name", "role__name")
    list_editable = ["role"]
    ordering = ["Lastname"]
    list_per_page = 10

    def Name(self, obj):
        return ("%s %s" % (obj.Firstname, obj.Lastname)).upper()
    Name.short_description = 'ФИО'

    def organization(self, obj):
        org = Org.objects.get(id=obj.org.id)
        return org.name.upper()
    organization.short_description = 'Наименование организации'

    def role(self, obj):
        return Users.role.name
    role.short_description = 'Должность'


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    # list_display = [field.name for field in Role._meta.get_fields() if not field.many_to_many]


@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ("id", "do", "po")
    list_display_links = ("id", "do", "po")
    # list_display = [field.name for field in Interaction._meta.get_fields() if not field.many_to_many]


@admin.register(ContractUsers)
class ContractUsersAdmin(admin.ModelAdmin):
    list_display = ("id", "contract", "user")
    list_display_links = ("id", "contract", "user")

    def contract(self, obj):
        contract = Contract.objects.get(id=obj.contract_id)
        return contract.name
    contract.short_description = 'contract'

    def user(self, obj):
        user = Users.objects.get(id=obj.users_id)
        return f'{user.Firstname} {user.Lastname}'
    user.short_description = 'user'


@admin.register(ContractRole)
class ContractRoleAdmin(admin.ModelAdmin):
    list_display = ("id", "contract", "role")
    list_display_links = ("id", "contract", "role")
    def contract(self, obj):
        contract = Contract.objects.get(id=obj.contract_id)
        return contract.name
    contract.short_description = 'contract'

    def role(self, obj):
        role = Role.objects.get(id=obj.role_id)
        return f'{role.name}'
    role.short_description = 'role'
# @admin.register(ContractRole)
# class ContractRoleAdmin(admin.ModelAdmin):
#     list_display = ("id", "do", "name", "role")
#
#     def name(self, obj):
#         contract_name = Contract.objects.get(id=obj.contract_id)
#         return contract_name.name
#     name.short_description = 'contract'
#
#     def role(self, obj):
#         allowed_role = Role.objects.get(id=obj.role_id)
#         return allowed_role.name
#     role.short_description = 'allowed_role'
#
#     def do(self, obj):
#         contract = Contract.objects.get(id=obj.contract_id)
#         intercation = Interaction.objects.get(id=obj.contract_id)
#         org = Org.objects.get(id=intercation.do_id)
#         return org.name
#     do.short_description = 'do_name'

# admin.site.register(Contract)
# admin.site.register(ContractRole)
# admin.site.register(ContractUsers)
# admin.site.register(Interaction)
# admin.site.register(Users)
# admin.site.register(Role)
# admin.site.register(Org)
# admin.site.register(Users, Org, Interaction, Contract, Role, ContractRole, ContractUsers)
# Register your models here.
