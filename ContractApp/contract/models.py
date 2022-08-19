from django.db import models


class Org(models.Model):

    name = models.CharField(max_length=100)
    inn = models.IntegerField(blank=False)
    kpp = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, null=True)
    do_atr1 = models.CharField(max_length=30, blank=True, null=True)
    do_atr2 = models.CharField(max_length=30, blank=True, null=True)
    do_atr3 = models.CharField(max_length=30, blank=True, null=True)
    po_atr1 = models.CharField(max_length=30, blank=True, null=True)
    po_atr2 = models.CharField(max_length=30, blank=True, null=True)
    po_atr3 = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Interaction(models.Model):
    class Meta:
        # делает уникальным ид
        unique_together = ("do", "po")
    #
    do = models.ForeignKey(Org, verbose_name='DO', related_name="do", on_delete=models.CASCADE)
    po = models.ForeignKey(Org, verbose_name='PO', related_name="po", on_delete=models.CASCADE)
    # do = models.ManyToManyField(Org, related_name="do")
    # po = models.ManyToManyField(Org, related_name="po")
    # rate = models.FloatField(verbose_name='Курс')
    def __str__(self):
        return f'{self.do} - {self.po}'


class Contract(models.Model):

    interaction = models.ForeignKey(Interaction, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(editable=True, auto_now_add=True)
    blob = models.FileField(upload_to='files/%Y/%m/%d/')

    def __str__(self):
        return self.name


class Role(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ContractRole(models.Model):

    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class Users(models.Model):

    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    org = models.ForeignKey(Org, on_delete=models.CASCADE)
    pwd = models.IntegerField(blank=False)

    def __str__(self):
        return self.Lastname

class ContractUsers(models.Model):

    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)


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
