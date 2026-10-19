from django.db import models


class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    comuna = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.ciudad}"


class Cliente(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.ForeignKey(Direccion, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class Telefono(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, related_name="telefonos"
    )
    numero = models.CharField(max_length=20)

    def __str__(self):
        return self.numero


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio_actual = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    direccion = models.ForeignKey(Direccion, on_delete=models.PROTECT)
    telefono = models.CharField(max_length=20)
    pagina_web = models.URLField(blank=True)
    producto = models.ForeignKey(
        Producto, on_delete=models.PROTECT, related_name="proveedores"
    )

    def __str__(self):
        return self.nombre


class Venta(models.Model):
    numero_factura = models.CharField(max_length=30, unique=True)
    fecha = models.DateTimeField()
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    monto_final = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.numero_factura


class DetalleVenta(models.Model):
    venta = models.ForeignKey(
        Venta, on_delete=models.CASCADE, related_name="detalles"
    )
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.venta.numero_factura} - {self.producto.nombre}"
