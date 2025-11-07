


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: dividir entre 0 no es posible"
    return a / b


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def potencia(a, b):
    return a ** b


def guardar_resultado(operacion, a, b, resultado):
    """
    Guarda la operación realizada en un archivo de texto.
    """
    with open("historial.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{a} {operacion} {b} = {resultado}\n")

def ver_historial():
    with open("historial.txt", "r", encoding="utf-8") as archivo:
        print(archivo.read())



#archivo operaciones.py el anterior fue main.py
