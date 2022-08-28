from django import template
from contract.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return ContractType.objects.all()