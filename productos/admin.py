from django.contrib import admin
from .models import Productos

class ProductosAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Productos, ProductosAdmin)