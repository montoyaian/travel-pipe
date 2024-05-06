# Utiliza una versión estable de Python como base
FROM python:3.10

# Establece variables de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instala las dependencias directamente en el entorno base
RUN pip install -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . .

# Expone el puerto 8000 (ajústalo según tus necesidades)
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
