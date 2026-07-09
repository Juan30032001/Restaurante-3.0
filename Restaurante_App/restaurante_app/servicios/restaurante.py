class Restaurante:
    """Servicio principal para administrar productos y clientes."""

    def __init__(self):
        self.productos = []
        self.clientes = []

    def registrar_producto(self, producto):
        self.productos.append(producto)

    def listar_productos(self):
        return self.productos

    def buscar_producto(self, termino):
        criterio = termino.lower().strip()
        return [
            producto
            for producto in self.productos
            if criterio in producto.nombre.lower() or criterio in producto.categoria.lower()
        ]

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        return self.clientes

    def buscar_cliente(self, termino):
        criterio = termino.lower().strip()
        return [
            cliente
            for cliente in self.clientes
            if criterio in cliente.nombre.lower()
            or criterio in cliente.correo.lower()
            or criterio == str(cliente.id_cliente)
        ]
