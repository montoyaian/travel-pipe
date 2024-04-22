# Usamos la imagen oficial de Python
FROM python:3.9

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos el archivo de requisitos e instalamos las dependencias
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código de la aplicación a la imagen
COPY app/ app/

# Definimos el comando para ejecutar la aplicación FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
