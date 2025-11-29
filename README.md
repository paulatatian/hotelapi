# 🏨 HotelApp - Sistema de Gestión Hotelera

![AWS EC2](https://img.shields.io/badge/deploy-AWS%20EC2-orange?logo=amazon-aws) 
![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue.svg)](https://www.postgresql.org/)

Aplicación web completa para gestionar habitaciones, huéspedes y reservas de hotel de forma rápida y sencilla. Sistema full-stack con backend en FastAPI, base de datos PostgreSQL y frontend interactivo.

---

## 📋 Contenidos

- [Descripción](#-descripción)
- [Arquitectura](#-arquitectura)
- [Componentes](#-componentes)
- [Flujo de Datos](#-flujo-de-datos)
- [Funcionalidades](#-funcionalidades)
- [Stack Tecnológico](#️-stack-tecnológico)
- [URLs de la Aplicación](#-urls-de-la-aplicación)
- [Instalación Local](#-instalación-local)
- [Inicio Rápido con Docker](#-inicio-rápido-con-docker)
- [Despliegue en AWS EC2](#️-despliegue-en-aws-ec2)
- [CI/CD con GitHub Actions](#-cicd-con-github-actions)
- [API Endpoints](#-api-endpoints)
- [Problemas y Soluciones](#-problemas-y-soluciones)
- [Aprendizajes](#-aprendizajes)
- [Troubleshooting](#-troubleshooting)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)
- [Autor](#-autor)
- [Soporte](#-soporte)
- [Roadmap](#-roadmap--futuras-mejoras)

---
HotelApp es un sistema completo de gestión hotelera que permite administrar eficientemente las operaciones diarias de un hotel. La aplicación ofrece una interfaz web intuitiva que proporciona operaciones CRUD completas para la gestión integral de un sistema hotelero como gestionar habitaciones, registrar huéspedes y controlar reservas, con validación de datos en tiempo real y persistencia en base de datos PostgreSQL. El proyecto implementa una arquitectura full-stack moderna con separación de responsabilidades, desplegado en AWS EC2 con automatización CI/CD mediante GitHub Actions.

---

## 🏗️ Arquitectura

```bash
┌─────────────────┐
│   USUARIO       │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────┐
│   FRONTEND (HTML/CSS/JS)    │
│   - Interfaz Usuario        │
│   - Validación Cliente      │
│   - Fetch API               │
└────────┬────────────────────┘
         │ HTTP/HTTPS
         ▼
┌─────────────────────────────┐
│   NGINX (Reverse Proxy)     │
│   - Puerto 80               │
│   - Servir estáticos        │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│   BACKEND API (FastAPI)     │
│   - Puerto 8000             │
│   - Lógica de Negocio       │
│   - Validación Pydantic     │
│   - SQLAlchemy ORM          │
└────────┬────────────────────┘
         │
         ▼
┌─────────────────────────────┐
│   BASE DE DATOS             │
│   (PostgreSQL)              │
│   - Puerto 5432             │
│   - Persistencia de Datos   │
└─────────────────────────────┘

┌─────────────────────────────┐
│   CI/CD (GitHub Actions)    │
│   - Tests Automáticos       │
│   - Deploy Automático       │
└─────────────────────────────┘
```

## 🧩 Componentes

### 1. Base de Datos

- **Descripción:** Base de datos relacional PostgreSQL que almacena toda la información del sistema (habitaciones, huéspedes, reservas)
- **Tecnología:** PostgreSQL 12+
- **Proveedor:** AWS EC2 (self-hosted) / Desarrollo local
- **Esquema:** 3 tablas principales con relaciones foreign key
- **Archivo de esquema:** `schema/create_tables.sql`

**Tablas principales:**
- `huespedes`: Información de clientes (id, nombre, email, telefono)
- `habitaciones`: Catálogo de habitaciones (id, numero, tipo, precio)
- `reservas`: Registro de reservas (id, huesped_id, habitacion_id, fecha_ingreso, fecha_salida)

### 2. Backend API

- **Descripción:** API RESTful desarrollada con FastAPI que maneja toda la lógica de negocio
- **Tecnología:** Python 3.11+ con FastAPI 0.104+
- **URL Producción:** `http://TU_IP_EC2/api/` (o `http://localhost/api/` en Docker)
- **Repositorio:** [Este repositorio]
- **Características:**
  - Validación automática con Pydantic
  - ORM con SQLAlchemy
  - Documentación interactiva (Swagger/ReDoc)
  - CORS habilitado para desarrollo

**Endpoints principales:**

**Habitaciones:**
- `POST /api/habitaciones/` - Crear habitación
- `GET /api/habitaciones/` - Listar todas las habitaciones

**Huéspedes:**
- `POST /api/huespedes/` - Crear huésped
- `GET /api/huespedes/` - Listar todos los huéspedes
- `GET /api/huespedes/{id}` - Obtener huésped por ID
- `PUT /api/huespedes/{id}` - Actualizar huésped
- `DELETE /api/huespedes/{id}` - Eliminar huésped

**Reservas:**
- `POST /api/reservas/` - Crear reserva
- `GET /api/reservas/` - Listar todas las reservas
- `GET /api/reservas/{id}` - Obtener reserva por ID
- `PUT /api/reservas/{id}` - Actualizar reserva
- `DELETE /api/reservas/{id}` - Eliminar reserva

### 3. Frontend

- **Descripción:** Interfaz web responsiva con JavaScript vanilla para interacción dinámica
- **Tecnología:** HTML5, CSS3, JavaScript ES6+, Jinja2 (templates)
- **URL Producción:** `http://TU_IP_EC2/` (o `http://localhost/` en Docker)
- **Repositorio:** [Este repositorio - carpeta src/templates y src/static]
- **Características:**
  - Diseño responsivo con gradientes y animaciones
  - Operaciones CRUD completas sin recargar página
  - Validación de formularios
  - Feedback visual para acciones del usuario

---

## 🔄 Flujo de Datos

1. **Usuario interactúa con el Frontend**
   - Llena formularios o hace clic en botones (Crear, Editar, Eliminar)
   - JavaScript captura eventos y valida datos

2. **Frontend hace request HTTP al Backend API**
   - Peticiones asíncronas con `fetch()` API
   - Formato JSON para envío/recepción de datos
   - Endpoints RESTful (`/api/huespedes/`, `/api/reservas/`, etc.)

3. **Backend API consulta/modifica Base de Datos**
   - FastAPI recibe request y valida con Pydantic schemas
   - SQLAlchemy ORM realiza operaciones en PostgreSQL
   - Se aplican restricciones de integridad y validaciones de negocio

4. **Backend API retorna respuesta al Frontend**
   - Respuesta JSON con datos solicitados o confirmación
   - Códigos HTTP estándar (200, 201, 404, 500, etc.)
   - Manejo de errores con mensajes descriptivos

5. **Frontend actualiza la interfaz**
   - JavaScript recibe respuesta y actualiza DOM dinámicamente
   - Se muestran listas actualizadas sin recargar página
   - Feedback visual (animaciones, mensajes de éxito/error)

---
## 🎯 Funcionalidades

### ✅ Funcionalidades Implementadas

#### Habitaciones
- ✅ **Listar habitaciones**: Ver todas las habitaciones con número, tipo y precio
- ✅ **Crear habitación**: Agregar nuevas habitaciones al sistema
- ✅ **Validación**: Control de campos requeridos y precios positivos

#### Huéspedes
- ✅ **Listar huéspedes**: Ver registro completo de huéspedes
- ✅ **Crear huésped**: Registrar nuevos huéspedes con validación de email
- ✅ **Editar huésped**: Actualizar información existente
- ✅ **Eliminar huésped**: Remover huéspedes del sistema (con cascada en reservas)

#### Reservas
- ✅ **Listar reservas**: Ver todas las reservas activas
- ✅ **Crear reserva**: Generar nuevas reservas con validación de fechas
- ✅ **Editar reserva**: Modificar fechas y detalles de reservas existentes
- ✅ **Eliminar reserva**: Cancelar reservas
- ✅ **Validación de integridad**: Verifica que huésped y habitación existan

#### Generales
- ✅ **Interfaz web moderna**: Diseño responsive con animaciones CSS
- ✅ **Operaciones asíncronas**: CRUD sin recargar página
- ✅ **Documentación interactiva**: Swagger UI y ReDoc automáticos
- ✅ **Validación de datos**: Cliente y servidor con feedback inmediato

---

## 🛠️ Stack Tecnológico

### Backend
- **Framework:** FastAPI 0.104.1
- **ORM:** SQLAlchemy 2.0.23
- **Validación:** Pydantic 2.5.0
- **Base de Datos:** PostgreSQL 12+ con psycopg2-binary
- **Servidor:** Uvicorn 0.24.0 con workers
- **Seguridad:** Passlib, Python-Jose (preparado para JWT)

### Frontend
- **Markup:** HTML5 con Jinja2 templates
- **Estilos:** CSS3 (gradientes, animaciones, flexbox)
- **Scripts:** JavaScript ES6+ (async/await, fetch API)
- **Diseño:** Responsive sin frameworks CSS

### Infraestructura
- **Cloud:** AWS EC2 (Ubuntu 22.04 LTS)
- **Reverse Proxy:** Nginx
- **Contenedores:** Docker + Docker Compose
- **CI/CD:** GitHub Actions
- **Control de Versiones:** Git + GitHub

### Deployment
- **Producción:** AWS EC2 con systemd services
- **Desarrollo:** Docker Compose (web + db containers)
- **Automatización:** GitHub Actions para tests y deploy

---

## 🌐 URLs de la Aplicación

### Producción (AWS EC2)
- **Frontend:** `http://TU_IP_PUBLICA_EC2/`
- **Backend API:** `http://TU_IP_PUBLICA_EC2/api/`
- **Swagger Docs:** `http://TU_IP_PUBLICA_EC2/docs`
- **ReDoc:** `http://TU_IP_PUBLICA_EC2/redoc`

### Desarrollo (Docker Local)
- **Frontend:** `http://localhost/`
- **Backend API:** `http://localhost/api/`
- **Swagger Docs:** `http://localhost/docs`
- **ReDoc:** `http://localhost/redoc`

### GitHub
- **Repositorio:** `https://github.com/paulatatian/hotelapi`
- **GitHub Project:** `https://github.com/users/paulatatian/projects/[TU_PROJECT_NUMBER]`

---

## 💻 Instalación Local

### Prerrequisitos

- Python 3.11 o superior
- PostgreSQL 12 o superior
- pip (gestor de paquetes Python)
- Git
- Navegador web moderno

### Paso 1: Clonar Repositorio
```bash
# Clonar el proyecto
git clone https://github.com/paulatatian/hotelapi.git
cd hotelapi
```

### Paso 2: Configurar Base de Datos
```bash
# Instalar PostgreSQL (si no lo tienes)
# Windows: Descargar desde https://www.postgresql.org/download/

# Iniciar servicio PostgreSQL

# Crear base de datos y usuario
sudo -u postgres psql
```
```sql
-- En el prompt de PostgreSQL
CREATE DATABASE hotel_db;
CREATE USER hotel_user WITH PASSWORD 'tu_password_seguro';
GRANT ALL PRIVILEGES ON DATABASE hotel_db TO hotel_user;
\q
```
```bash
# Crear tablas usando el script SQL
psql -U hotel_user -d hotel_db -f schema/create_tables.sql
```

### Paso 3: Configurar Backend
```bash
# Crear entorno virtual
python3 -m venv venv

# Windows
venv\Scripts\activate

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Configurar variable de entorno para la base de datos
# Crear archivo .env en la raíz del proyecto
echo 'DATABASE_URL=postgresql://hotel_user:tu_password_seguro@localhost:5432/hotel_db' > .env
```

### Paso 4: Ejecutar Aplicación
```bash
# Iniciar servidor (desde la raíz del proyecto)
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# O usando el comando completo
python -m uvicorn src.main:app --reload
```

### Paso 5: Acceder a la Aplicación

Abre tu navegador y visita:
- **Aplicación:** `http://localhost:8000/`
- **Documentación API:** `http://localhost:8000/docs`

---

## 🐳 Inicio Rápido con Docker

### Prerrequisitos
- Docker Desktop instalado y corriendo
- Docker Compose incluido

### Paso 1: Preparar Proyecto
```bash
# Clonar repositorio
git clone https://github.com/paulatatian/hotelapi.git
cd hotelapi
```

### Paso 2: Configurar Variables de Entorno
```bash
# Crear archivo .env (opcional, docker-compose tiene defaults)
cat > .env << EOF
DATABASE_URL=postgresql://postgres:1940@db:5432/hotel_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=1940
POSTGRES_DB=hotel_db
EOF
```

### Paso 3: Construir e Iniciar Contenedores
```bash
# Construir imágenes e iniciar servicios en background
docker-compose up -d

# Ver logs en tiempo real
docker-compose logs -f

# Ver solo logs del web service
docker-compose logs -f web
```

### Paso 4: Verificar Estado
```bash
# Ver contenedores corriendo
docker ps

# Deberías ver:
# - hotelapi-web (puerto 80)
# - hotelapi-db (puerto 5432)

# Verificar salud de la aplicación
curl http://localhost/docs
```

### Paso 5: Acceder a la Aplicación

- 🌐 **App:** `http://localhost`
- 📚 **Swagger UI:** `http://localhost/docs`
- 📖 **ReDoc:** `http://localhost/redoc`

### Comandos Útiles Docker
```bash
# Ver logs en tiempo real
docker-compose logs -f

# Reiniciar servicios
docker-compose restart

# Detener contenedores (mantiene volúmenes)
docker-compose stop

# Detener y eliminar contenedores
docker-compose down

# Eliminar contenedores Y volúmenes (⚠️ borra datos)
docker-compose down -v

# Reconstruir imágenes sin caché
docker-compose build --no-cache

# Restart completo (útil después de cambios)
docker-compose down
docker-compose up -d

# Ver uso de recursos
docker stats

# Ejecutar comandos dentro del contenedor web
docker-compose exec web bash

# Ejecutar comandos en la base de datos
docker-compose exec db psql -U postgres -d hotel_db

# Ver estructura de base de datos
docker-compose exec db psql -U postgres -d hotel_db -c "\dt"
```

### Troubleshooting Docker

**Puerto 80 ocupado:**
```bash
# Editar docker-compose.yml
# Cambiar: "80:80" por "8000:80"
# Acceder en: http://localhost:8000
```

**Ver logs de errores:**
```bash
docker-compose logs web | grep -i error
docker-compose logs db | grep -i error
```

**Reiniciar desde cero:**
```bash
docker-compose down -v
docker-compose build --no-cache
docker-compose up -d
```

---

## ☁️ Despliegue en AWS EC2

### Requisitos Previos

1. **Cuenta de AWS** con acceso a EC2
2. **Instancia EC2** configurada:
   - **AMI:** Ubuntu Server 22.04 LTS
   - **Tipo:** t2.micro (Free Tier) o superior
   - **Almacenamiento:** 8 GB mínimo
3. **Security Group** con reglas:
   - Puerto 22 (SSH) - Solo tu IP
   - Puerto 80 (HTTP) - 0.0.0.0/0
   - Puerto 443 (HTTPS) - 0.0.0.0/0 (opcional)
4. **Par de claves SSH** (.pem file) o acceso EC2 Instance Connect

### Paso 1: Conectar a EC2

#### Opción A: EC2 Instance Connect (Recomendado)
```bash
# Desde AWS Console:
# 1. Ve a EC2 → Instances
# 2. Selecciona tu instancia
# 3. Click en "Connect"
# 4. Pestaña "EC2 Instance Connect"
# 5. Click "Connect"
```

### Paso 2: Actualizar Sistema e Instalar Dependencias
```bash
# Actualizar paquetes del sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependencias necesarias
sudo apt install -y \
    python3-pip \
    python3-venv \
    nginx \
    postgresql \
    postgresql-contrib \
    git

# Verificar instalaciones
python3 --version  # Debe ser 3.10+
psql --version     # Debe ser 12+
nginx -v           # Cualquier versión reciente
```

### Paso 3: Configurar PostgreSQL
```bash
# Iniciar servicio PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Crear base de datos y usuario
sudo -u postgres psql
```
```sql
-- Ejecutar en el prompt de PostgreSQL
CREATE DATABASE hotel_db;
CREATE USER hotel_user WITH PASSWORD 'TU_PASSWORD_SEGURO_AQUI';
GRANT ALL PRIVILEGES ON DATABASE hotel_db TO hotel_user;

-- Verificar creación
\l
\du

-- Salir
\q
```
```bash
# Permitir conexiones locales (opcional)
sudo nano /etc/postgresql/14/main/pg_hba.conf
# Asegurar que exista esta línea:
# local   all             all                                     md5

# Reiniciar PostgreSQL
sudo systemctl restart postgresql
```

### Paso 4: Clonar y Configurar Aplicación
```bash
# Ir al directorio home
cd /home/ubuntu

# Clonar repositorio
git clone https://github.com/paulatatian/hotelapi.git
cd hotelapi

# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Actualizar pip e instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt
```

### Paso 5: Configurar Variables de Entorno
```bash
# Crear archivo .env
nano .env
```
```bash
# Contenido del archivo .env
DATABASE_URL=postgresql://hotel_user:TU_PASSWORD_SEGURO_AQUI@localhost:5432/hotel_db
```
```bash
# Guardar (Ctrl+O, Enter, Ctrl+X)

# Cargar variables de entorno
source .env
```

### Paso 6: Inicializar Base de Datos
```bash
# Opción 1: Usar script SQL
psql -U hotel_user -d hotel_db -f schema/create_tables.sql

# Verificar tablas creadas
psql -U hotel_user -d hotel_db -c "\dt"
```

### Paso 7: Configurar Servicio Systemd para Uvicorn
```bash
# Crear archivo de servicio
sudo nano /etc/systemd/system/uvicorn.service
```
```ini
[Unit]
Description=Uvicorn server for FastAPI HotelApp
After=network.target postgresql.service

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/hotelapi
Environment="PATH=/home/ubuntu/hotelapi/venv/bin"
Environment="DATABASE_URL=postgresql://hotel_user:TU_PASSWORD_SEGURO_AQUI@localhost:5432/hotel_db"
ExecStart=/home/ubuntu/hotelapi/venv/bin/uvicorn src.main:app --host 127.0.0.1 --port 8000 --workers 2
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```
```bash
# Guardar y cerrar (Ctrl+O, Enter, Ctrl+X)

# Recargar systemd
sudo systemctl daemon-reload

# Habilitar servicio al iniciar
sudo systemctl enable uvicorn

# Iniciar servicio
sudo systemctl start uvicorn

# Verificar estado
sudo systemctl status uvicorn

# Ver logs si hay problemas
sudo journalctl -u uvicorn -f
```

### Paso 8: Configurar Nginx como Reverse Proxy
```bash
# Crear archivo de configuración
sudo nano /etc/nginx/sites-available/hotelapi
```
```nginx
server {
    listen 80;
    server_name _;  # Acepta cualquier dominio (o coloca tu IP/dominio)

    # Logs
    access_log /var/log/nginx/hotelapi_access.log;
    error_log /var/log/nginx/hotelapi_error.log;

    # Proxy hacia FastAPI
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Archivos estáticos (opcional, FastAPI ya los sirve)
    location /static/ {
        alias /home/ubuntu/hotelapi/src/static/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```
```bash
# Guardar y cerrar

# Crear symlink para habilitar sitio
sudo ln -s /etc/nginx/sites-available/hotelapi /etc/nginx/sites-enabled/

# Eliminar sitio default
sudo rm /etc/nginx/sites-enabled/default

# Verificar configuración de Nginx
sudo nginx -t

# Si todo está OK, reiniciar Nginx
sudo systemctl restart nginx

# Verificar estado
sudo systemctl status nginx
```

### Paso 10: Verificar Despliegue
```bash
# Obtener IP pública de tu instancia
curl http://checkip.amazonaws.com

# O desde AWS Console: EC2 → Instances → Tu instancia → Public IPv4 address
```

**Abre tu navegador y visita:**
- `http://TU_IP_PUBLICA/`
- `http://TU_IP_PUBLICA/docs`

### Paso 11: Actualizar Aplicación (Futuras Actualizaciones)
```bash
# Conectar a EC2
ssh -i "tu-clave.pem" ubuntu@ec2-XX-XX-XX-XX.compute-1.amazonaws.com

# Ir al directorio del proyecto
cd /home/ubuntu/hotelapi

# Pull últimos cambios
git pull origin main

# Activar entorno virtual
source venv/bin/activate

# Actualizar dependencias (si cambiaron)
pip install -r requirements.txt

# Reiniciar servicio
sudo systemctl restart uvicorn

# Verificar estado
sudo systemctl status uvicorn

# Ver logs si hay problemas
sudo journalctl -u uvicorn -n 50
```

---

## 🤖 CI/CD con GitHub Actions

### ¿Qué se Automatiza?

El proyecto incluye workflows de GitHub Actions para automatizar:

- ✅ **Tests automáticos** en cada push/PR
- ✅ **Validación de código** (linting)
- ✅ **Verificación de dependencias**
- ✅ **Deploy automático a EC2** (configuración opcional)

### Workflows Configurados

#### 1. CI (Integración Continua)

**Archivo:** `.github/workflows/ci.yml`

**Se ejecuta cuando:**
- Haces `push` a rama `main`
- Abres o actualizas un Pull Request
- Manualmente desde GitHub Actions tab

**Pasos que ejecuta:**
1. Checkout del código
2. Setup de Python 3.12
3. Instalación de dependencias
4. Ejecución de tests (si existen en `tests/`)
5. Validación de imports y sintaxis

#### 2. Deploy (Despliegue Continuo)

**Archivo:** `.github/workflows/ci.yml` (sección deploy)

**Configuración adicional requerida:**
```bash
# En GitHub: Settings → Secrets and variables → Actions
# Agregar estos secrets:

EC2_HOST        # IP pública de tu EC2
EC2_USER        # ubuntu
EC2_KEY         # Contenido completo de tu archivo .pem
```

**Pasos que ejecuta:**
1. Conecta a EC2 vía SSH
2. Hace `git pull` del último código
3. Actualiza dependencias Python
4. Reinicia servicios (uvicorn + nginx)

#### Paso 2: Habilitar GitHub Actions
```bash
# Los workflows ya están en .github/workflows/
# GitHub los detecta automáticamente

# Para verificar:
# 1. Ve a tu repo en GitHub
# 2. Click en pestaña "Actions"
# 3. Deberías ver los workflows listados
```

#### Paso 3: Probar CI/CD
```bash
# Hacer un cambio simple y pushearlo
cd hotelapi
echo "# Test CI/CD" >> README.md
git add README.md
git commit -m "Test: Verificar GitHub Actions"
git push origin main

# Ir a GitHub → Actions para ver el workflow corriendo
```
---

## 📚 API Endpoints

### Base URL

- **Producción:** `http://TU_IP_EC2/api/`
- **Local:** `http://localhost:8000/api/`


## 🏠 Habitaciones

### 1. Obtener todas las habitaciones

**GET** `/api/habitaciones/`

**Descripción**: Retorna la lista completa de habitaciones disponibles en el hotel.

**Parámetros**: Ninguno

**Response 200 OK**:
```json
[
  {
    "id": 1,
    "numero": "101",
    "tipo": "Suite Presidencial",
    "precio": 500000
  },
  {
    "id": 2,
    "numero": "102",
    "tipo": "Suite Junior",
    "precio": 350000
  }
]
```

**Ejemplo con cURL**:
```bash
curl -X GET "http://[IP_PUBLICA_EC2]/api/habitaciones/"
```

---

### 2. Crear una habitación

**POST** `/api/habitaciones/`

**Descripción**: Crea una nueva habitación en el sistema.

**Request Body**:
```json
{
  "numero": "305",
  "tipo": "Doble Deluxe",
  "precio": 280000
}
```

**Parámetros requeridos**:
- `numero` (string): Número único de la habitación
- `tipo` (string): Tipo de habitación
- `precio` (integer): Precio por noche en pesos

**Response 200 OK**:
```json
{
  "id": 13,
  "numero": "305",
  "tipo": "Doble Deluxe",
  "precio": 280000
}
```

**Ejemplo con cURL**:
```bash
curl -X POST "http://[IP_PUBLICA_EC2]/api/habitaciones/" \
  -H "Content-Type: application/json" \
  -d '{
    "numero": "305",
    "tipo": "Doble Deluxe",
    "precio": 280000
  }'
```

---

## 👥 Huéspedes

### 1. Obtener todos los huéspedes

**GET** `/api/huespedes/`

**Descripción**: Retorna la lista completa de huéspedes registrados.

**Parámetros**: Ninguno

**Response 200 OK**:
```json
[
  {
    "id": 1,
    "nombre": "Carlos Rodríguez",
    "email": "carlos.rodriguez@email.com",
    "telefono": "3001234567"
  }
]
```

---

### 2. Obtener un huésped por ID

**GET** `/api/huespedes/{id}`

**Descripción**: Retorna la información de un huésped específico.

**Parámetros**:
- `id` (path, integer, requerido): ID del huésped

**Response 200 OK**:
```json
{
  "id": 1,
  "nombre": "Carlos Rodríguez",
  "email": "carlos.rodriguez@email.com",
  "telefono": "3001234567"
}
```

**Response 404 Not Found**:
```json
{
  "detail": "Huésped no encontrado"
}
```

---

### 3. Crear un huésped

**POST** `/api/huespedes/`

**Descripción**: Registra un nuevo huésped en el sistema.

**Request Body**:
```json
{
  "nombre": "María García",
  "email": "maria.garcia@email.com",
  "telefono": "3101234567"
}
```

**Parámetros requeridos**:
- `nombre` (string): Nombre completo del huésped
- `email` (string): Email único del huésped
- `telefono` (string, opcional): Número de teléfono

**Response 200 OK**:
```json
{
  "id": 11,
  "nombre": "María García",
  "email": "maria.garcia@email.com",
  "telefono": "3101234567"
}
```

---

### 4. Actualizar un huésped

**PUT** `/api/huespedes/{id}`

**Descripción**: Actualiza la información de un huésped existente.

**Parámetros**:
- `id` (path, integer, requerido): ID del huésped a actualizar

**Request Body**:
```json
{
  "nombre": "María García López",
  "email": "maria.garcia.lopez@email.com",
  "telefono": "3109876543"
}
```

**Response 200 OK**:
```json
{
  "id": 11,
  "nombre": "María García López",
  "email": "maria.garcia.lopez@email.com",
  "telefono": "3109876543"
}
```

---

### 5. Eliminar un huésped

**DELETE** `/api/huespedes/{id}`

**Descripción**: Elimina un huésped del sistema. También elimina todas sus reservas asociadas (CASCADE).

**Parámetros**:
- `id` (path, integer, requerido): ID del huésped a eliminar

**Response 200 OK**:
```json
{
  "mensaje": "Huésped eliminado correctamente"
}
```

---

## 📅 Reservas

### 1. Obtener todas las reservas

**GET** `/api/reservas/`

**Descripción**: Retorna todas las reservas registradas en el sistema.

**Parámetros**: Ninguno

**Response 200 OK**:
```json
[
  {
    "id": 1,
    "huesped_id": 1,
    "habitacion_id": 1,
    "fecha_ingreso": "2024-12-01",
    "fecha_salida": "2024-12-05"
  }
]
```

---

### 2. Obtener una reserva por ID

**GET** `/api/reservas/{id}`

**Descripción**: Retorna información detallada de una reserva específica.

**Parámetros**:
- `id` (path, integer, requerido): ID de la reserva

**Response 200 OK**:
```json
{
  "id": 1,
  "huesped_id": 1,
  "habitacion_id": 1,
  "fecha_ingreso": "2024-12-01",
  "fecha_salida": "2024-12-05"
}
```

---

### 3. Crear una reserva

**POST** `/api/reservas/`

**Descripción**: Crea una nueva reserva validando que el huésped y la habitación existan.

**Request Body**:
```json
{
  "huesped_id": 2,
  "habitacion_id": 5,
  "fecha_ingreso": "2025-01-15",
  "fecha_salida": "2025-01-20"
}
```

**Parámetros requeridos**:
- `huesped_id` (integer): ID del huésped que reserva
- `habitacion_id` (integer): ID de la habitación a reservar
- `fecha_ingreso` (date): Fecha de check-in (formato: YYYY-MM-DD)
- `fecha_salida` (date): Fecha de check-out (formato: YYYY-MM-DD)

**Validaciones**:
- ✅ El huésped debe existir
- ✅ La habitación debe existir
- ✅ `fecha_salida` debe ser mayor que `fecha_ingreso`

**Response 200 OK**:
```json
{
  "id": 14,
  "huesped_id": 2,
  "habitacion_id": 5,
  "fecha_ingreso": "2025-01-15",
  "fecha_salida": "2025-01-20"
}
```

**Response 404 Not Found**:
```json
{
  "detail": "Huésped no encontrado"
}
```

---

### 4. Actualizar una reserva

**PUT** `/api/reservas/{id}`

**Descripción**: Modifica los datos de una reserva existente.

**Parámetros**:
- `id` (path, integer, requerido): ID de la reserva a actualizar

**Request Body**:
```json
{
  "huesped_id": 2,
  "habitacion_id": 5,
  "fecha_ingreso": "2025-01-16",
  "fecha_salida": "2025-01-22"
}
```

**Response 200 OK**:
```json
{
  "id": 14,
  "huesped_id": 2,
  "habitacion_id": 5,
  "fecha_ingreso": "2025-01-16",
  "fecha_salida": "2025-01-22"
}
```

---

### 5. Eliminar una reserva

**DELETE** `/api/reservas/{id}`

**Descripción**: Cancela y elimina una reserva del sistema.

**Parámetros**:
- `id` (path, integer, requerido): ID de la reserva a eliminar

**Response 200 OK**:
```json
{
  "mensaje": "Reserva eliminada correctamente"
}
```

---
## ⚠️ Problemas y Soluciones

### Problema 1: Error de conexión a PostgreSQL

**Descripción:** La aplicación no puede conectarse a la base de datos

**Solución:**
```bash
# Verificar que PostgreSQL esté corriendo
sudo systemctl status postgresql

# Si está detenido, iniciarlo
sudo systemctl start postgresql

# Verificar credenciales en .env
cat .env
# DATABASE_URL debe coincidir con usuario/password creados

# Probar conexión manual
psql -U hotel_user -d hotel_db -h localhost

# Verificar logs de PostgreSQL
sudo tail -f /var/log/postgresql/postgresql-14-main.log
```

### Problema 2: Puerto 80 ocupado en Docker

**Descripción:** Error `port is already allocated`

**Solución:**
```bash
# Opción 1: Cambiar puerto en docker-compose.yml
nano docker-compose.yml
# Cambiar "80:80" por "8000:80"

# Opción 2: Encontrar y matar proceso en puerto 80
sudo lsof -i :80
sudo kill -9 [PID]

# Luego reiniciar
docker-compose up -d
```

### Problema 3: Uvicorn no inicia en EC2

**Descripción:** Servicio uvicorn falla al iniciar

**Solución:**
```bash
# Ver logs detallados
sudo journalctl -u uvicorn -n 100

# Errores comunes:
# 1. DATABASE_URL incorrecto
sudo nano /etc/systemd/system/uvicorn.service
# Verificar Environment="DATABASE_URL=..."

# 2. Permisos incorrectos
sudo chown -R ubuntu:www-data /home/ubuntu/hotelapi
chmod -R 755 /home/ubuntu/hotelapi

# 3. Python path incorrecto
# Verificar que /home/ubuntu/hotelapi/venv/bin/uvicorn existe
ls -la /home/ubuntu/hotelapi/venv/bin/

# Después de cambios, recargar
sudo systemctl daemon-reload
sudo systemctl restart uvicorn
```
---

### Troubleshooting GitHub Actions

**Error: Permission denied (publickey)**
```bash
# Verificar que EC2_KEY tenga el contenido completo del .pem
# Incluir -----BEGIN RSA PRIVATE KEY----- y -----END RSA PRIVATE KEY-----
```

**Error: Connection timeout**
```bash
# Verificar que EC2_HOST sea la IP pública correcta
# Verificar que Security Group permita SSH desde GitHub IPs
# (Mejor: usar 0.0.0.0/0 para SSH o rangos de GitHub Actions)
```

**Tests fallan**
```bash
# Si no tienes tests, el workflow los skipea automáticamente
# Para agregar tests:
mkdir -p tests
# Crear archivos test_*.py con pytest
```
---

## 📊 Estructura del Proyecto

```
hotelapi/
├── README.md                   # Esta documentación
├── .env.example                # Ejemplo de variables de entorno
├── requirements.txt            # Dependencias Python
├── main.py                     # Aplicación principal FastAPI
├── database.py                 # Configuración de conexión a BD
├── models.py                   # Modelos SQLAlchemy (ORM)
├── schemas.py                  # Schemas Pydantic (validación)
├── routers/                    # Endpoints API organizados
│   ├── habitaciones.py         # CRUD Habitaciones
│   ├── huespedes.py            # CRUD Huéspedes
│   └── reservas.py             # CRUD Reservas
├── schema/                     # Scripts de base de datos
│   ├── diagram.png             # Diagrama ER
│   └── create_tables.sql       # Creación de tablas
├── data/
│   └── sample_data.sql         # Datos de prueba
├── screenshots/
│   ├── postman/                # Capturas de pruebas Postman
│   └── ...                     # Otras capturas
├── static/                     # Archivos estáticos (CSS, JS)
├── templates/                  # Templates HTML (opcional)
└── docker-compose.yml          # Configuración Docker (opcional)
```


### Requisitos Cumplidos

| Requisito | Estado | Evidencia |
|-----------|--------|-----------|
| API REST con CRUD | ✅ | 3 entidades con 5 operaciones c/u |
| Conexión a BD Actividad 7 | ✅ | PostgreSQL en AWS EC2 |
| Despliegue en cloud | ✅ | AWS EC2 + Nginx |
| Documentación de endpoints | ✅ | Este README + Swagger |
| Pruebas funcionando | ✅ | Screenshots en `screenshots/postman/` |
| Variables de entorno | ✅ | `.env.example` incluido |
| Instalación local | ✅ | Instrucciones paso a paso |

 ### 📞 Soporte y Contacto
Estudiante: Paula Tatian
GitHub: https://github.com/paulatatian
Repositorio: https://github.com/paulatatian/hotelapi

  ### 📄 Licencia
MIT License - Ver archivo LICENSE para más detalles.
