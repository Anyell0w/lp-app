# controllers/rol_controller.py
import sqlite3
from models.rol import Rol


class RolController:
    def __init__(self, db_path):
        self.db_path = db_path

    def obtener_roles(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM roles")
        roles = [Rol(*row) for row in cursor.fetchall()]
        conn.close()
        return roles

    def agregar_rol(self, nombre):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO roles (nombre_rol) VALUES (?)", (nombre,))
        conn.commit()
        conn.close()

    def actualizar_rol(self, id, nombre):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE roles SET nombre_rol=? WHERE id_rol=?", (nombre, id))
        conn.commit()
        conn.close()

    def eliminar_rol(self, id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM roles WHERE id_rol=?", (id,))
        conn.commit()
        conn.close()

    def buscar_roles(self, filtro):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM roles WHERE nombre_rol LIKE ?", ('%' + filtro + '%',))
        roles_encontrados = [Rol(*row) for row in cursor.fetchall()]
        conn.close()
        return roles_encontrados
