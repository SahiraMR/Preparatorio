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
def guardar_usuarios(lista: List[Usuario]):
    with open(RUTA_CSV, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "nombre", "correo", "tipo"])
        writer.writeheader()
        for u in lista:
            writer.writerow(u.dict())

def agregar_usuario(usuario: Usuario):
    usuarios = leer_usuarios()
    usuarios.append(usuario)
    guardar_usuarios(usuarios)

def obtener_usuario_por_id(user_id: int) -> Optional[Usuario]:
    usuarios = leer_usuarios()
    for u in usuarios:
        if u.id == user_id:
            return u
    return None


