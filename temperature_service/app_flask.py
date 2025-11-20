import datetime
import mimetypes
from datetime import timezone

from flask import Flask, jsonify, request # type: ignore

mimetypes.add_type("text/javascript", ".js")

app = Flask(__name__, static_folder="frontend", static_url_path="")

def log(mensaje):
    # Hora actual en UTC menos 5 horas (Bogotá / Lima)
    hora_local = datetime.datetime.now(timezone.utc) - datetime.timedelta(hours=5)
    ruta_log = "/tmp/bitacora.log"

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

@app.route("/convert/c2f", methods=["GET"])
def convert_c2f():
    c = float(request.args.get("c"))
    return jsonify({"celsius": c, "fahrenheit": celsius_a_fahrenheit(c)})

@app.route("/convert/f2c", methods=["GET"])
def convert_f2c():
    f = float(request.args.get("f"))
    return jsonify({"fahrenheit": f, "celsius": fahrenheit_a_celsius(f)})

@app.route("/")
def home():
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
