# Proyecto: Una Mejor Calculadora

## Descripción
Este proyecto es una calculadora en Python que realiza operaciones básicas con listas de números y verifica propiedades numéricas.  
Las funciones principales del proyecto son: sumar números, multiplicar números, determinar si un número es par y verificar si un número es entero.

---

## Funciones del proyecto

1. **`addmultiplenumbers(lista)`**  
   - Suma todos los números de la lista y devuelve el resultado.  
   - Funciona con números positivos, negativos y decimales.

2. **`multiplymultiplenumbers(lista)`**  
   - Multiplica todos los números de la lista y devuelve el resultado.  
   - Funciona con números positivos, negativos y decimales.

3. **`isiteven(numero)`**  
   - Devuelve `True` si el número es entero y par, `False` en caso contrario.  
   - Funciona con enteros positivos y negativos, y detecta decimales correctamente.

4. **`isitaninteger(numero)`**  
   - Devuelve `True` si el número es un entero (por ejemplo 7 o 7.0), `False` si no.  

---

## Estructura del proyecto

- **`main.py`**  
  Contiene todas las funciones y la función principal `main()`, que imprime mensajes claros y permite probar la calculadora.  

- **`test_main.py`**  
  Contiene pruebas automáticas usando `pytest` para verificar que todas las funciones se comporten correctamente.  

---

## Pasos que seguimos para crear el proyecto

1. **Crear `main.py`**  
   - Se definió la función principal `main()` y el bloque de ejecución `if __name__=="__main__": main()`.  

2. **Definir las funciones**  
   - `addmultiplenumbers(lista)`  
   - `multiplymultiplenumbers(lista)`  
   - `isiteven(numero)`  
   - `isitaninteger(numero)`  

3. **Probar funciones manualmente**  
   - Se agregó código en `main()` para imprimir resultados de ejemplo y verificar funcionamiento.  

4. **Crear tests automáticos**  
   - Se creó `test_main.py` con 8 pruebas usando `pytest` para garantizar que todas las funciones cumplan con los requisitos.  

5. **Instalar pytest y correr pruebas**  
   - Se instaló `pytest` con `pip install pytest`.  
   - Se ejecutaron las pruebas en la terminal de VSCode y todas pasaron correctamente.  

6. **Verificación final**  
   - Se comprobó que el proyecto cumple con todos los requisitos: funciones correctas, mensajes claros, código organizado, casos especiales manejados, y README incluido.  

---

## Cómo ejecutar la calculadora

1. Abrir la terminal en la carpeta del proyecto.  
2. Ejecutar:  
   ```bash
   python main.py
