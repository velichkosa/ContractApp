from django.urls import path
from .views import *


urlpatterns = [
    path('', Authentication.as_view(), name='login'),
    path('test/', test),
    path('contract/', contract),
    path('home/', home),

]