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

## 2. Rectángulo

### Objetivo
Crear una clase `Rectangle` que herede de `BaseGeometry`.

### Clase Rectangle

- Hereda de la clase `BaseGeometry`.
- Recibe `width` (ancho) y `height` (altura) en el constructor.
- Ambos atributos son privados.
- No dispone de getters ni setters.
- Valida ambas dimensiones utilizando `integer_validator()` de la clase padre.
- Las dimensiones deben ser enteros positivos.

### Archivos

- `1-rectangle.py`: implementación de la clase `Rectangle`.

### Ejecución

    python3 -c "Rectangle = __import__('1-rectangle').Rectangle; r = Rectangle(3, 5); print(r)"

### Verificación de estilo

    pycodestyle base_geometry.py 1-rectangle.py

## 3. Rectángulo completo

### Objetivo
Extender la clase `Rectangle` para implementar el cálculo del área y su representación en cadena.

### Funcionalidades

- `area()`: calcula el área multiplicando el ancho por la altura.
- `__str__()`: devuelve la descripción `[Rectangle] <width>/<height>`.
- Mantiene los atributos privados `width` y `height`.
- Conserva la validación heredada de `BaseGeometry`.

### Archivo

- `2-rectangle.py`: implementación completa de la clase `Rectangle`.

### Ejecución

    python3 -c "Rectangle = __import__('2-rectangle').Rectangle; r = Rectangle(3, 5); print(r); print(r.area())"

### Verificación de estilo

    pycodestyle base_geometry.py 1-rectangle.py 2-rectangle.py

## 4. Cuadrado #1

### Objetivo
Crear una clase `Square` que herede de `Rectangle`.

### Funcionalidades

- Recibe un único parámetro `size`.
- El atributo `size` es privado.
- Valida que `size` sea un entero positivo mediante `integer_validator()`.
- Inicializa la clase padre con el mismo ancho y altura.
- Implementa `area()` para calcular la superficie del cuadrado.

### Archivo

- `1-square.py`: implementación de la clase `Square`.

### Ejecución

    python3 -c "Square = __import__('1-square').Square; s = Square(13); print(s); print(s.area())"

### Verificación de estilo

    pycodestyle base_geometry.py 1-rectangle.py 2-rectangle.py 1-square.py

## 5. Cuadrado #2

### Objetivo
Extender la clase `Square` para incorporar su propia representación en cadena.

### Funcionalidades

- Hereda de la clase `Square` del ejercicio anterior.
- Implementa `__str__()`.
- La representación devuelve `[Square] <width>/<height>`.
- Mantiene el cálculo del área y las validaciones heredadas.

### Archivo

- `2-square.py`: implementación de la representación completa del cuadrado.

### Ejecución

    python3 -c "Square = __import__('2-square').Square; s = Square(13); print(s); print(s.area())"

### Verificación de estilo

    pycodestyle base_geometry.py 1-rectangle.py 2-rectangle.py 1-square.py 2-square.py

### Reflexión: polimorfismo

Las clases `Rectangle` y `Square` comparten métodos como `area()`, pero cada una puede proporcionar su propia implementación. Esto permite trabajar con diferentes figuras geométricas mediante una interfaz común.
