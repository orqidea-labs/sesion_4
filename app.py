# app.py
def celsius_a_fahrenheit(c):
    """Convierte Celsius a Fahrenheit"""
    return (c * 9/5) + 32

def fahrenheit_a_celsius(f):
    """Convierte Fahrenheit a Celsius"""
    return (f - 32) * 5/9

if __name__ == "__main__":
    print("Conversor de temperaturas")
    c = float(input("Ingrese grados Celsius: "))
    print(f"{c}°C equivalen a {celsius_a_fahrenheit(c)}°F")
