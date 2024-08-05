# Utilizar la imagen base de Python 3.8 con Alpine
FROM python:3.11-alpine

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar el archivo requirements.txt en el directorio de trabajo
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el contenido del directorio actual en el directorio de trabajo
COPY . .

# Exponer el puerto 8000 para la aplicación Sanic
EXPOSE 8000

# Ejecutar la aplicación utilizando el comando "sanic"
CMD ["python", "main.py"]