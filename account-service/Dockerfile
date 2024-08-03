# Utilizar una imagen base de Python Alpine
FROM python:3.11-alpine

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar las dependencias del sistema necesarias
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev

# Copiar los archivos de requisitos
COPY requirements.txt .

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para correr la aplicación
CMD ["python", "main.py"]