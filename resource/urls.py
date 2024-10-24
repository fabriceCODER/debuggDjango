from django.urls import path
from . import views

urlpatterns = [
    path('', views.resource_list, name='resource_list'),
    path('new/', views.resource_create, name='resource_create'),
    path('edit/<int:pk>/', views.resource_update, name='resource_update'),
    path('delete/<int:pk>/', views.resource_delete, name='resource_delete'),
]
