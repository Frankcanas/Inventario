import csv
import os

def agregar_producto(inventario, nombre, precio, cantidad):

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print(f" Producto '{nombre}' agregado.")

def mostrar_inventario(inventario):
    """Muestra todos los productos en formato de tabla simple."""
    if not inventario:
        print("\n El inventario está vacío.")
        return
    print("\n--- INVENTARIO ACTUAL ---")
    for p in inventario:
        print(f"ID: {inventario.index(p)+1} | Nombre: {p['nombre']:<15} | Precio: ${p['precio']:>8.2f} | Stock: {p['cantidad']:>5}")

def buscar_producto(inventario, nombre):
    """Busca un producto por nombre y retorna el diccionario o None."""
    for p in inventario:
        if p['nombre'].lower() == nombre.lower():
            return p
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza datos de un producto existente."""
    p = buscar_producto(inventario, nombre)
    if p:
        if nuevo_precio is not None: p['precio'] = nuevo_precio
        if nueva_cantidad is not None: p['cantidad'] = nueva_cantidad
        return True
    return False

def eliminar_producto(inventario, nombre):
    """Elimina un producto de la lista por su nombre."""
    p = buscar_producto(inventario, nombre)
    if p:
        inventario.remove(p)
        return True
    return False

def calcular_estadisticas(inventario):
    """
    Calcula métricas clave del inventario.
    Retorna un diccionario con los resultados.
    """
    if not inventario:
        return None
    
    # Uso de lambda para subtotal como pide la tarea
    get_subtotal = lambda p: p["precio"] * p["cantidad"]
    
    unidades_totales = sum(p['cantidad'] for p in inventario)
    valor_total = sum(get_subtotal(p) for p in inventario)
    
    # Buscamos el más caro y el de mayor stock
    producto_mas_caro = max(inventario, key=lambda x: x['precio'])
    producto_mayor_stock = max(inventario, key=lambda x: x['cantidad'])
    
    return {
        "unidades": unidades_totales,
        "valor": valor_total,
        "caro": producto_mas_caro,
        "stock_max": producto_mayor_stock
    }

# --- PERSISTENCIA (ARCHIVOS) ---

def guardar_csv(inventario, ruta="inventario_total.csv"):
    """Guarda la lista de diccionarios en un archivo CSV."""
    if not inventario:
        print(" No hay datos para guardar.")
        return False
    
    try:
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            campos = ['nombre', 'precio', 'cantidad']
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(inventario)
        print(f"💾 Inventario guardado en: {ruta}")
        return True
    except Exception as e:
        print(f" Error al guardar: {e}")
        return False

def cargar_csv(ruta="inventario_total.csv"):
    """Lee el CSV y valida cada fila antes de retornarla como lista."""
    if not os.path.exists(ruta):
        print(" El archivo no existe todavía.")
        return []

    productos_cargados = []
    errores = 0
    
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for fila in reader:
                try:
                    # Validaciones de formato y valores no negativos
                    nombre = fila['nombre']
                    precio = float(fila['precio'])
                    cantidad = int(fila['cantidad'])
                    
                    if precio < 0 or cantidad < 0:
                        raise ValueError
                        
                    productos_cargados.append({
                        "nombre": nombre, "precio": precio, "cantidad": cantidad
                    })
                except (ValueError, KeyError):
                    errores += 1
        
        if errores > 0:
            print(f" Se omitieron {errores} filas por datos inválidos.")
            
        return productos_cargados
    except Exception as e:
        print(f" Error crítico al cargar: {e}")
        return []
