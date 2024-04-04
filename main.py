from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker

# Define la URL de la base de datos SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Crea la instancia de la aplicación FastAPI
app = FastAPI()

# Crea la conexión a la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define el modelo de datos para la tabla Candidato
class Candidato(Base):
    __tablename__ = "candidatos"
    id = Column(Integer, primary_key=True, index=True)
    dni = Column(String, unique=True, index=True)
    nombre = Column(String)
    apellido = Column(String)

# Crea las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Define un modelo Pydantic para recibir los datos de entrada
class CandidatoCreate(BaseModel):
    dni: str
    nombre: str
    apellido: str

# Define la ruta para el endpoint /candidato con método POST
@app.post("/candidato")
def create_candidato(candidato: CandidatoCreate):
    # Crea una sesión de base de datos
    db = SessionLocal()
    # Crea una nueva instancia de Candidato con los datos recibidos
    db_candidato = Candidato(dni=candidato.dni, nombre=candidato.nombre, apellido=candidato.apellido)
    # Agrega el candidato a la sesión
    db.add(db_candidato)
    # Guarda los cambios en la base de datos
    db.commit()
    # Refresca el objeto candidato para asegurarse de que tenga el ID asignado
    db.refresh(db_candidato)
    # Devuelve el candidato creado
    return db_candidato