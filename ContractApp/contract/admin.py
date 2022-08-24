from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = [UserInline]


# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "do", "po", "name", "blob", "author", "created_at")
    list_display_links = ("id", "name", "do")
    search_fields = ["name", "do__name", "po__name"]
    list_filter = ["author"]

    # def datecreated(self, obj):
    #     return obj.created_at
    #
    # datecreated.short_description = 'datecreated'
    verbose_name = 'Договора'


@admin.register(Org)
class OrgAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "inn", "kpp", "city")
    list_display_links = ("id", "name")
    search_fields = ("name", "inn__startswith")
    list_filter = ["city"]
    ordering = ["name"]
    list_per_page = 10
    save_on_top = True


# @admin.register(Users)
# class UsersAdmin(admin.ModelAdmin):
#     list_display = ("id", "Name", "organization", "role")
#     list_display_links = ("id", "Name")
#     search_fields = ("first_name__startswith", "last_name__startswith", "org__name", "role__name")
#     list_editable = ["role"]
#     ordering = ["last_name"]
#     list_filter = ["role"]
#     list_per_page = 10
#
#     # def role_name(self, obj):
#     #     role_name = Role.objects.get(id=obj.role_id)
#     #     return role_name.name
#     # role_name.short_description = 'Должность'
#
#
#     def Name(self, obj):
#         return ("%s %s" % (obj.last_name, obj.first_name)).upper()
#     Name.short_description = 'ФИО'
#
#     def organization(self, obj):
#         org = Org.objects.get(id=obj.org.id)
#         return org.name.upper()
#     organization.short_description = 'Наименование организации'


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ["id"]
    list_editable = ["name"]
    ordering = ["name"]
    # list_display = [field.name for field in Role._meta.get_fields() if not field.many_to_many]
    list_per_page = 10


# @admin.register(Interaction)
# class InteractionAdmin(admin.ModelAdmin):
#     list_display = ("id", "do", "po")
#     list_display_links = ("id", "do", "po")
#     # list_display = [field.name for field in Interaction._meta.get_fields() if not field.many_to_many]
#     list_per_page = 10


@admin.register(ContractUsers)
class ContractUsersAdmin(admin.ModelAdmin):
    list_display = ("id", "contract", "user")
    list_display_links = ("id", "contract", "user")
    list_per_page = 10

    def contract(self, obj):
        contract = Contract.objects.get(id=obj.contract_id)
        return contract.name
    contract.short_description = 'contract'

    def user(self, obj):
        user = User.objects.get(id=obj.users_id)
        return f'{user.first_name} {user.last_name}'
    user.short_description = 'user'


@admin.register(ContractRole)
class ContractRoleAdmin(admin.ModelAdmin):
    list_display = ["id", "contract", "role"]
    ordering = ["contract"]
    list_per_page = 15


admin.site.site_header = "ContractApp"
admin.site.index_title = "Консоль администратора"
