from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductosForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required  
def listar_productos(request):
    productos = Productos.objects.filter(user=request.user)
    return render(request, 'productos/listar_productos.html', {
        'productos':productos
    })



