
productos = [
    "Lay's", "Doritos", "Chochlitos", "Cheetos",
    "Mani", "Mani Moto", "Mani con Pasas", "Mani Mixto",
    "Gala", "Chocorramo", "Gansito", "Brownie",
    "Pepsi", "Manzana", "Colombiana", "Uva"
]

precios = [
    1000, 1500, 500, 900,
    500, 700, 600, 800,
    1000, 1800, 900, 2500,
    1500, 1500, 1500, 1500
]

cantidades = [
    5, 5, 5, 5,
    5, 5, 5, 5,
    5, 5, 5, 5,
    5, 5, 5, 4
]

ganancias = 0
ventas = [0] * len(productos)

# Función principal
def run():
    while True:
        print("\n________ MENÚ PRINCIPAL ________")
        print("1. Retirar producto")
        print("2. Inventario")
        print("3. Informes")
        print("4. Configuración")
        print("5. Finalizar")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            retirar_producto()
        elif opcion == '2':
            menu_inventario()
        elif opcion == '3':
            informes()
        elif opcion == '4':
            configuracion()
        elif opcion == '5':
            print("Fin del programa.")
            break
        else:
            print("Opción no válida.")

# Función para retirar producto
def retirar_producto():
    global ganancias
    print("\n___________ RETIRAR PRODUCTO __________")
    for i in range(len(productos)):
        print(f"[{i//4}{i%4}] {productos[i]} - ${precios[i]} ({cantidades[i]} disponibles)")

    codigo = input("Ingrese el código del producto (ej. 01): ")
    try:
        fila = int(codigo[0])
        col = int(codigo[1])
        index = fila * 4 + col
        if cantidades[index] > 0:
            print(f"Producto entregado: {productos[index]}")
            cantidades[index] -= 1
            ganancias += precios[index]
            ventas[index] += 1
        else:
            print("Producto agotado.")
    except:
        print("Código inválido.")

# Funciones de inventario
def menu_inventario():
    print("\nINVENTARIO")
    print("1. Añadir unidad a un producto")
    print("2. Añadir producto nuevo")
    print("3. Mostrar inventario actual")

    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        mostrar_inventario()
        idx = int(input("Seleccione el número del producto: "))
        cantidades[idx] += 1
        print("Unidad añadida.")
    elif opcion == '2':
        nombre = input("Nombre del nuevo producto: ")
        precio = int(input("Precio del nuevo producto: "))
        cantidad = int(input("Cantidad inicial: "))
        productos.append(nombre)
        precios.append(precio)
        cantidades.append(cantidad)
        ventas.append(0)
        print("Producto añadido.")
    elif opcion == '3':
        mostrar_inventario()
    else:
        print("Opción inválida.")

def mostrar_inventario():
    print("\nINVENTARIO ACTUAL")
    for i, nombre in enumerate(productos):
        print(f"{i}. {nombre} - Precio: ${precios[i]}, Cantidad: {cantidades[i]}")


# Informes
def informes():
    print("\n--- INFORMES ---")
    print(f"Ganancia total: ${ganancias}")
    print("Ventas por producto:")
    for i in range(len(productos)):
        if ventas[i] > 0:
            print(f"{productos[i]}: {ventas[i]} unidades - Ganancia: ${ventas[i] * precios[i]}")

# Configuración
def configuracion():
    print("\nCONFIGURACIÓN")
    print("1. Cambiar moneda")
    print("2. Restaurar valores de fábrica")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        conversion_de_moneda()
        print("Moneda cambiada a dólares.")
    elif opcion == '2':
        restaurar_valores_fabrica()


def conversion_de_moneda():
    for i in range(len(precios)):
        precios[i] = float(round(precios[i] * 0.00025, 2))
        # Cambia el precio a dólares (suponiendo que 1 dólar = 4000 pesos)


def restaurar_valores_fabrica():
    global productos, precios, cantidades, ganancias, ventas
    productos = [
        "Lay's", "Doritos", "Chochlitos", "Cheetos",
        "Mani", "Mani Moto", "Mani con Pasas", "Mani Mixto",
        "Gala", "Chocorramo", "Gansito", "Brownie",
        "Pepsi", "Manzana", "Colombiana", "Uva"
    ]
    precios = [
        1000, 1500, 500, 900, 
        500, 700, 600, 800,
        1000, 1800, 900, 2500,
        1500, 1500, 1500, 1500
    ]
    cantidades = [5] * 15 + [4]
    ganancias = 0
    ventas = [0] * len(productos)
    print("Sistema restaurado a valores de fábrica.")


# Ejecutar el sistema
run()

