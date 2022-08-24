from django import template
from contract.models import *

register = template.Library()

def get_categories():
    return Contract.objects.all()