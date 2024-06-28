# controllers/usuario_controller.py
import sqlite3
from models.usuario import Usuario


class UsuarioController:
    def __init__(self, db_path):
        self.db_path = db_path

    def obtener_usuarios(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = [Usuario(*row) for row in cursor.fetchall()]
        conn.close()
        return usuarios

    def agregar_usuario(self, nombre, apellido, email, dni, celular, rol):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, apellido, email, dni, celular, roles_idrol) VALUES (?, ?, ?, ?, ?, ?)",
                       (nombre, apellido, email, dni, celular, rol))
        conn.commit()
        conn.close()

    def actualizar_usuario(self, id, nombre, apellido, email, dni, celular, rol):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET nombre=?, apellido=?, email=?, dni=?, celular=?, roles_idrol=? WHERE id_usuario=?",
                       (nombre, apellido, email, dni, celular, rol, id))
        conn.commit()
        conn.close()

    def eliminar_usuario(self, id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id_usuario=?", (id,))
        conn.commit()
        conn.close()
