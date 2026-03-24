# 📦 Sistema de Gestión de Inventario Avanzado

Este proyecto es una aplicación de consola en **Python** diseñada para administrar el inventario de un negocio de manera eficiente. Permite realizar operaciones CRUD, calcular estadísticas críticas y mantener la persistencia de los datos mediante archivos CSV.

---

## 🛠️ Estructura del Proyecto

El sistema está dividido en dos módulos principales para seguir las mejores prácticas de desarrollo (separación de lógica e interfaz):

* **`funciones.py`**: Contiene toda la lógica de negocio, manipulación de la lista de diccionarios, cálculos de estadísticas y gestión de lectura/escritura del archivo CSV.
* **`main.py`**: Es el punto de entrada del programa. Gestiona el menú interactivo, las entradas del usuario (`input`) y las validaciones de datos.

---

## 🚀 Funcionalidades Principales

1.  **Gestión Completa (CRUD):** * Agregar productos con nombre, precio y cantidad.
    * Buscar productos por nombre.
    * Actualizar stock y precios de productos existentes.
    * Eliminar registros del sistema.
2.  **Estadísticas de Negocio:**
    * Cálculo automático de unidades totales en bodega.
    * Valorización monetaria del inventario total ($Precio \times Cantidad$).
    * Identificación del producto más caro y el de mayor existencia.
3.  **Persistencia CSV (`inventario_total.csv`):**
    * **Guardar:** Exporta el estado actual del inventario a un archivo compatible con Excel.
    * **Cargar:** Importa datos externos con opción de **Sobrescribir** o **Fusionar** (suma cantidades y actualiza precios si el producto ya existe).

---

## 📋 Requisitos y Ejecución

1.  Tener instalado **Python 3.x**.
2.  Descargar `app.py` y `funciones.py` en la misma carpeta.
3.  Ejecutar el comando:
    ```bash
    python app.py
    ```

---

## 📝 Notas de Implementación

* **Validación de Datos:** El sistema utiliza bloques `try-except` para asegurar que el programa no se cierre si el usuario ingresa datos erróneos o valores negativos.
* **Modularidad:** Las funciones están documentadas con *docstrings* y utilizan tipos de datos compuestos (listas de diccionarios).
* **Eficiencia:** Se emplea el módulo nativo `csv` de Python para garantizar un manejo limpio de los registros.

---
Generado para el proyecto de Inventario - Marzo 2026
