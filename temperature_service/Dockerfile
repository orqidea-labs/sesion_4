FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app_flask.py .

# ⬇️ Agregar esta línea para copiar tu carpeta frontend
COPY frontend ./frontend

EXPOSE 5001

CMD ["python", "app_flask.py"]
