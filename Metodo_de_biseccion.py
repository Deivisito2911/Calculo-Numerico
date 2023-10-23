from os import system
from math import log, e 

def validar_float(valor):
    while True:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            system("cls")
            print("El valor ingresado no es válido.")
            valor = input("Por favor, ingrese un valor válido: ")

def validar_int(valor):
    while True:
        if valor.isnumeric():
            return int(valor)
        else:
            system("cls")
            print("El valor ingresado no es válido.")
            valor = input("Por favor, ingrese un valor válido: ")

def Metodo_De_Biseccion(funcion, a, b, error, Max_Iteraciones):
    try:
        func = eval("lambda x: " + funcion)
    except:
        print("La función ingresada no es válida.")
        return None
    if func(a) * func(b) >= 0:
        print("La función no cumple con los requisitos del método de bisección.")
        return None

    iteration = 0
    while abs((b - a) / 2) > error and iteration < Max_Iteraciones:
        c = (a + b) / 2.0

        if func(c) == 0:
            return c

        if func(a) * func(c) < 0:
            b = c
        else:
            a = c

        iteration += 1

    return (a + b) / 2.0

print("Programa para el metodo de bisección. Calculo numerico. Realizado por Deivith Zanella")
system("pause")
system("cls")
# Se ingresan los parametros que se necesitaran para evaluar la funcion
funcion = input("Ingrese la función que desea evaluar: ")
a = validar_float(input("Ingrese el valor de la variable a : "))
b = validar_float(input("Ingrese el valor de la variable b : "))
error = validar_float(input("Ingrese el Error que se buscara :  "))
Max_Iteraciones = validar_int(input("Ingrese el maximo de iteraciones : "))
Solucion = Metodo_De_Biseccion(funcion, a, b, error, Max_Iteraciones)

if Solucion is not None:
    print("La solución aproximada es:", Solucion)
else:
    print("No se pudo encontrar una solución en las iteraciones especificadas.")
