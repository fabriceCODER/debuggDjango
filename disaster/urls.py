from django.urls import path
from . import views

urlpatterns = [
    path('', views.disaster_list, name='disaster_list'),
    path('new/', views.disaster_create, name='disaster_create'),
    path('edit/<int:pk>/', views.disaster_update, name='disaster_update'),
    path('delete/<int:pk>/', views.disaster_delete, name='disaster_delete'),
]
