# controllers/categoria_controller.py
import sqlite3
from models.categoria import Categoria


class CategoriaController:
    def __init__(self, db_path):
        self.db_path = db_path

    def obtener_categorias(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categoria")
        categorias = [Categoria(*row) for row in cursor.fetchall()]
        conn.close()
        return categorias

    def agregar_categoria(self, nombre, descripcion):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO categoria (nombre_categoria, descripcion) VALUES (?, ?)",
                       (nombre, descripcion))
        conn.commit()
        conn.close()

    def actualizar_categoria(self, id, nombre, descripcion):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE categoria SET nombre_categoria=?, descripcion=? WHERE id_categoria=?",
                       (nombre, descripcion, id))
        conn.commit()
        conn.close()

    def eliminar_categoria(self, id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM categoria WHERE id_categoria=?", (id,))
        conn.commit()
        conn.close()

    def buscar_categorias(self, filtro):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categoria WHERE nombre_categoria LIKE ? OR descripcion LIKE ?",
                       ('%' + filtro + '%', '%' + filtro + '%'))
        categorias = [Categoria(*row) for row in cursor.fetchall()]
        conn.close()
        return categorias