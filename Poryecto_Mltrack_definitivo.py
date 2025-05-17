import json

productos = []
pedidos = []

# ---------------- FUNCIONES DE ARCHIVOS ----------------

def guardar_datos():
    with open("productos.json", "w") as f:
        json.dump(productos, f)
    with open("pedidos.json", "w") as f:
        json.dump(pedidos, f)
    print("Datos guardados correctamente.")

def cargar_datos():
    global productos, pedidos
    try:
        with open("productos.json", "r") as f:
            productos = json.load(f)
        with open("pedidos.json", "r") as f:
            pedidos = json.load(f)
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontraron archivos de datos anteriores.")

# ---------------- FUNCIONES PRINCIPALES ----------------

def mostrar_menu():
    print("\n--- MLTrack Consola ---")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Crear nuevo pedido")
    print("4. Agregar producto a un pedido")
    print("5. Ver pedidos")
    print("6. Cambiar estado de pedido")
    print("7. Procesar pago de un pedido")
    print("8. Guardar datos")
    print("9. Cargar datos")
    print("10. Asistente (bot de ayuda)")
    print("11. Salir")

def agregar_producto():
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    stock = int(input("Stock disponible: "))
    producto = {
        "id": len(productos) + 1,
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }
    productos.append(producto)
    print("Producto agregado.")

def listar_productos():
    print("\n--- Productos ---")
    for p in productos:
        print(f"{p['id']}. {p['nombre']} - ${p['precio']} (Stock: {p['stock']})")

def crear_pedido():
    pedido = {
        "id": len(pedidos) + 1,
        "productos": [],
        "estado": "Pendiente",
        "pagado": False
    }
    pedidos.append(pedido)
    print(f"Pedido #{pedido['id']} creado.")

def agregar_producto_a_pedido():
    if not pedidos:
        print("No hay pedidos creados.")
        return
    listar_productos()
    id_prod = int(input("ID del producto: "))
    cantidad = int(input("Cantidad: "))
    id_pedido = int(input("ID del pedido: "))
    
    producto = next((p for p in productos if p["id"] == id_prod), None)
    if producto and producto["stock"] >= cantidad:
        producto["stock"] -= cantidad
        item = {"producto": producto["nombre"], "cantidad": cantidad, "subtotal": cantidad * producto["precio"]}
        pedidos[id_pedido - 1]["productos"].append(item)
        print("Producto agregado al pedido.")
    else:
        print("Producto no encontrado o stock insuficiente.")

def ver_pedidos():
    print("\n--- Pedidos ---")
    for p in pedidos:
        print(f"Pedido #{p['id']} - Estado: {p['estado']} - Pagado: {'Sí' if p['pagado'] else 'No'}")
        for item in p["productos"]:
            print(f"  {item['cantidad']} x {item['producto']} = ${item['subtotal']}")
        total = sum(item['subtotal'] for item in p["productos"])
        print(f"  Total: ${total}")

def cambiar_estado_pedido():
    id_pedido = int(input("ID del pedido: "))
    nuevo_estado = input("Nuevo estado (Pendiente/Pagado/Enviado/Entregado): ")
    if 0 < id_pedido <= len(pedidos):
        pedidos[id_pedido - 1]["estado"] = nuevo_estado
        print("Estado actualizado.")
    else:
        print("Pedido no encontrado.")

def procesar_pago():
    id_pedido = int(input("ID del pedido a pagar: "))
    if 0 < id_pedido <= len(pedidos):
        pedido = pedidos[id_pedido - 1]
        if not pedido["pagado"]:
            pedido["pagado"] = True
            pedido["estado"] = "Pagado"
            print("Pago procesado correctamente.")
        else:
            print("Este pedido ya está pagado.")
    else:
        print("Pedido no encontrado.")

# ---------------- ASISTENTE BOT ----------------

def asistente():
    print("\nAsistente MLTrack - Preguntas Frecuentes")
    print("Puedes preguntar cosas como:")
    print("- ¿Cómo creo un pedido?")
    print("- ¿Qué es MLTrack?")
    print("- ¿Cómo agregar productos?")
    print("- salir (para volver al menú)")
    while True:
        pregunta = input("\nTú: ").lower()
        if "crear pedido" in pregunta:
            print("Bot: Para crear un pedido, selecciona la opción 3 del menú principal.")
        elif "mltrack" in pregunta:
            print("Bot: MLTrack es un sistema que simula la gestión de pedidos e inventario de una tienda online.")
        elif "agregar producto" in pregunta:
            print("Bot: Usa la opción 1 del menú para ingresar nuevos productos con nombre, precio y stock.")
        elif "salir" in pregunta:
            print("Bot: ¡Hasta luego!")
            break
        else:
            print("Bot: Lo siento, no entiendo esa pregunta. Intenta con otra.")

# ---------------- BUCLE PRINCIPAL ----------------

cargar_datos()
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        listar_productos()
    elif opcion == "3":
        crear_pedido()
    elif opcion == "4":
        agregar_producto_a_pedido()
    elif opcion == "5":
        ver_pedidos()
    elif opcion == "6":
        cambiar_estado_pedido()
    elif opcion == "7":
        procesar_pago()
    elif opcion == "8":
        guardar_datos()
    elif opcion == "9":
        cargar_datos()
    elif opcion == "10":
        asistente()
    elif opcion == "11":
        print("Gracias por usar MLTrack.")
        break
    else:
        print("Opción inválida.")