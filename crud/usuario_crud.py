import csv
from typing import List, Optional
from models.usuario import Usuario

RUTA_CSV = "data/usuarios.csv"

def leer_usuarios() -> List[Usuario]:
    usuarios = []
    with open(RUTA_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            usuarios.append(Usuario(**{
                "id": int(row["id"]),
                "nombre": row["nombre"],
                "correo": row["correo"],
                "tipo": row["tipo"]
            }))
    return usuarios

