# Python - Inheritance

## 1. Geometría básica

### Objetivo
Crear una clase `BaseGeometry` que sirva como base para otras clases geométricas.

### Clase BaseGeometry

La clase contiene los siguientes métodos:

- **area()**: lanza una excepción indicando que el método no está implementado.
- **integer_validator(name, value)**: valida que el valor recibido sea un número entero positivo.

### Validaciones

- Si el valor no es un entero, lanza `TypeError`.
- Si el valor es menor o igual a cero, lanza `ValueError`.
- Si el valor es válido, no lanza excepciones.

### Archivos

- `base_geometry.py`: implementación de la clase `BaseGeometry`.
- `main.py`: pruebas de funcionamiento.

### Ejecución

    python3 main.py

### Verificación de estilo

    pycodestyle base_geometry.py
