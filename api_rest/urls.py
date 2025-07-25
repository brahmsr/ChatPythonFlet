from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path('contacts/', views.contact_list, name='contact_list'),
    path('messages/', views.message_list, name='message_list'),
    path('kanban/', views.contact_kanban_list, name='contact_kanban'),
]