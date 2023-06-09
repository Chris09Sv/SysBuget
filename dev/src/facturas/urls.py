
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'facturas'
urlpatterns = [
        path('create/', views.factura_create_view, name='create'),

]
