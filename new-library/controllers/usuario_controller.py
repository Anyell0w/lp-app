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

    def agregar_usuario(self, nombre, apellido, email ,dni,     celular, roles_idrol):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, apellido, email, dni, celular, roles_idrol) VALUES (?, ?, ?, ?, ?, ?)", (nombre, apellido, email, dni, celular, roles_idrol))
        conn.commit()
        conn.close()

    def actualizar_usuario(self, id, nombre, apellido, email, dni, celular, roles_idrol):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET nombre=?, email=?, email=?, dni=?,celular=?, roles_idrol=? WHERE id_usuario=?", (nombre, email, dni, celular, roles_idrol, id))
        conn.commit()
        conn.close()

    def eliminar_usuario(self, id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id_usuario=?", (id,))
        conn.commit()
        conn.close()

    def buscar_usuarios(self, filtro):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre LIKE ? OR email LIKE ?", ('%' + filtro + '%', '%' + filtro + '%'))
        usuarios_encontrados = [Usuario(*row) for row in cursor.fetchall()]
        conn.close()
        return usuarios_encontrados
