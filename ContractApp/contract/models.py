from django.db import models


class Org(models.Model):

    name = models.CharField(max_length=100)
    atr_1 = models.CharField(max_length=30)
    atr_2 = models.CharField(max_length=30)
    atr_3 = models.CharField(max_length=30)
    atr_4 = models.CharField(max_length=30)
    atr_5 = models.CharField(max_length=30)
    atr_6 = models.CharField(max_length=30)
    atr_7 = models.CharField(max_length=30)
    atr_8 = models.CharField(max_length=30)
    atr_9 = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'



class Interaction(models.Model):
    class Meta:
        # делает уникальным ид
        unique_together = ("_do", "_po")

    _do = models.ForeignKey(Org, verbose_name='DO', related_name="do", on_delete=models.CASCADE)
    _po = models.ForeignKey(Org, verbose_name='PO', related_name="po", on_delete=models.CASCADE)

    # rate = models.FloatField(verbose_name='Курс')


class Contract(models.Model):

    interaction_id = models.ForeignKey(Interaction, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    blob = models.FileField(upload_to='files/%Y/%m/%d/')


class Role(models.Model):

    name = models.CharField(max_length=30)


class ContractRole(models.Model):

    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)


class Users(models.Model):

    name = models.CharField(max_length=100)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    org_id = models.ForeignKey(Org, on_delete=models.CASCADE)
    pwd = models.IntegerField(blank=False)


class ContractUsers(models.Model):

    contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE)
    users_id = models.ForeignKey(Users, on_delete=models.CASCADE)


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
