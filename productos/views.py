from django.shortcuts import render, redirect
from .models import Productos
from .forms import ProductosForm
from django.contrib.auth.models import User

# Create your views here.
def productos(request):
    productos = Productos.objects.filter(user=request.user)
    return render(request, 'productos/producto.html', {
        'productos':productos
    })

def crear_productos(request):
    if request.method == 'GET':
        return render(request, 'productos/crear_productos.html', {
            'form':ProductosForm
        })
    else:
        try:
            form = ProductosForm(request.POST)
            new_productos = form.save(commit=True)
            new_productos.user = request.user
            new_productos.save()
            return redirect('producto')
        except:
            return render(request, 'productos/crear_productos.html', {
                'form':ProductosForm,
                'error': 'Error en el ingreso de datos'
            })


