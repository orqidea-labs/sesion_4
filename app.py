import datetime
import os

def log(mensaje):
    with open("bitacora.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - {mensaje}\n")

def celsius_a_fahrenheit(c):
    resultado = (c * 9/5) + 32
    log(f"Convertido {c}°C → {resultado}°F")
    return resultado

def fahrenheit_a_celsius(f):
    resultado = (f - 32) * 5/9
    log(f"Convertido {f}°F → {resultado}°C")
    return resultado

if __name__ == "__main__":
    print("Conversor de temperaturas")
    opcion = input("Seleccione (1) celsius→fahrenheit o (2) F→C: ")
    if opcion == "1":
        c = float(input("Ingrese grados Celsius: "))
        print(f"{c}°celsius = {celsius_a_fahrenheit(c)}°F")
    elif opcion == "2":
        f = float(input("Ingrese grados Fahrenheit: "))
        print(f"{f}°fahrenheit = {fahrenheit_a_celsius(f)}°celsius")
    else:
        print("Opción no válida")
