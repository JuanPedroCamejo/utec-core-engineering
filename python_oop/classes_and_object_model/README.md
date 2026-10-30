# Python - Classes and Object Model

## Descripción

Este directorio contiene ejercicios prácticos de Python relacionados con la programación orientada a objetos (OOP).

El objetivo es aprender a crear clases, instanciar objetos y comprender cómo funciona el modelo de objetos de Python.

## Objetivos

- Comprender el concepto de clases y objetos.
- Crear clases utilizando la palabra reservada `class`.
- Crear instancias a partir de una clase.
- Comprender los atributos y métodos de los objetos.
- Aprender a utilizar los métodos especiales de Python.

## Ejercicios

### 0. My First Square

**Archivo:** `0-square.py`

**Objetivo:** Crear una primera clase llamada `Square` que represente un cuadrado.

**Requisitos:**
- Definir una clase llamada `Square`.
- La clase no debe contener atributos ni métodos.
- Utilizar `pass` para mantener la clase vacía.

**Ejemplo de uso:**

```python
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
```

**Resultado esperado:**

```text
<class '0-square.Square'>
{}
```

## Entorno de desarrollo

- Lenguaje: Python 3
- Sistema operativo: Linux (Docker)
- Editor: Visual Studio Code
- Repositorio: `utec-core-engineering`

## Ejecución

Para ejecutar los ejercicios desde la terminal, ubicarse en el directorio correspondiente y utilizar:

```bash
python3 0-main.py
```

## Autor

Juan Pedro Camejo

## Institución

UTEC - Universidad Tecnológica del Uruguay