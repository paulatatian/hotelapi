# 🏨 HotelApp - Sistema de Gestión Hotelera

![AWS EC2](https://img.shields.io/badge/deploy-AWS%20EC2-orange?logo=amazon-aws) 
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue.svg)](https://www.postgresql.org/)

Aplicación web para gestionar habitaciones, huéspedes y reservas de hotel de forma rápida y sencilla.

---

## 📋 Contenidos

- [Funcionalidades](#-funcionalidades)
- [Stack Tecnológico](#-stack-tecnológico)
- [Inicio Rápido con Docker](#-inicio-rápido-con-docker)
- [Despliegue en AWS EC2](#-despliegue-en-aws-ec2)
- [CI/CD con GitHub Actions](#-cicd-con-github-actions)
- [API Endpoints](#-api-endpoints)
- [Troubleshooting](#-troubleshooting)

---

## 🎯 Funcionalidades

- **Habitaciones**: Crear, listar, actualizar y eliminar habitaciones con control de disponibilidad
- **Huéspedes**: Registrar y gestionar información de huéspedes con historial
- **Reservas**: Crear y administrar reservas con validación de fechas
- **Interfaz Web**: UI moderna y responsive con Swagger integrado

---

## 🛠️ Stack Tecnológico

**Backend**: FastAPI + SQLAlchemy + PostgreSQL  
**Frontend**: HTML5 + CSS3 + JavaScript + Jinja2  
**Infraestructura**: AWS EC2 + Nginx + Docker  
**CI/CD**: GitHub Actions

---

## 🐳 Inicio Rápido con Docker

### Requisitos
- Docker Desktop instalado y corriendo

### Comandos

```bash
# Clonar repositorio
git clone https://github.com/paulatatian/hotelapi.git
cd hotelapi

# Construir e iniciar contenedores
docker-compose up -d

# Verificar estado
docker ps
```

### Acceder a la aplicación
- 🌐 **App**: http://localhost
- 📚 **Swagger UI**: http://localhost/docs
- 📖 **ReDoc**: http://localhost/redoc

### Comandos útiles

```bash
# Ver logs en tiempo real
docker-compose logs -f

# Detener contenedores
docker-compose down

# Reiniciar después de cambios
docker-compose restart web

# Rebuild completo
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

**Nota**: Si el puerto 80 está ocupado, edita `docker-compose.yml` y cambia `"80:80"` por `"8000:80"`.

---

## ☁️ Despliegue en AWS EC2

### Requisitos Previos

1. **Instancia EC2** Ubuntu 22.04 LTS
2. **Security Group** configurado:
   - Puerto 22 (SSH) - Solo tu IP
   - Puerto 80 (HTTP) - 0.0.0.0/0
3. Acceso SSH (archivo .pem o EC2 Instance Connect)

### Paso 1: Conectar a EC2

```bash
# Opción A: EC2 Instance Connect (recomendado)
# Desde AWS Console → EC2 → Connect → EC2 Instance Connect

# Opción B: SSH
ssh -i "tu-clave.pem" ubuntu@ec2-xx-xx-xx-xx.compute-1.amazonaws.com
```

### Paso 2: Instalar Dependencias

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv nginx postgresql-client git
```

### Paso 3: Configurar Aplicación

```bash
# Clonar repositorio
cd /home/ubuntu
git clone https://github.com/paulatatian/hotelapi.git
cd hotelapi

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt
```

### Paso 4: Configurar PostgreSQL

```bash
# Instalar PostgreSQL
sudo apt install postgresql postgresql-contrib -y

# Crear base de datos
sudo -u postgres psql
```

```sql
CREATE DATABASE hotel_db;
CREATE USER hotel_user WITH PASSWORD 'password_seguro';
GRANT ALL PRIVILEGES ON DATABASE hotel_db TO hotel_user;
\q
```

```bash
# Editar configuración
nano database.py
# Cambiar: DATABASE_URL = "postgresql://hotel_user:password_seguro@localhost:5432/hotel_db"

# Crear tablas
python3 -c "from database import Base, engine; import models; Base.metadata.create_all(bind=engine)"
```

### Paso 5: Configurar Servicio Uvicorn

```bash
sudo nano /etc/systemd/system/uvicorn.service
```

```ini
[Unit]
Description=Uvicorn server for FastAPI HotelApp
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/hotelapi
Environment="PATH=/home/ubuntu/hotelapi/venv/bin"
ExecStart=/home/ubuntu/hotelapi/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable uvicorn
sudo systemctl start uvicorn
sudo systemctl status uvicorn
```

### Paso 6: Configurar Nginx

```bash
sudo nano /etc/nginx/sites-available/hotelapi
```

```nginx
server {
    listen 80;
    server_name _;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static/ {
        alias /home/ubuntu/hotelapi/static/;
        expires 30d;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/hotelapi /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
```

### Paso 7: Verificar Despliegue

```bash
# Obtener IP pública
curl http://checkip.amazonaws.com

# Acceder desde navegador
# http://TU_IP_PUBLICA
```

### Actualizar Aplicación

```bash
cd /home/ubuntu/hotelapi
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart uvicorn
```

---

## 🤖 CI/CD con GitHub Actions

### ¿Qué se automatiza?

- ✅ Validación de código Python (linting)
- ✅ Tests automáticos
- ✅ Verificación de dependencias

### ¿Cuándo se ejecuta?

- Cada `push` a `main`
- Cada Pull Request
- Manualmente desde GitHub

### Configuración

Crea `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Lint with flake8
      run: |
        pip install flake8
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

---

## 📚 API Endpoints

### Habitaciones
- `POST /api/habitaciones/` - Crear habitación
- `GET /api/habitaciones/` - Listar todas

### Huéspedes
- `POST /api/huespedes/` - Crear huésped
- `GET /api/huespedes/` - Listar todos
- `GET /api/huespedes/{id}` - Obtener por ID
- `PUT /api/huespedes/{id}` - Actualizar
- `DELETE /api/huespedes/{id}` - Eliminar

### Reservas
- `POST /api/reservas/` - Crear reserva
- `GET /api/reservas/` - Listar todas
- `GET /api/reservas/{id}` - Obtener por ID
- `PUT /api/reservas/{id}` - Actualizar
- `DELETE /api/reservas/{id}` - Eliminar

### Ejemplo de uso

```bash
# Crear habitación
curl -X POST "http://TU_IP/api/habitaciones/" \
  -H "Content-Type: application/json" \
  -d '{"numero": "101", "tipo": "Suite", "precio": 150000}'

# Listar huéspedes
curl http://TU_IP/api/huespedes/
```

---

## 🐛 Troubleshooting

### Docker

```bash
# Puerto 80 ocupado
# Editar docker-compose.yml: cambiar "80:80" por "8000:80"

# Ver logs
docker-compose logs -f web

# Reiniciar desde cero
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

### AWS EC2

```bash
# Ver logs de Uvicorn
sudo journalctl -u uvicorn -f

# Ver logs de Nginx
sudo tail -f /var/log/nginx/error.log

# Verificar estado de servicios
sudo systemctl status uvicorn
sudo systemctl status nginx
sudo systemctl status postgresql

# Reiniciar servicios
sudo systemctl restart uvicorn
sudo systemctl restart nginx
```

### Base de Datos

```bash
# Verificar conexión PostgreSQL
psql -h localhost -U hotel_user -d hotel_db

# Ver logs de PostgreSQL
sudo tail -f /var/log/postgresql/postgresql-14-main.log
```

---

## 📊 Estructura del Proyecto

```
hotelapi/
├── routers/              # Endpoints API
├── static/               # CSS y JavaScript
├── templates/            # HTML templates
├── database.py           # Configuración DB
├── models.py             # Modelos SQLAlchemy
├── schemas.py            # Validación Pydantic
├── main.py               # App principal
├── docker-compose.yml    # Configuración Docker
└── requirements.txt      # Dependencias
```

---

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/NuevaCaracteristica`)
3. Commit (`git commit -m 'Agregar nueva característica'`)
4. Push (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

---

## 📄 Licencia

MIT License - Ver `LICENSE` para más detalles

---

## 👥 Autor

**Paula Tatian** - [GitHub](https://github.com/paulatatian)