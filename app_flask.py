from flask import Flask, request, jsonify
import datetime
import os

app = Flask(__name__)

def log(mensaje):
    ruta_log = "/tmp/bitacora.log"
    with open(ruta_log, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} - {mensaje}\n")

def celsius_a_fahrenheit(c):
    resultado = (c * 9/5) + 32
    log(f"Convertido {c}°C → {resultado}°F")
    return resultado

def fahrenheit_a_celsius(f):
    resultado = (f - 32) * 5/9
    log(f"Convertido {f}°F → {resultado}°C")
    return resultado

@app.route("/convert/c2f", methods=["GET"])
def convert_c2f():
    c = float(request.args.get("c"))
    return jsonify({"celsius": c, "fahrenheit": celsius_a_fahrenheit(c)})

@app.route("/convert/f2c", methods=["GET"])
def convert_f2c():
    f = float(request.args.get("f"))
    return jsonify({"fahrenheit": f, "celsius": fahrenheit_a_celsius(f)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)


# app_flask.py - versión con Flask para conversión de temperaturas
# y registro en bitácora dentro de un contenedor Docker