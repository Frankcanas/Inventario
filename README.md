# Sistema de Ingreso de Inventario (Python)

Este es un script de consola diseñado para gestionar de manera segura la entrada de productos a un sistema de inventario. 

El programa se enfoca en la integridad de los datos, obligando al usuario a ingresar valores numéricos válidos antes de proceder con los cálculos.

# 📋 Función del Programa

La función principal es registrar un producto individual, capturando su nombre, precio unitario y stock disponible. 
El script calcula automáticamente el valor total de la existencia (Precio × Cantidad) y presenta un resumen limpio al finalizar.

# 🚀 Funcionalidades y Procesos

El código ejecuta los siguientes procesos de manera secuencial:


1. Captura de Identidad: Solicita el nombre del producto (cadena de texto).

2. Validación de Precio (Float): Implementa un bucle while que no permite avanzar hasta que se ingrese un número decimal válido. Maneja errores de tipo ValueError.

3. Validación de Cantidad (Int): Similar al proceso anterior, pero restringe la entrada exclusivamente a números enteros.

4. Cálculo Aritmético: Aplica la fórmula:
 
                                           Costo_Total = Precio * Cantidad

5. Generación de Reporte: Muestra en una sola línea formateada (f-string) todos los datos recolectados para una lectura rápida.


# 💻 ¿Por dónde se puede correr?

Al ser un script de Python estándar (.py), puedes ejecutarlo en:

    •  IDEs de Desarrollo: Visual Studio Code, PyCharm o Spyder 
  
    • Entornos Interactivos: Jupyter Notebook o Google Colab.
  
    • Terminal/Consola: Cualquier terminal de Windows (CMD/PowerShell), macOS o Linux que tenga Python instalado.
  
  # 🛠️ Cómo correr el código 
  
  Sigue estos pasos para probar el script en tu máquina local:
  
  1. Instalar Python: Asegúrate de tener instalada una versión de Python 3.x.
  
  2. Preparar el archivo: Copia el código y guárdalo en un archivo llamado inventario.py.
  
  # Ejecución desde la terminal: 
  Abre tu terminal o consola de comandos.
  Navega hasta la carpeta donde guardaste el archivo.
  Escribe el siguiente comando y presiona Enter:

  ``` python
  python inventario.py
  ```
