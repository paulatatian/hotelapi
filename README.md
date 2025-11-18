# 🏨 HotelApp - Gestión de Hotel con FastAPI

![AWS EC2](https://img.shields.io/badge/deploy-AWS%20EC2-orange?logo=amazon-aws) 
![JavaScript CI](https://github.com/paulatatian/calculadora-cdt/workflows/JavaScript%20CI/badge.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue.svg)](https://www.postgresql.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


Esta aplicación web permite administrar un hotel de manera rápida y sencilla.
---

## 📋 Tabla de Contenidos

- [Funcionalidades](#-funcionalidades-principales)
- [Tecnologías](#-tecnologías-utilizadas)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación Local](#-instalación-local)
- [Despliegue en AWS](#-despliegue-en-aws)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [API Endpoints](#-api-endpoints)
- [Troubleshooting](#-troubleshooting)
- [Contribuir](#-contribuir)

---

## 🏨 Funcionalidades principales

### 📋 Gestión de Habitaciones
* Crear, listar, actualizar y eliminar habitaciones del hotel
* Control de disponibilidad y tipo de habitación
* Asignación de precios por tipo

### 🧑‍🤝‍🧑 Gestión de Huéspedes
* Registrar huéspedes con sus datos personales
* Listar, actualizar o eliminar registros de huéspedes
* Historial de reservas por huésped

### 📅 Gestión de Reservas
* Crear reservas asignando habitaciones a huéspedes
* Consultar reservas activas, modificar o cancelar reservas
* Control de fechas de ingreso y salida

### 🌐 Interfaz Web
* Páginas HTML con CSS moderno y animaciones
* Navegación intuitiva entre "Habitaciones", "Huéspedes" y "Reservas"
* Interfaz responsive para dispositivos móviles
* Swagger UI para probar la API en tiempo real

---

## 🛠️ Tecnologías Utilizadas

### Backend
- **FastAPI** - Framework web moderno de alto rendimiento
- **SQLAlchemy** - ORM para Python
- **PostgreSQL** - Base de datos relacional
- **Pydantic** - Validación de datos
- **Uvicorn** - Servidor ASGI

### Frontend
- **HTML5** - Estructura semántica
- **CSS3** - Estilos con gradientes y animaciones
- **JavaScript ES6+** - Fetch API para comunicación con backend
- **Jinja2** - Motor de templates

### Infraestructura
- **AWS EC2** - Servidor de aplicación
- **Nginx** - Proxy reverso y servidor web
- **systemd** - Gestión de servicios

---

## 📋 Requisitos Previos

### Para AWS
* **Cuenta AWS** activa
* **Instancia EC2** creada y corriendo (Ubuntu 22.04 LTS recomendado)
* **Security Group** configurado con puertos:
   * `22` (SSH)
   * `80` (HTTP)
   * `8000` (desarrollo/opcional)
* Acceso SSH a la instancia (par de claves .pem)

### Para desarrollo local
* Python 3.8 o superior
* PostgreSQL 12 o superior
* Git

---

## 💻 Instalación Local

### 1. Clonar el repositorio

```bash
git clone https://github.com/paulatatian/hotelapi.git
cd hotelapi
```

### 2. Crear entorno virtual

```bash
python3 -m venv venv

# Linux/Mac
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos local

```bash
# Crear base de datos PostgreSQL
sudo -u postgres psql
CREATE DATABASE hotel_db;
CREATE USER hotel_user WITH PASSWORD 'tu_password';
GRANT ALL PRIVILEGES ON DATABASE hotel_db TO hotel_user;
\q
```

Edita `database.py`:

```python
DATABASE_URL = "postgresql://hotel_user:tu_password@localhost:5432/hotel_db"
```

### 5. Crear tablas

```bash
python3 -c "from database import Base, engine; import models; Base.metadata.create_all(bind=engine)"
```

### 6. Ejecutar servidor de desarrollo

```bash
uvicorn main:app --reload
```

Accede a: `http://localhost:8000`

---

## 🚀 Despliegue en AWS

### 🔧 Paso 1: Conectarse a la Instancia EC2

#### Opción A: EC2 Instance Connect (Recomendado)
1. Ve a **AWS Console** → **EC2** → **Instances**
2. Selecciona tu instancia
3. Clic en **"Connect"** → **"EC2 Instance Connect"** → **"Connect"**

#### Opción B: SSH con archivo .pem
```bash
ssh -i "tu-clave.pem" ubuntu@ec2-xx-xx-xx-xx.compute-1.amazonaws.com
```

---

### 🔧 Paso 2: Preparar el Entorno

```bash
# Actualizar sistema
sudo apt update
sudo apt upgrade -y

# Instalar dependencias
sudo apt install -y python3-pip python3-venv nginx postgresql-client git

# Verificar instalación
python3 --version
nginx -v
```

---

### 📥 Paso 3: Clonar el Repositorio

```bash
cd /home/ubuntu
git clone https://github.com/paulatatian/hotelapi.git
cd hotelapi
```

---

### 🐍 Paso 4: Configurar Entorno Virtual

```bash
python3 -m venv venv
source venv/bin/activate

# Verificar que estás en el entorno virtual
which python  # Debe mostrar: /home/ubuntu/hotelapi/venv/bin/python
```

---

### 📦 Paso 5: Instalar Dependencias

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Si `requirements.txt` está vacío, instala manualmente:

```bash
pip install fastapi uvicorn[standard] sqlalchemy psycopg2-binary pydantic jinja2 python-multipart
```

---

### 🗄️ Paso 6: Configurar Base de Datos

#### Opción A: PostgreSQL Local en EC2

```bash
# Instalar PostgreSQL
sudo apt install postgresql postgresql-contrib -y

# Crear base de datos
sudo -u postgres psql

# Dentro de psql:
CREATE DATABASE hotel_db;
CREATE USER hotel_user WITH PASSWORD 'password_seguro';
GRANT ALL PRIVILEGES ON DATABASE hotel_db TO hotel_user;
\q
```

Edita `database.py`:

```bash
nano database.py
```

Cambia la línea:

```python
DATABASE_URL = "postgresql://hotel_user:password_seguro@localhost:5432/hotel_db"
```

#### Opción B: AWS RDS (Recomendado para producción)

1. Crea una instancia RDS PostgreSQL en AWS Console
2. Anota el endpoint: `hotel-db.xxxxx.us-east-1.rds.amazonaws.com`
3. Configura Security Group para permitir conexión desde EC2
4. Edita `database.py`:

```python
DATABASE_URL = "postgresql://usuario:password@hotel-db.xxxxx.us-east-1.rds.amazonaws.com:5432/hotel_db"
```

#### Crear Tablas

```bash
python3 -c "from database import Base, engine; import models; Base.metadata.create_all(bind=engine)"
```

---

### ⚙️ Paso 7: Configurar Uvicorn con systemd

Crear archivo de servicio:

```bash
sudo nano /etc/systemd/system/uvicorn.service
```

Contenido del archivo:

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

# Reinicio automático en caso de fallo
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Activar el servicio:

```bash
# Recargar systemd
sudo systemctl daemon-reload

# Habilitar inicio automático
sudo systemctl enable uvicorn

# Iniciar servicio
sudo systemctl start uvicorn

# Verificar estado
sudo systemctl status uvicorn
```

**Comandos útiles para gestionar el servicio:**

```bash
sudo systemctl stop uvicorn      # Detener
sudo systemctl restart uvicorn   # Reiniciar
sudo systemctl status uvicorn    # Ver estado
sudo journalctl -u uvicorn -f    # Ver logs en tiempo real
```

---

### ⚙️ Paso 8: Configurar Nginx

Crear archivo de configuración:

```bash
sudo nano /etc/nginx/sites-available/hotelapi
```

Contenido del archivo:

```nginx
server {
    listen 80;
    server_name _;  # Reemplaza con tu dominio si tienes uno

    # Logs
    access_log /var/log/nginx/hotelapi_access.log;
    error_log /var/log/nginx/hotelapi_error.log;

    # Proxy para la aplicación FastAPI
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $http_x_forwarded_proto;
    }

    # Servir archivos estáticos directamente
    location /static/ {
        alias /home/ubuntu/hotelapi/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    # Tamaño máximo de archivos (si implementas uploads)
    client_max_body_size 10M;
}
```

Activar configuración:

```bash
# Crear enlace simbólico
sudo ln -s /etc/nginx/sites-available/hotelapi /etc/nginx/sites-enabled/

# Eliminar configuración por defecto (opcional)
sudo rm /etc/nginx/sites-enabled/default

# Verificar sintaxis
sudo nginx -t

# Reiniciar Nginx
sudo systemctl restart nginx

# Verificar estado
sudo systemctl status nginx
```

---

### 🌐 Paso 9: Acceder a la Aplicación

#### Obtener IP Pública de EC2

```bash
curl http://checkip.amazonaws.com
```

O desde AWS Console → EC2 → Instances → Copiar "Public IPv4 address"

#### Acceder desde navegador:

* **Aplicación**: `http://TU_IP_PUBLICA/`
* **Swagger UI**: `http://TU_IP_PUBLICA/docs`
* **ReDoc**: `http://TU_IP_PUBLICA/redoc`

---

## 🛡️ Security Group - Configuración Requerida

Asegúrate de que tu Security Group tenga estas reglas de **Inbound**:

| Tipo | Puerto | Origen | Descripción |
|------|--------|--------|-------------|
| SSH | 22 | Tu IP | Acceso SSH seguro |
| HTTP | 80 | 0.0.0.0/0 | Servidor web público |
| Custom TCP | 8000 | 0.0.0.0/0 | Desarrollo (opcional) |

**Nota de seguridad**: Para SSH, restringe el acceso solo a tu IP en lugar de 0.0.0.0/0

---

## 📝 Configuración Adicional

### Variables de Entorno (Recomendado)

Crea un archivo `.env`:

```bash
nano .env
```

Contenido:

```env
DATABASE_URL=postgresql://usuario:password@host:5432/hotel_db
SECRET_KEY=clave-super-secreta-cambiar-en-produccion
DEBUG=False
ENVIRONMENT=production
```

Instala python-dotenv:

```bash
pip install python-dotenv
```

Modifica `database.py`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
```

---

## 🔄 Actualizar la Aplicación

Cuando hagas cambios en el código:

```bash
cd /home/ubuntu/hotelapi

# Obtener últimos cambios
git pull origin main

# Activar entorno virtual
source venv/bin/activate

# Actualizar dependencias si hay cambios
pip install -r requirements.txt

# Reiniciar servicio
sudo systemctl restart uvicorn

# Verificar estado
sudo systemctl status uvicorn
```

---

## 📚 API Endpoints

### Habitaciones

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/habitaciones/` | Crear habitación |
| GET | `/api/habitaciones/` | Listar todas |

### Huéspedes

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/huespedes/` | Crear huésped |
| GET | `/api/huespedes/` | Listar todos |
| GET | `/api/huespedes/{id}` | Obtener por ID |
| PUT | `/api/huespedes/{id}` | Actualizar |
| DELETE | `/api/huespedes/{id}` | Eliminar |

### Reservas

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/reservas/` | Crear reserva |
| GET | `/api/reservas/` | Listar todas |
| GET | `/api/reservas/{id}` | Obtener por ID |
| PUT | `/api/reservas/{id}` | Actualizar |
| DELETE | `/api/reservas/{id}` | Eliminar |

### Ejemplos de Uso

**Crear habitación:**

```bash
curl -X POST "http://TU_IP/api/habitaciones/" \
  -H "Content-Type: application/json" \
  -d '{
    "numero": "101",
    "tipo": "Suite",
    "precio": 150000
  }'
```

**Listar huéspedes:**

```bash
curl http://TU_IP/api/huespedes/
```

---

## 🐛 Troubleshooting

### La aplicación no inicia

```bash
# Ver logs de Uvicorn
sudo journalctl -u uvicorn -n 50

# Ver logs de Nginx
sudo tail -f /var/log/nginx/error.log
```

### Error de conexión a PostgreSQL

```bash
# Verificar que PostgreSQL está corriendo
sudo systemctl status postgresql

# Probar conexión manual
psql -h localhost -U hotel_user -d hotel_db
```

### Nginx no sirve archivos estáticos

```bash
# Verificar permisos
ls -la /home/ubuntu/hotelapi/static/

# Dar permisos si es necesario
sudo chmod -R 755 /home/ubuntu/hotelapi/static/
```

### Puerto 80 ocupado

```bash
# Ver qué proceso usa el puerto 80
sudo lsof -i :80

# Detener proceso si es necesario
sudo systemctl stop apache2  # Si tienes Apache instalado
```

### Cambios no se reflejan

```bash
# Limpiar caché del navegador o prueba en modo incógnito
# Reiniciar servicios
sudo systemctl restart uvicorn
sudo systemctl restart nginx
```

---

## 🤖 Automatización con GitHub Actions

### ✅ ¿Qué se automatiza?

* Validación de código Python (linting)
* Tests automáticos
* Verificación de dependencias
* Comprobación de sintaxis

### 🔄 ¿Cuándo se ejecuta?

* Cada `push` a la rama `main`
* Cada Pull Request
* Manualmente desde GitHub Actions

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

## 📊 Estructura del Proyecto

```
hotelapi/
├── routers/
│   ├── habitaciones.py       # Endpoints de habitaciones
│   ├── huespedes.py          # Endpoints de huéspedes
│   ├── reservas.py           # Endpoints de reservas
│   └── usuarios.py           # Sistema de autenticación
├── static/
│   ├── css/
│   │   └── styles.css        # Estilos globales
│   └── js/
│       └── scripts.js        # Lógica del cliente
├── templates/
│   ├── index.html            # Página principal
│   ├── habitaciones.html     # Gestión de habitaciones
│   ├── huespedes.html        # Gestión de huéspedes
│   └── reservas.html         # Gestión de reservas
├── database.py               # Configuración de DB
├── models.py                 # Modelos SQLAlchemy
├── schemas.py                # Schemas Pydantic
├── main.py                   # Aplicación principal
├── requirements.txt          # Dependencias Python
└── README.md                 # Este archivo
```

---

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 👥 Autores

* **Paula Tatian** - [GitHub](https://github.com/paulatatian)



