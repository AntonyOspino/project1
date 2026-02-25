import json

# =============================================================
# Ejercicio 1: Crear variable nombre
# =============================================================
nombre = "Antony"
print(f"Ejercicio 1 - Nombre: {nombre}")


# =============================================================
# Ejercicio 2: Sumar dos números
# =============================================================
a, b = 15, 27
suma = a + b
print(f"Ejercicio 2 - Suma de {a} + {b} = {suma}")


# =============================================================
# Ejercicio 3: Validar número par
# =============================================================
numero = 42
es_par = "par" if numero % 2 == 0 else "impar"
print(f"Ejercicio 3 - El número {numero} es {es_par}")


# =============================================================
# Ejercicio 4: Recorrer lista
# =============================================================
frutas = ["manzana", "banana", "cereza", "mango"]
print("Ejercicio 4 - Lista de frutas:")
for fruta in frutas:
    print(f"  - {fruta}")


# =============================================================
# Ejercicio 5: Función multiplicar
# =============================================================
def multiplicar(x, y):
    return x * y

print(f"Ejercicio 5 - Multiplicar(6, 7) = {multiplicar(6, 7)}")


# =============================================================
# Ejercicio 6: Diccionario persona
# =============================================================
persona = {
    "nombre": "Laura",
    "edad": 25,
    "ciudad": "Bogotá",
    "profesion": "Ingeniera"
}
print(f"Ejercicio 6 - Persona: {persona}")


# =============================================================
# Ejercicio 7: Mostrar claves del diccionario
# =============================================================
print("Ejercicio 7 - Claves del diccionario persona:")
for clave in persona.keys():
    print(f"  {clave}: {persona[clave]}")


# =============================================================
# Ejercicio 8: Clase Producto
# =============================================================
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def descripcion(self):
        return f"{self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock} unidades"

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * (porcentaje / 100)

producto = Producto("Laptop", 1200.00, 10)
producto.aplicar_descuento(10)
print(f"Ejercicio 8 - Producto: {producto.descripcion()}")


# =============================================================
# Ejercicio 9: Try / Except
# =============================================================
print("Ejercicio 9 - División con manejo de errores:")
try:
    dividendo, divisor = 100, 0
    print(f"  {dividendo} / {divisor} = {dividendo / divisor}")
except ZeroDivisionError:
    print("  Error: No se puede dividir entre cero.")
finally:
    print("  Bloque finally ejecutado.")


# =============================================================
# Ejercicio 10: Lista del 1 al 10
# =============================================================
lista_1_10 = list(range(1, 11))
print(f"Ejercicio 10 - Lista del 1 al 10: {lista_1_10}")


# =============================================================
# Ejercicio 11: Duplicar lista
# =============================================================
lista_duplicada = [n * 2 for n in lista_1_10]
print(f"Ejercicio 11 - Lista duplicada: {lista_duplicada}")


# =============================================================
# Ejercicio 12: Mayor de dos números
# =============================================================
def mayor_de_dos(x, y):
    return x if x >= y else y

print(f"Ejercicio 12 - Mayor entre 45 y 72: {mayor_de_dos(45, 72)}")


# =============================================================
# Ejercicio 13: Leer archivo
# =============================================================
print("Ejercicio 13 - Leer archivo:")
try:
    with open("README.md", "r", encoding="utf-8") as archivo:
        lineas = [archivo.readline().strip() for _ in range(3)]
    for linea in lineas:
        print(f"  {linea}")
except FileNotFoundError:
    print("  Archivo no encontrado.")


# =============================================================
# Ejercicio 14: Diccionario a JSON
# =============================================================
datos = {
    "proyecto": "basic_python_br",
    "version": "1.0",
    "lenguaje": "Python",
    "ejercicios": 14
}
print(f"Ejercicio 14 - Dict a JSON:\n{json.dumps(datos, indent=4, ensure_ascii=False)}")


