# Usa la imagen oficial de Python como base
FROM python:3.9

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de requerimientos (requirements.txt) al contenedor
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia tu aplicación FastAPI al contenedor
COPY . .

# Expone el puerto 80 (puedes cambiarlo según tus necesidades)
EXPOSE 80

# Define el comando para ejecutar tu aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

