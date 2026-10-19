from django.contrib import admin
from .models import (
    Direccion,
    Cliente,
    Telefono,
    Categoria,
    Producto,
    Proveedor,
    Venta,
    DetalleVenta,
)

admin.site.register(Direccion)
admin.site.register(Cliente)
admin.site.register(Telefono)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Venta)
admin.site.register(DetalleVenta)