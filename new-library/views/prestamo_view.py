# views/prestamo_view.py
import tkinter as tk
from tkinter import ttk
from controllers.prestamo_controller import PrestamoController


class PrestamoView:
    def __init__(self, root, prestamo_controller):
        self.root = root
        self.prestamo_controller = prestamo_controller
        self.create_widgets()
        self.cargar_prestamos()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=(
            "ID", "FechaPrestamo", "FechaEntrega", "IDLibro", "IDUsuario", "Devuelto"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("FechaPrestamo", text="Fecha Préstamo")
        self.tree.heading("FechaEntrega", text="Fecha Entrega")
        self.tree.heading("IDLibro", text="ID Libro")
        self.tree.heading("IDUsuario", text="ID Usuario")
        self.tree.heading("Devuelto", text="Devuelto")
        self.tree.pack(expand=True, fill='both')

        self.btn_nuevo = ttk.Button(
            self.root, text="Nuevo Préstamo", command=self.nuevo_prestamo)
        self.btn_nuevo.pack(side="left")

        self.btn_actualizar = ttk.Button(
            self.root, text="Actualizar Préstamo", command=self.actualizar_prestamo)
        self.btn_actualizar.pack(side="left")

        self.btn_eliminar = ttk.Button(
            self.root, text="Eliminar Préstamo", command=self.eliminar_prestamo)
        self.btn_eliminar.pack(side="left")

    def cargar_prestamos(self):
        for prestamo in self.prestamo_controller.obtener_prestamos():
            self.tree.insert('', 'end', values=(prestamo.id, prestamo.fecha_prestamo,
                             prestamo.fecha_entrega, prestamo.id_libro, prestamo.id_usuario, prestamo.devuelto))

    def nuevo_prestamo(self):
        self.nuevo_prestamo_window = tk.Toplevel(self.root)
        self.nuevo_prestamo_window.title("Nuevo Préstamo")
        self.nuevo_prestamo_window.geometry("200x200")

        self.lbl_fecha_prestamo = ttk.Label(self.nuevo_prestamo_window, text="Fecha Préstamo")
        self.lbl_fecha_prestamo.pack()
        self.entry_fecha_prestamo = ttk.Entry(self.nuevo_prestamo_window)
        self.entry_fecha_prestamo.pack()

        self.lbl_fecha_entrega = ttk.Label(self.nuevo_prestamo_window, text="Fecha Entrega")
        self.lbl_fecha_entrega.pack()
        self.entry_fecha_entrega = ttk.Entry(self.nuevo_prestamo_window)
        self.entry_fecha_entrega.pack()

        self.lbl_id_libro = ttk.Label(self.nuevo_prestamo_window, text="ID Libro")
        self.lbl_id_libro.pack()
        self.entry_id_libro = ttk.Entry(self.nuevo_prestamo_window)
        self.entry_id_libro.pack()

        self.lbl_id_usuario = ttk.Label(self.nuevo_prestamo_window, text="ID Usuario")
        self.lbl_id_usuario.pack()
        self.entry_id_usuario = ttk.Entry(self.nuevo_prestamo_window)
        self.entry_id_usuario.pack()

        self.lbl_devuelto = ttk.Label(self.nuevo_prestamo_window, text="Devuelto")
        self.lbl_devuelto.pack()
        self.entry_devuelto = ttk.Entry(self.nuevo_prestamo_window)
        self.entry_devuelto.pack()

        self.btn_guardar = ttk.Button(
            self.nuevo_prestamo_window, text="Guardar", command=self.guardar_prestamo)
        self.btn_guardar.pack()

    def guardar_prestamo(self):
        fecha_prestamo = self.entry_fecha_prestamo.get()
        fecha_entrega = self.entry_fecha_entrega.get()
        id_libro = self.entry_id_libro.get()
        id_usuario = self.entry_id_usuario.get()
        devuelto = self.entry_devuelto.get()
        self.prestamo_controller.agregar_prestamo(fecha_prestamo, fecha_entrega, id_libro, id_usuario, devuelto)
        self.nuevo_prestamo_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_prestamos()

    def actualizar_prestamo(self):
        self.actualizar_prestamo_window = tk.Toplevel(self.root)
        self.actualizar_prestamo_window.title("Actualizar Préstamo")
        self.actualizar_prestamo_window.geometry("200x200")

        self.lbl_id = ttk.Label(self.actualizar_prestamo_window, text="ID")
        self.lbl_id.pack()
        self.entry_id = ttk.Entry(self.actualizar_prestamo_window)
        self.entry_id.pack()

        self.lbl_fecha_prestamo = ttk.Label(self.actualizar_prestamo_window, text="Fecha Préstamo")
        self.lbl_fecha_prestamo.pack()
        self.entry_fecha_prestamo = ttk.Entry(self.actualizar_prestamo_window)
        self.entry_fecha_prestamo.pack()

        self.lbl_fecha_entrega = ttk.Label(self.actualizar_prestamo_window, text="Fecha Entrega")
        self.lbl_fecha_entrega.pack()
        self.entry_fecha_entrega = ttk.Entry(self.actualizar_prestamo_window)
        self.entry_fecha_entrega.pack()

        self.lbl_id_libro = ttk.Label(self.actualizar_prestamo_window, text="ID Libro")
        self.lbl_id_libro.pack()
        self.entry_id_libro = ttk.Entry(self.actualizar_prestamo_window)
        self.entry_id_libro.pack()

        self.lbl_id_usuario = ttk.Label(self.actualizar_prestamo_window, text="ID Usuario")
        self.lbl_id_usuario.pack()
        self.entry_id_usuario = ttk.Entry(self.actualizar_prestamo_window)
        self.entry_id_usuario.pack()

        self.lbl_devuelto = ttk.Label(self.actualizar_prestamo_window, text="Devuelto")
        self.lbl_devuelto.pack()
        self.entry_devuelto = ttk.Entry(self.actualizar_prestamo_window)
        self.entry_devuelto.pack()

        self.btn_guardar = ttk.Button(
            self.actualizar_prestamo_window, text="Guardar", command=self.guardar_actualizacion)
        self.btn_guardar.pack()

    def guardar_actualizacion(self):
        id = self.entry_id.get()
        fecha_prestamo = self.entry_fecha_prestamo.get()
        fecha_entrega = self.entry_fecha_entrega.get()
        id_libro = self.entry_id_libro.get()
        id_usuario = self.entry_id_usuario.get()
        devuelto = self.entry_devuelto.get()
        self.prestamo_controller.actualizar_prestamo(id, fecha_prestamo, fecha_entrega, id_libro, id_usuario, devuelto)
        self.actualizar_prestamo_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_prestamos()

    def eliminar_prestamo(self):
        self.eliminar_prestamo_window = tk.Toplevel(self.root)
        self.eliminar_prestamo_window.title("Eliminar Préstamo")
        self.eliminar_prestamo_window.geometry("200x200")

        self.lbl_id = ttk.Label(self.eliminar_prestamo_window, text="ID")
        self.lbl_id.pack()
        self.entry_id = ttk.Entry(self.eliminar_prestamo_window)
        self.entry_id.pack()

        self.btn_eliminar = ttk.Button(
            self.eliminar_prestamo_window, text="Eliminar", command=self.eliminar)
        self.btn_eliminar.pack()

    def eliminar(self):
        id = self.entry_id.get()
        self.prestamo_controller.eliminar_prestamo(id)
        self.eliminar_prestamo_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_prestamos()
