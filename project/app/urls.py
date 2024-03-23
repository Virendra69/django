from django.urls import path
from .views import *

urlpatterns = [
    path('', indexPage, name='indexPage'),
    path('create-task/', createTask, name='createTask'),
    path('delete-task/<int:task_id>/', deleteTask, name='deleteTask'),
]