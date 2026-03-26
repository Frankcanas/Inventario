import csv
import os

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