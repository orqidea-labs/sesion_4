import datetime
import os

def log(mensaje):
    # Hora actual en UTC menos 5 horas (Bogotá / Lima)
    hora_local = datetime.datetime.utcnow() - datetime.timedelta(hours=5)
    ruta_log = "/tmp/bitacora.log"  # o el path que prefieras
    with open(ruta_log, "a", encoding="utf-8") as f:
        f.write(f"{hora_local.strftime('%Y-%m-%d %H:%M:%S')} - {mensaje}\n")

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
    print("Ruta actual:", os.getcwd())  # solo para verificar

    opcion = input("Seleccione (1) Celsius → Fahrenheit o (2) Fahrenheit → °Celsius: ")
    if opcion == "1":
        c = float(input("Ingrese grados Celsius: "))
        print(f"{c} °Celsius = {celsius_a_fahrenheit(c)} °Fahrenheit")
    elif opcion == "2":
        f = float(input("Ingrese grados Fahrenheit: "))
        print(f"{f} °Fahrenheit = {fahrenheit_a_celsius(f)} °Celsius")
    else:
        print("Opción no válida")
