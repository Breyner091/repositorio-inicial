
productos = [
    "Lay's", "Doritos", "Chochlitos", "Cheetos",
    "Mani", "Mani Moto", "Mani con Pasas", "Mani Mixto",
    "Gala", "Chocorramo", "Gansito", "Brownie",
    "Pepsi", "Manzana", "Colombiana", "Uva"
]

precios_pesos = [
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

ventas = [0] * len(productos)
ganancias = 0

TASA_DOLAR = 4000
moneda_actual = "COP"  # Puede ser 'COP' o 'USD'

def main():
    global moneda_actual
    while True:
        print("\n________ MENÚ PRINCIPAL ________")
        print("1. Retirar producto")
        print("2. Inventario")
        print("3. Informes")
        print("4. Configuración")
        print("5. Finalizar")

        opcion = input("Seleccione una opción: ").strip()

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
            print("Opción no válida, por favor intente de nuevo.")

def mostrar_productos():
    print("\nProductos disponibles:")
    for i, producto in enumerate(productos):
        fila, col = divmod(i, 4)
        precio = precios_pesos[i] if moneda_actual == "COP" else round(precios_pesos[i] / TASA_DOLAR, 2)
        unidad_moneda = moneda_actual if moneda_actual == "COP" else "USD"
        print(f"[{fila}{col}] {producto} - ${precio} {unidad_moneda} ({cantidades[i]} disponibles)")

def retirar_producto():
    global ganancias
    print("\n___________ RETIRAR PRODUCTO __________")
    mostrar_productos()

    codigo = input("Ingrese el código del producto (ej. 01): ").strip()
    if len(codigo) != 2 or not codigo.isdigit():
        print("Código inválido. Debe ser dos dígitos numéricos, por ejemplo 01.")
        return

    fila, col = int(codigo[0]), int(codigo[1])

    if fila < 0 or col < 0 or col > 3:
        print("Código no fue encontrado (por favor revisar los numeros que respresentan cada producto).")
        return

    index = fila * 4 + col

    if index < 0 or index >= len(productos):
        print("Código fuera del rango de productos existentes.")
        return

    if cantidades[index] > 0:
        print(f"Producto entregado: {productos[index]}")
        cantidades[index] -= 1
        ganancias += precios_pesos[index]
        ventas[index] += 1
    else:
        print("Producto agotado.")


# Funciones de inventario
def menu_inventario():
    print("\nINVENTARIO")
    print("1. Añadir unidades a un producto")
    print("2. Añadir producto nuevo")
    print("3. Mostrar inventario actual")

    opcion = input("Seleccione una opción: ").strip()
    if opcion == '1':
        mostrar_inventario()
        try:
            idx = int(input("Seleccione el número del producto: ").strip())
            if 0 <= idx < len(productos):
                try:
                    agregar_stock = int(input(f"¿Cuántas unidades desea agregar a '{productos[idx]}'?: ").strip())
                    if agregar_stock < 0:
                        print("No puede ingresar una cantidad negativa.")
                        return
                    if cantidades[idx] + agregar_stock > 99:
                        print("Límite máximo de stock es 99 unidades por producto.")
                        return
                    cantidades[idx] += agregar_stock
                    print(f"Se agregaron {agregar_stock} unidades a '{productos[idx]}'.")
                    print(f"Nuevo stock de '{productos[idx]}': {cantidades[idx]} unidades.")
                    mostrar_inventario()
                except ValueError:
                    print(" Entrada inválida. Debe ingresar un número entero.")
            else:
                print("Índice fuera de rango.")
        except ValueError:
            print("Entrada inválida. Debe ingresar un número.")
    
    elif opcion == '2':
        nombre = input("🆕 Nombre del nuevo producto: ").strip()
        try:
            precio = int(input("💰 Precio del nuevo producto en pesos: ").strip())
            cantidad = int(input("📦 Cantidad inicial: ").strip())
            if precio <= 0 or cantidad < 0:
                print("El precio debe ser positivo y la cantidad no negativa.")
                return
            if cantidad > 99:
                print("La cantidad inicial no puede exceder las 99 unidades.")
                return
            productos.append(nombre)
            precios_pesos.append(precio)
            cantidades.append(cantidad)
            ventas.append(0)
            print(f"✅ Producto '{nombre}' añadido correctamente con {cantidad} unidades a ${precio} COP.")
            mostrar_inventario()
        except ValueError:
            print("Precio y cantidad deben ser números enteros válidos.")
    
    elif opcion == '3':
        mostrar_inventario()
    
    else:
        print("❌ Opción inválida.")

def mostrar_inventario():
    print("\nINVENTARIO ACTUAL")
    for i, nombre in enumerate(productos):
        precio = precios_pesos[i] if moneda_actual == "COP" else round(precios_pesos[i] / TASA_DOLAR, 2)
        unidad_moneda = moneda_actual if moneda_actual == "COP" else "USD"
        print(f"{i}. {nombre} - Precio: ${precio} {unidad_moneda}, Cantidad: {cantidades[i]}")

def informes():
    print("\nINFORMES")
    print(f"Ganancia total en pesos: ${ganancias} COP")
    ganancia_usd = round(ganancias / TASA_DOLAR, 2)
    print(f"Ganancia total en dólares: ${ganancia_usd} USD")

    print("\nVentas por producto:")
    for i, nombre in enumerate(productos):
        if ventas[i] > 0:
            total_cop = ventas[i] * precios_pesos[i]
            total_usd = round(total_cop / TASA_DOLAR, 2)
            print(f"{nombre}: {ventas[i]} unidades - Ganancia: ${total_cop} COP / ${total_usd} USD")

def configuracion():
    global moneda_actual
    print("\nCONFIGURACIÓN")
    print("1. Cambiar moneda")
    print("2. Restaurar valores de fábrica")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        if moneda_actual == "COP":
            moneda_actual = "USD"
            print("Moneda cambiada a dólares.")
        else:
            moneda_actual = "COP"
            print("Moneda cambiada a pesos colombianos.")
    elif opcion == '2':
        restaurar_valores_fabrica()
    else:
        print("Opción inválida.")

def restaurar_valores_fabrica():
    global productos, precios_pesos, cantidades, ganancias, ventas, moneda_actual
    productos = [
        "Lay's", "Doritos", "Chochlitos", "Cheetos",
        "Mani", "Mani Moto", "Mani con Pasas", "Mani Mixto",
        "Gala", "Chocorramo", "Gansito", "Brownie",
        "Pepsi", "Manzana", "Colombiana", "Uva"
    ]
    precios_pesos = [
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
    moneda_actual = "COP"
    print("Sistema restaurado a valores de fábrica.")

if __name__ == "__main__":
    main()
