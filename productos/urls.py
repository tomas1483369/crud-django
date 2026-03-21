from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.productos, name='productos'),
    path('crear_productos/', views.crear_productos, name='crear_productos'),
]   