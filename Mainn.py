from funciones import *

def solicitar_numero(mensaje, tipo=float):
    """Función auxiliar para validar entradas numéricas del usuario."""
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor < 0:
                print("Error: El valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print(f"Error: Ingrese un número válido ({tipo.__name__}).")

def ejecutar_menu():
    inventario = []
    archivo_default = "inventario_total.csv"

    while True:
        print("\n" + "="*30)
        print("  SISTEMA DE GESTIÓN AVANZADA")
        print("="*30)
        print("1. Agregar Producto")
        print("2. Mostrar Inventario")
        print("3. Buscar Producto")
        print("4. Actualizar Producto")
        print("5. Eliminar Producto")
        print("6. Ver Estadísticas")
        print("7. Guardar en CSV")
        print("8. Cargar desde CSV")
        print("9. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            precio = solicitar_numero("Precio: ", float)
            cantidad = solicitar_numero("Cantidad: ", int)
            agregar_producto(inventario, nombre, precio, cantidad)

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            p = buscar_producto(inventario, nombre)
            if p:
                print(f"Encontrado: {p['nombre']} - ${p['precio']} - Stock: {p['cantidad']}")
            else:
                print(" Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del producto a actualizar: ")
            if buscar_producto(inventario, nombre):
                np = solicitar_numero("Nuevo Precio: ", float)
                nc = solicitar_numero("Nueva Cantidad: ", int)
                actualizar_producto(inventario, nombre, np, nc)
                print(" Actualizado.")
            else:
                print(" No existe el producto.")

        elif opcion == "5":
            nombre = input("Nombre a eliminar: ")
            if eliminar_producto(inventario, nombre):
                print(" Producto eliminado.")
            else:
                print(" No se encontró el producto.")

        elif opcion == "6":
            stats = calcular_estadisticas(inventario)
            if stats:
                print("\n--- RESUMEN DE NEGOCIO ---")
                print(f" Unidades totales: {stats['unidades']}")
                print(f" Valor total: ${stats['valor']:,.2f}")
                print(f" Más caro: {stats['caro']['nombre']} (${stats['caro']['precio']})")
                print(f" Mayor stock: {stats['stock_max']['nombre']} ({stats['stock_max']['cantidad']} unds)")
            else:
                print(" No hay datos para estadísticas.")

        elif opcion == "7":
            guardar_csv(inventario, archivo_default)

        elif opcion == "8":
            nuevos_datos = cargar_csv(archivo_default)
            if nuevos_datos:
                modo = input("¿Sobrescribir inventario actual? (S/N): ").upper()
                if modo == 'S':
                    inventario = nuevos_datos
                    print(" Inventario reemplazado.")
                else:
                    # Fusión: si existe suma cantidad y actualiza precio
                    for nd in nuevos_datos:
                        p_existente = buscar_producto(inventario, nd['nombre'])
                        if p_existente:
                            p_existente['cantidad'] += nd['cantidad']
                            p_existente['precio'] = nd['precio']
                        else:
                            inventario.append(nd)
                    print(" Inventario fusionado.")

        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print(" Opción inválida.")

if __name__ == "__main__":
    ejecutar_menu()
