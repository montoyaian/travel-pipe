# Usa la imagen oficial de Python como base
FROM python:3.11


# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file from the build context to the container's working directory
COPY requirements.txt .


RUN pip install -r requirements.txt

COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
