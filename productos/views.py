from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductosForm
from django.contrib.auth.models import User

# Create your views here.
 
def listar_productos(request):
    productos = Productos.objects.all()
    return render(request, 'productos/listar_productos.html', {
        'productos':productos
    })



