# Usamos una imagen base oficial de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos todos los archivos del proyecto
COPY . /app

# Actualizamos pip y luego instalamos dependencias
RUN pip install --upgrade pip

# Comando por defecto para ejecutar la aplicación
CMD ["python", "server.py"]