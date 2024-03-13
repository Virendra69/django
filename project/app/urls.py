from django.urls import path
from .views import *

urlpatterns = [
    path('', indexPage, name='indexPage'),
    path('create-task/', createTask, name='createTask'),
]