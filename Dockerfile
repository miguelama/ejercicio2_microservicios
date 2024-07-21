FROM ubuntu:latest
LABEL authors="MIGUEL_MUNOZ"

ENTRYPOINT ["top", "-b"]
# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de requisitos
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el contenido del proyecto en el directorio de trabajo
COPY . .

# Expone el puerto en el que correrá la aplicación
EXPOSE 5000

# Comando para correr la aplicación con Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
