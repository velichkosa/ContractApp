from django.db import models
# from django.db.models import ManyToManyField
from django.urls import reverse  # for absolute_url
from django.contrib.auth.models import User


class Org(models.Model):

    objects = None
    name = models.CharField(max_length=100, verbose_name='Наименование')
    inn = models.IntegerField(blank=False, verbose_name='ИНН')
    kpp = models.CharField(max_length=30, blank=True, null=True, verbose_name='КПП')
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name='Город')
    do_atr1 = models.CharField(max_length=30, blank=True, null=True)
    do_atr2 = models.CharField(max_length=30, blank=True, null=True)
    do_atr3 = models.CharField(max_length=30, blank=True, null=True)
    po_atr1 = models.CharField(max_length=30, blank=True, null=True)
    po_atr2 = models.CharField(max_length=30, blank=True, null=True)
    po_atr3 = models.CharField(max_length=30, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('myurl', kwargs={'id': self.name})

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Организации"
        verbose_name_plural = "Организации"
        ordering = ['name']


# class Interaction(models.Model):
#     class Meta:
#         # делает уникальным ид
#         unique_together = ("do", "po")
#     #
#     do = models.ForeignKey(Org, verbose_name='DO', related_name="do", on_delete=models.CASCADE)
#     po = models.ForeignKey(Org, verbose_name='PO', related_name="po", on_delete=models.CASCADE)
#     # do = models.ManyToManyField(Org, related_name="do")
#     # po = models.ManyToManyField(Org, related_name="po")
#     # rate = models.FloatField(verbose_name='Курс')
#     def __str__(self):
#         return f'{self.do} - {self.po}'


class ContractType(models.Model):
    name = models.CharField(max_length=30, verbose_name='Вид договора')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вид договора"
        verbose_name_plural = "Вид договора"
        ordering = ["name"]


class Contract(models.Model):

    # interaction = models.ForeignKey(Interaction, on_delete=models.CASCADE)
    objects = None
    name = models.CharField(max_length=30, verbose_name='Название')
    created_at = models.DateTimeField(editable=True, auto_now_add=True, verbose_name='Создан')
    blob = models.FileField(upload_to='files/%Y/%m/%d/', verbose_name='Файл')
    do = models.ForeignKey(Org, verbose_name='ДО', related_name="do", on_delete=models.PROTECT, default=1)
    po = models.ForeignKey(Org, verbose_name='ПО', related_name="po", on_delete=models.PROTECT, default=11)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=1, verbose_name='Автор')
    type = models.ForeignKey(ContractType, on_delete=models.PROTECT, null=True, verbose_name='Вид договора')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contract_view', kwargs={'contract_id': self.pk})

    class Meta:
        verbose_name = "Договора"
        verbose_name_plural = "Договора"
        ordering = ["name"]


class Role(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        ordering = ["name"]


class UserProfile(models.Model):  # добавляем в юсеров поля
    user = models.OneToOneField(User, on_delete=models.PROTECT, default=1)
    photo = models.ImageField(upload_to='photo/users', verbose_name='Фото')
    role = models.ForeignKey(Role, on_delete=models.PROTECT, verbose_name='ROLE_ID')
    org = models.ForeignKey(Org, on_delete=models.PROTECT, verbose_name='ORG_ID')

    # def __str__(self):
    #     return f'{self.last_name} {self.first_name} - {self.org}'

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class ContractRole(models.Model):

    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, default='1', verbose_name='Договор')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default='2', verbose_name='Должность')
    # contract = ManyToManyField(Contract)
    # role = ManyToManyField(Role)

    class Meta:
        verbose_name = 'Должность по договору'
        verbose_name_plural = 'Должности по договору'
        ordering = ["pk"]


# class Users(models.Model):
#     CHOICES = (
#         ('М', 'Муж'),
#         ('Ж', 'Жен'),
#     )
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     gender = models.CharField(max_length=1, choices=CHOICES, default='М')
#     role = models.ForeignKey(Role, on_delete=models.CASCADE)
#     org = models.ForeignKey(Org, on_delete=models.CASCADE)
#     pwd = models.IntegerField(blank=False)
#
#     def __str__(self):
#         return f'{self.last_name} {self.first_name} - {self.org}'

class ContractUsers(models.Model):

    contract = models.ForeignKey(Contract, on_delete=models.PROTECT)
    users = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Пользователи по договору'
        verbose_name_plural = 'Пользователи по договору'
        ordering = ["users"]


# class Users(models.Model):
#
#     username = models.CharField(max_length=100)
#     fio = models.TextField(blank=True)
#     org_type = models.IntegerField
#     position = models.CharField(max_length=110)
#     created_at = models.DateTimeField(auto_now_add=True)
#     files = models.FileField(upload_to='files/%Y/%m/%d/')
#
#     def __str__(self):
#         return self.username
