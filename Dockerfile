# Usamos la imagen oficial de Python
FROM python:3.9

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos todo el contenido del directorio de trabajo al contenedor
COPY . .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Definimos el comando para ejecutar la aplicación FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
