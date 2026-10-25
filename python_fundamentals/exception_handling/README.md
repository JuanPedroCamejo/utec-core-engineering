# Exception Handling - UTEC

## Tarea 0: Impresión segura de listas

Archivo: `safe_print_list.py`

### Objetivo
Imprimir de forma segura una cantidad determinada de elementos de una lista.

### Funcionamiento
- Recibe una lista y la cantidad de elementos a imprimir.
- Imprime los elementos en una misma línea, sin espacios adicionales.
- Utiliza try y except IndexError para controlar accesos fuera de los límites.
- Si la lista tiene menos elementos de los solicitados, detiene la impresión.
- Imprime una nueva línea al finalizar.
- Devuelve la cantidad real de elementos impresos.

### Restricciones
- No importa módulos.
- No utiliza len().
- Compatible con Python 3.8 y PEP 8.

### Ejemplo
La llamada `safe_print_list([1, 2, 3, 4, 5], 2)` imprime `12` y devuelve `2`.
