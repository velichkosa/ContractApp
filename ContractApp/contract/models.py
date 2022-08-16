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


class Interaction(models.Model):

    do_id = models.IntegerField(blank=False)
    po_id = models.IntegerField(blank=False)


class Contract(models.Model):

    interaction_id = models.IntegerField(blank=False)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    blob = models.FileField(upload_to='files/%Y/%m/%d/')


class Role(models.Model):

    name = models.CharField(max_length=30)


class ContractRole(models.Model):

    contract_id = models.IntegerField(blank=False)
    role_id = models.IntegerField(blank=False)


class Users(models.Model):

    name = models.CharField(max_length=100)
    role_id = models.IntegerField(blank=False)
    org_id = models.IntegerField(blank=False)


class ContractUsers(models.Model):

    contract_id = models.IntegerField(blank=False)
    users_id = models.IntegerField(blank=False)


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
