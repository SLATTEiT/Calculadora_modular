import operaciones
from operaciones import ver_historial


def mostrar_menu():
    print("\n-- Calculadora --")
    print("1) Multiplicar")
    print("2) Dividir")
    print("3) Sumar")
    print("4) Restar")
    print("5) potencia")
    print("6) salir")
    print("7) ver historial")


while True:
    mostrar_menu()
    opciones = input("seleccione una opcion:")
    if opciones == "6":
        print("Hasta pronto :D")
        break
    elif opciones == "7":
        ver_historial()
        break
    try:
        a = float(input("ingrese un numero: "))
        b = float(input("ingrese otro numero: "))


        if opciones == "1":
            resultado = operaciones.multiplicar(a, b)
        elif opciones == "2":
            resultado = operaciones.dividir(a, b)
        elif opciones == "3":
            resultado = operaciones.sumar(a, b)
        elif opciones == "4":
            resultado = operaciones.restar(a, b)
        else:
            print("Opcion no valida")
            continue

        print("Resultado:", resultado)
        # Preguntar si desea guardar el resultado
        guardar = input("¿Deseas guardar este resultado? (s/n): ").lower()
        if guardar == "s":
            operacion = {
                "1": "*",
                "2": "/",
                "3": "+",
                "4": "-",
                "5": "**",
            }.get(opciones, "Operación desconocida")

            operaciones.guardar_resultado(operacion, a, b, resultado)
            print("Resultado guardado exitosamente en historial.txt")


    except ValueError:
        print("Error: ingrese un número válido")





