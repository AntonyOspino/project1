import json
from fastapi import FastAPI

app = FastAPI(title="API de Programación Agéntica - EPII Diurno", description="Elaborado por Antony Ospino", version="1.0.0.", contact={
                "name": "Antony Ospino",
                "email": "amospinop@ul.edu.co",
        })

@app.get("/")
def ruta_principal():
    return {"mensaje": "Bienvenido a la API del Proyecto 1. Visita /docs para ver todos los ejercicios."}

@app.get("/ejercicio1")
def ejercicio_1():
    nombre = "Antony"
    return {"ejercicio": 1, "descripcion": "Crear variable nombre", "nombre": nombre}

@app.get("/ejercicio2")
def ejercicio_2():
    a, b = 15, 27
    return {"ejercicio": 2, "descripcion": f"Suma de {a} + {b}", "resultado": a + b}

@app.get("/ejercicio3")
def ejercicio_3():
    numero = 42
    es_par = "par" if numero % 2 == 0 else "impar"
    return {"ejercicio": 3, "numero": numero, "estado": es_par}

@app.get("/ejercicio4")
def ejercicio_4():
    frutas = ["manzana", "banana", "cereza", "mango"]
    return {"ejercicio": 4, "frutas": frutas}

@app.get("/ejercicio5")
def ejercicio_5():
    def multiplicar(x, y):
        return x * y
    return {"ejercicio": 5, "operacion": "6 * 7", "resultado": multiplicar(6, 7)}

@app.get("/ejercicio6")
def ejercicio_6():
    persona = {
        "nombre": "Laura",
        "edad": 25,
        "ciudad": "Bogotá",
        "profesion": "Ingeniera"
    }
    return {"ejercicio": 6, "persona": persona}

@app.get("/ejercicio7")
def ejercicio_7():
    persona = {"nombre": "Laura", "edad": 25, "ciudad": "Bogotá", "profesion": "Ingeniera"}
    # Devolvemos solo las claves como una lista
    return {"ejercicio": 7, "claves": list(persona.keys())}

@app.get("/ejercicio8")
def ejercicio_8():
    class Producto:
        def __init__(self, nombre, precio, stock):
            self.nombre = nombre
            self.precio = precio
            self.stock = stock

        def aplicar_descuento(self, porcentaje):
            self.precio -= self.precio * (porcentaje / 100)

    producto = Producto("Laptop", 1200.00, 10)
    producto.aplicar_descuento(10)
    return {
        "ejercicio": 8,
        "producto": producto.nombre,
        "precio_con_descuento": producto.precio,
        "stock": producto.stock
    }

@app.get("/ejercicio9")
def ejercicio_9():
    dividendo, divisor = 100, 0
    try:
        resultado = dividendo / divisor
        return {"ejercicio": 9, "resultado": resultado}
    except ZeroDivisionError:
        return {"ejercicio": 9, "error": "No se puede dividir entre cero."}

@app.get("/ejercicio10")
def ejercicio_10():
    lista_1_10 = list(range(1, 11))
    return {"ejercicio": 10, "lista": lista_1_10}

@app.get("/ejercicio11")
def ejercicio_11():
    lista_1_10 = list(range(1, 11))
    lista_duplicada = [n * 2 for n in lista_1_10]
    return {"ejercicio": 11, "lista_duplicada": lista_duplicada}

@app.get("/ejercicio12")
def ejercicio_12():
    def mayor_de_dos(x, y):
        return x if x >= y else y
    return {"ejercicio": 12, "mayor": mayor_de_dos(45, 72)}

@app.get("/ejercicio13")
def ejercicio_13():
    try:
        with open("README.md", "r", encoding="utf-8") as archivo:
            # Leemos las primeras 3 líneas del README para no saturar la respuesta
            lineas = [archivo.readline().strip() for _ in range(3)]
        return {"ejercicio": 13, "contenido_readme": lineas}
    except FileNotFoundError:
        return {"ejercicio": 13, "error": "Archivo no encontrado."}

@app.get("/ejercicio14")
def ejercicio_14():
    datos = {
        "proyecto": "basic_python_br",
        "version": "1.0",
        "lenguaje": "Python",
        "ejercicios": 14
    }
    # FastAPI convierte los diccionarios a JSON automáticamente
    return {"ejercicio": 14, "datos": datos}
