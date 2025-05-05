from fastapi import FastAPI, HTTPException
from models.usuario import Usuario
from crud.usuario_crud import (
    leer_usuarios, agregar_usuario, obtener_usuario_por_id,
    eliminar_usuario, actualizar_usuario, filtrar_por_tipo
)

app = FastAPI(title="API de Usuarios")

@app.get("/")
def root():
    return {"mensaje": "Bienvenido a la API de usuarios"}

@app.get("/usuarios", response_model=list[Usuario])
def listar_usuarios():
    return leer_usuarios()

@app.get("/usuarios/{user_id}", response_model=Usuario)
def obtener_usuario(user_id: int):
    usuario = obtener_usuario_por_id(user_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.post("/usuarios", response_model=Usuario)
def crear_usuario(usuario: Usuario):
    if obtener_usuario_por_id(usuario.id):
        raise HTTPException(status_code=400, detail="ID ya existe")
    agregar_usuario(usuario)
    return usuario

@app.delete("/usuarios/{user_id}")
def borrar_usuario(user_id: int):
    if not eliminar_usuario(user_id):
        raise HTTPException(status_code=404, detail="No se pudo eliminar")
    return {"mensaje": "Usuario eliminado"}

@app.put("/usuarios/{user_id}", response_model=Usuario)
def actualizar(user_id: int, datos: Usuario):
    if not actualizar_usuario(user_id, datos):
        raise HTTPException(status_code=404, detail="No se pudo actualizar")
    return datos

@app.get("/usuarios/tipo/{tipo}", response_model=list[Usuario])
def usuarios_por_tipo(tipo: str):
    resultados = filtrar_por_tipo(tipo)
    return resultados
