from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
import models
from routers import habitaciones, huespedes, reservas

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Hotel con Frontend")

# Routers API
app.include_router(habitaciones.router, prefix="/api")
app.include_router(huespedes.router, prefix="/api")
app.include_router(reservas.router, prefix="/api")

# Carpeta de archivos estáticos y templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Rutas para páginas HTML
@app.get("/", name="Inicio")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/habitaciones-page", name="Habitaciones")
def view_habitaciones(request: Request):
    return templates.TemplateResponse("habitaciones.html", {"request": request})

@app.get("/huespedes-page", name="Huéspedes")
def view_huespedes(request: Request):
    return templates.TemplateResponse("huespedes.html", {"request": request})

@app.get("/reservas-page", name="Reservas")
def view_reservas(request: Request):
    return templates.TemplateResponse("reservas.html", {"request": request})

# CORS: permite cualquier origen (para desarrollo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
