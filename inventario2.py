# Lista global para almacenar los productos del inventario
inventario = []

def agregar_producto():
    # Permite ingresar datos de un producto sin usar While True.
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Ingrese el nombre del producto: ")
    
    # Validación de precio con variable de control
    precio_valido = False
    precio = 0.0
    while not precio_valido:
        try:
            entrada_precio = float(input("Ingrese el precio del producto: "))
            if entrada_precio >= 0:
                precio = entrada_precio
                precio_valido = True
            else:
                print("Error: El precio no puede ser negativo.")
        except ValueError:
            print("Error: El precio debe ser un valor numérico.")
        except:
            print("Error: Entrada inválida para el precio.")

            
    # Validación de cantidad con variable de control
    cantidad_valida = False
    cantidad = 0
    while not cantidad_valida:
        try:
            entrada_cantidad = int(input("Ingrese la cantidad del producto: "))
            if entrada_cantidad >= 0:
                cantidad = entrada_cantidad
                cantidad_valida = True
            else:
                print("Error: La cantidad no puede ser negativa.")
        except ValueError:
            print("Error: La cantidad debe ser un número entero.")

    # TASK 2: Estructura de diccionario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    inventario.append(producto)
    print(f"¡Producto '{nombre}' añadido correctamente!")

def mostrar_inventario():
    """TASK 3: Muestra los productos usando un bucle for."""
    print("\n--- Inventario Actual ---")
    if len(inventario) == 0:
        print("El inventario está actualmente vacío.")
    else:
        for p in inventario:
            print(f"Producto: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")

def calcular_estadisticas():
    """TASK 4: Cálculo de totales acumulados."""
    print("\n--- Estadísticas del Inventario ---")
    if not inventario:
        print("No hay productos registrados para calcular estadísticas.")
        return

    valor_total = 0
    unidades_totales = 0

    for p in inventario:
        valor_total += (p['precio'] * p['cantidad'])
        unidades_totales += p['cantidad']

    print(f"Total de productos en stock: {unidades_totales}")
    print(f"Valor total del inventario: ${valor_total:,.2f}")

def menu_principal():
    """TASK 1 & 2: Menú interactivo usando una variable de control para el bucle."""
    ejecutando = True  # Reemplaza el 'True' directo en el while
    
    while ejecutando:
        print("\n========== SISTEMA DE INVENTARIO ==========")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadísticas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            calcular_estadisticas()
        elif opcion == "4":
            print("Cerrando el sistema de gestión. ¡Buen día!")
            ejecutando = False  # Cambiamos el estado para finalizar el bucle
        else:
            print("Error: Opción inválida. Intente con los números del 1 al 4.")

# Ejecución principal
if __name__ == "__main__":
    menu_principal()

# OBJETIVO DE LA SEMANA:
# Desarrollar una aplicación de consola en Python que integre el uso de funciones, 
# listas de diccionarios y control de flujo mediante variables de estado, 
# garantizando la integridad de los datos ingresados por el usuario.