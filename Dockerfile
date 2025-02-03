# Usa una imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt requirements.txt
COPY app.py app.py
COPY database.db database.db
COPY index.html index.html

# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto que usará la aplicación
EXPOSE 5000

# Define el comando de arranque
CMD ["python", "app.py"]
