# Usa la imagen oficial de Python como base
FROM python:3.12

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

# Set an environment variable to enable unbuffered stdout and stderr
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file from the build context to the container's working directory
COPY requirements.txt .

# Create a virtual environment named venv using the python interpreter
RUN python -m venv venv

RUN /bin/bash -c "source venv/bin/activate"

RUN pip install -r requirements.txt

COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
