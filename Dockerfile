# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establecer variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para PostgreSQL
RUN apt-get update && apt-get install -y \
    postgresql-client \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements.txt primero para aprovechar cache de Docker
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Crear directorios necesarios si no existen
RUN mkdir -p src/static/css src/static/js src/templates

# Exponer el puerto 80
EXPOSE 80

# Comando para ejecutar la aplicación en el puerto 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]