
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'clientes'
urlpatterns = [
        path('create/', views.cliente_create_view, name='create'),

]
