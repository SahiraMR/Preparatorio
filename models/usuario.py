from pydantic import BaseModel
from typing import Literal


class Usuario(BaseModel):
    id: int
    nombre: str
    correo: str
    tipo: Literal["Premium", "Normal", "Inactivo"]
