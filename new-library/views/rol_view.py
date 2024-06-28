# views/rol_view.py
import tkinter as tk
from tkinter import ttk
from controllers.rol_controller import RolController


class RolView:
    def __init__(self, root, rol_controller: RolController):
        self.root = root
        self.rol_controller = rol_controller
        self.create_widgets()
        self.cargar_roles()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.pack(expand=True, fill='both')

        self.btn_nuevo = ttk.Button(self.root, text="Nuevo Rol", command=self.nuevo_rol)
        self.btn_nuevo.pack(side="left")

        self.btn_actualizar = ttk.Button(self.root, text="Actualizar Rol", command=self.actualizar_rol)
        self.btn_actualizar.pack(side="left")

        self.btn_eliminar = ttk.Button(self.root, text="Eliminar Rol", command=self.eliminar_rol)
        self.btn_eliminar.pack(side="left")

    def cargar_roles(self):
        for rol in self.rol_controller.obtener_roles():
            self.tree.insert('', 'end', values=(rol.id, rol.nombre))

    def nuevo_rol(self):
        self.nuevo_rol_window = tk.Toplevel(self.root)
        self.nuevo_rol_window.title("Nuevo Rol")
        self.nuevo_rol_window.geometry("200x200")

        self.lbl_nombre = ttk.Label(self.nuevo_rol_window, text="Nombre")
        self.lbl_nombre.pack()
        self.entry_nombre = ttk.Entry(self.nuevo_rol_window)
        self.entry_nombre.pack()

        self.btn_guardar = ttk.Button(self.nuevo_rol_window, text="Guardar", command=self.guardar_rol)
        self.btn_guardar.pack()
        self.btn_guardar.focus()

    def guardar_rol(self):
        nombre = self.entry_nombre.get()
        self.rol_controller.agregar_rol(nombre)
        self.nuevo_rol_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_roles()

    def actualizar_rol(self):
        self.actualizar_rol_window = tk.Toplevel(self.root)
        self.actualizar_rol_window.title("Actualizar Rol")
        self.actualizar_rol_window.geometry("200x200")

        self.lbl_id = ttk.Label(self.actualizar_rol_window, text="ID")
        self.lbl_id.pack()
        self.entry_id = ttk.Entry(self.actualizar_rol_window)
        self.entry_id.pack()

        self.lbl_nombre = ttk.Label(self.actualizar_rol_window, text="Nombre")
        self.lbl_nombre.pack()
        self.entry_nombre = ttk.Entry(self.actualizar_rol_window)
        self.entry_nombre.pack()

        self.btn_actualizar = ttk.Button(self.actualizar_rol_window, text="Actualizar", command=self.guardar_actualizar_rol)
        self.btn_actualizar.pack()
        self.btn_actualizar.focus()

    def guardar_actualizar_rol(self):
        id = self.entry_id.get()
        nombre = self.entry_nombre.get()
        self.rol_controller.actualizar_rol(id, nombre)
        self.actualizar_rol_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_roles()

    def eliminar_rol(self):
        self.eliminar_rol_window = tk.Toplevel(self.root)
        self.eliminar_rol_window.title("Eliminar Rol")
        self.eliminar_rol_window.geometry("200x200")

        self.lbl_nombre = ttk.Label(self.eliminar_rol_window, text="Nombre")
        self.lbl_nombre.pack()
        self.entry_nombre = ttk.Entry(self.eliminar_rol_window)
        self.entry_nombre.pack()

        self.btn_eliminar = ttk.Button(self.eliminar_rol_window, text="Eliminar", command=self.eliminar)
        self.btn_eliminar.pack()
        self.btn_eliminar.focus()

    def eliminar(self):
        nombre = self.entry_nombre.get()
        self.rol_controller.eliminar_rol(nombre)
        self.eliminar_rol_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_roles()
