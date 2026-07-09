from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.cliente import Cliente
from restaurante_app.servicios.restaurante import Restaurante


def mostrar_menu():
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("----------------------------------------")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("----------------------------------------")
    print("7. Salir")


def registrar_producto(restaurante):
    try:
        nombre = input("Ingrese el nombre del producto: ").strip()
        categoria = input("Ingrese la categoría del producto: ").strip()
        precio = input("Ingrese el precio del producto: ").strip()
        disponible_input = input("¿Está disponible? (s/n): ").strip().lower()

        disponible = disponible_input in {"s", "si", "sí", "y", "yes"}
        producto = Producto(nombre=nombre, categoria=categoria, precio=precio, disponible=disponible)
        restaurante.registrar_producto(producto)
        print("\nProducto registrado correctamente.")
    except ValueError as error:
        print(f"\nError: {error}")


def listar_productos(restaurante):
    productos = restaurante.listar_productos()
    if not productos:
        print("\nNo hay productos registrados.")
        return

    print("\nProductos registrados:")
    for producto in productos:
        print("-" * 30)
        print(producto.mostrar_informacion())


def buscar_producto(restaurante):
    termino = input("Ingrese el nombre o categoría del producto a buscar: ").strip()
    resultados = restaurante.buscar_producto(termino)
    if not resultados:
        print("\nNo se encontraron productos.")
        return

    print("\nResultados de búsqueda:")
    for producto in resultados:
        print("-" * 30)
        print(producto.mostrar_informacion())


def registrar_cliente(restaurante):
    try:
        nombre = input("Ingrese el nombre del cliente: ").strip()
        correo = input("Ingrese el correo del cliente: ").strip()
        id_cliente = int(input("Ingrese el identificador del cliente: ").strip())

        cliente = Cliente(nombre=nombre, correo=correo, id_cliente=id_cliente)
        restaurante.registrar_cliente(cliente)
        print("\nCliente registrado correctamente.")
    except ValueError as error:
        print(f"\nError: {error}")


def listar_clientes(restaurante):
    clientes = restaurante.listar_clientes()
    if not clientes:
        print("\nNo hay clientes registrados.")
        return

    print("\nClientes registrados:")
    for cliente in clientes:
        print("-" * 30)
        print(f"ID: {cliente.id_cliente}")
        print(f"Nombre: {cliente.nombre}")
        print(f"Correo: {cliente.correo}")


def buscar_cliente(restaurante):
    termino = input("Ingrese el nombre, correo o ID del cliente a buscar: ").strip()
    resultados = restaurante.buscar_cliente(termino)
    if not resultados:
        print("\nNo se encontraron clientes.")
        return

    print("\nResultados de búsqueda:")
    for cliente in resultados:
        print("-" * 30)
        print(f"ID: {cliente.id_cliente}")
        print(f"Nombre: {cliente.nombre}")
        print(f"Correo: {cliente.correo}")


def main():
    restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto(restaurante)
        elif opcion == "2":
            listar_productos(restaurante)
        elif opcion == "3":
            buscar_producto(restaurante)
        elif opcion == "4":
            registrar_cliente(restaurante)
        elif opcion == "5":
            listar_clientes(restaurante)
        elif opcion == "6":
            buscar_cliente(restaurante)
        elif opcion == "7":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
