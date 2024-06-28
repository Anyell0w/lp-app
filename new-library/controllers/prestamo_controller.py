# controllers/prestamo_controller.py
import sqlite3
from models.prestamo import Prestamo


class PrestamoController:
    def __init__(self, db_path):
        self.db_path = db_path

    def obtener_prestamos(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM prestamos")
        prestamos = [Prestamo(*row) for row in cursor.fetchall()]
        conn.close()
        return prestamos

    def agregar_prestamo(self, fecha_prestamo, fecha_entrega, id_libro, id_usuario, devuelto):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO prestamos (fecha_prestamo, fecha_entrega, libros_idlibro, usuarios_idusuario, devuelto) VALUES (?, ?, ?, ?, ?)",
                       (fecha_prestamo, fecha_entrega, id_libro, id_usuario, devuelto))
        conn.commit()
        conn.close()

    def actualizar_prestamo(self, id, fecha_prestamo, fecha_entrega, id_libro, id_usuario, devuelto):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE prestamos SET fecha_prestamo=?, fecha_entrega=?, libros_idlibro=?, usuarios_idusuario=?, devuelto=? WHERE id_prestamo=?",
                       (fecha_prestamo, fecha_entrega, id_libro, id_usuario, devuelto, id))
        conn.commit()
        conn.close()

    def eliminar_prestamo(self, id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM prestamos WHERE id_prestamo=?", (id,))
        conn.commit()
        conn.close()
