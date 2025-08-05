from django.contrib import admin
from django.urls import path
from knox import views as knox_views
from .views import LoginAPI

from .import views

urlpatterns = [
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/<int:id>/', views.contact_list, name='contact_detail'),
    path('contacts/create/', views.contact_create, name='contact_create'),
    path('contacts/<int:id>/update/', views.contact_update, name='contact_update'),
    path('contacts/<int:id>/delete/', views.contact_delete, name='contact_delete'),
    
    path('messages/', views.message_list, name='message_list'),
    path('kanban/', views.contact_kanban_list, name='contact_kanban'),
    
    path('contacts/<str:name>', views.contact_list, name='contact_detail'),
    # path('kanban/<int:pk>/', views.contact_kanban_detail, name='contact_kanban_detail'),
    # path('kanban/<int:pk>/update/', views.contact_kanban_update, name='contact_kanban_update'),
    # path('kanban/<int:pk>/delete/', views.contact_kanban_delete, name='contact_kanban_delete'),
    # path('kanban/create/', views.contact_kanban_create, name='contact_kanban_create'),
    # path('kanban/<int:pk>/messages/', views.message_list, name='message_list'),
    # path('kanban/<int:pk>/messages/create/', views.message_create, name='message_create'),
    # path('kanban/<int:pk>/messages/<int:message_pk>/', views.message_detail, name='message_detail'),
    # path('kanban/<int:pk>/messages/<int:message_pk>/update/', views.message_update, name='message_update'),
    # path('kanban/<int:pk>/messages/<int:message_pk>/delete/', views.message_delete, name='message_delete'),
    
    path('dashboard/stats/', views.dashboard_stats, name='dashboard_stats'),
    path('dashboard/users/', views.dashboard_users, name='dashboard_users'),
    
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
]