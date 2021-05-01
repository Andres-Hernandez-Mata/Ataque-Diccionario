# Ataque-Diccionario
Ataque de diccionario

## Introducción
Este tipo de ataque consiste en intentar averiguar una clave o contraseña probando palabras provenientes de un diccionario, y suele ser exitoso cuando las contraseñas están formadas por palabras comunes. Un diccionario puede contener una lista de contraseñas comúnmente utilizadas, lo cuál es un poco más efectivo. Para que un ataque de esta naturaleza pueda ser efectuado, el sistema que realiza la autenticación de las credenciales no debe tener restricciones en cuanto a la cantidad de intentos fallidos; de esta manera el programa que ataca podría probar infinidad de posibilidades sin que el host remoto lo bloquee. Esto mismo es aplicable para un ataque por fuerza bruta, que casi siempre se realiza en combinación con un ataque de diccionario.

## Sistema Operativo
- Windows 10

## Versión
- Python 3.9.1

## Ejecución
Debes ejecutar primero el script del servidor que se encuentra en la carpeta src.

```python	

> python src\easy_server.py

```

Despues el script del cliente que en este caso es el diccionario y se encuentra en la carpeta src.

```python	

> python src\diccionario.py

```
