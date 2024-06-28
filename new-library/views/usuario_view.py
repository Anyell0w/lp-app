# views/usuario_view.py
import tkinter as tk
from tkinter import ttk
from controllers.usuario_controller import UsuarioController


class UsuarioView:
    def __init__(self, root, usuario_controller):
        self.root = root
        self.usuario_controller = usuario_controller
        self.create_widgets()
        self.cargar_usuarios()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=(
            "ID", "Nombre", "Apellido", "Email", "DNI", "Celular", "Rol"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Apellido", text="Apellido")
        self.tree.heading("Email", text="Email")
        self.tree.heading("DNI", text="DNI")
        self.tree.heading("Celular", text="Celular")
        self.tree.heading("Rol", text="Rol")
        self.tree.pack(expand=True, fill='both')

        self.btn_nuevo = ttk.Button(
            self.root, text="Nuevo Usuario", command=self.nuevo_usuario)
        self.btn_nuevo.pack(side="left")

        self.btn_actualizar = ttk.Button(
            self.root, text="Actualizar Usuario", command=self.actualizar_usuario)
        self.btn_actualizar.pack(side="left")

        self.btn_eliminar = ttk.Button(
            self.root, text="Eliminar Usuario", command=self.eliminar_usuario)
        self.btn_eliminar.pack(side="left")

    def cargar_usuarios(self):
        for usuario in self.usuario_controller.obtener_usuarios():
            self.tree.insert('', 'end', values=(usuario.id, usuario.nombre, usuario.apellido,
                             usuario.email, usuario.dni, usuario.celular, usuario.rol))

    def nuevo_usuario(self):
        self.nuevo_usuario_window = tk.Toplevel(self.root)
        self.nuevo_usuario_window.title("Nuevo Usuario")
        self.nuevo_usuario_window.geometry("400x400")

        self.nombre_label = ttk.Label(self.nuevo_usuario_window, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = ttk.Entry(self.nuevo_usuario_window)
        self.nombre_entry.pack()

        self.apellido_label = ttk.Label(self.nuevo_usuario_window, text="Apellido:")
        self.apellido_label.pack()
        self.apellido_entry = ttk.Entry(self.nuevo_usuario_window)
        self.apellido_entry.pack()

        self.email_label = ttk.Label(self.nuevo_usuario_window, text="Email:")
        self.email_label.pack()
        self.email_entry = ttk.Entry(self.nuevo_usuario_window)
        self.email_entry.pack()

        self.dni_label = ttk.Label(self.nuevo_usuario_window, text="DNI:")
        self.dni_label.pack()
        self.dni_entry = ttk.Entry(self.nuevo_usuario_window)
        self.dni_entry.pack()

        self.celular_label = ttk.Label(self.nuevo_usuario_window, text="Celular:")
        self.celular_label.pack()
        self.celular_entry = ttk.Entry(self.nuevo_usuario_window)
        self.celular_entry.pack()

        self.rol_label = ttk.Label(self.nuevo_usuario_window, text="Rol:")
        self.rol_label.pack()
        self.rol_entry = ttk.Entry(self.nuevo_usuario_window)
        self.rol_entry.pack()

        self.btn_guardar = ttk.Button(
            self.nuevo_usuario_window, text="Guardar", command=self.guardar_usuario)
        self.btn_guardar.pack()

    def guardar_usuario(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        email = self.email_entry.get()
        dni = self.dni_entry.get()
        celular = self.celular_entry.get()
        rol = self.rol_entry.get()
        self.usuario_controller.agregar_usuario(
            nombre, apellido, email, dni, celular, rol)
        self.nuevo_usuario_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_usuarios()

    def actualizar_usuario(self):
        self.actualizar_usuario_window = tk.Toplevel(self.root)
        self.actualizar_usuario_window.title("Actualizar Usuario")
        self.actualizar_usuario_window.geometry("400x400")

        self.id_label = ttk.Label(self.actualizar_usuario_window, text="ID:")
        self.id_label.pack()
        self.id_entry = ttk.Entry(self.actualizar_usuario_window)
        self.id_entry.pack()

        self.nombre_label = ttk.Label(self.actualizar_usuario_window, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = ttk.Entry(self.actualizar_usuario_window)
        self.nombre_entry.pack()

        self.apellido_label = ttk.Label(self.actualizar_usuario_window, text="Apellido:")
        self.apellido_label.pack()
        self.apellido_entry = ttk.Entry(self.actualizar_usuario_window)
        self.apellido_entry.pack()

        self.email_label = ttk.Label(self.actualizar_usuario_window, text="Email:")
        self.email_label.pack()
        self.email_entry = ttk.Entry(self.actualizar_usuario_window)
        self.email_entry.pack()

        self.dni_label = ttk.Label(self.actualizar_usuario_window, text="DNI:")
        self.dni_label.pack()
        self.dni_entry = ttk.Entry(self.actualizar_usuario_window)
        self.dni_entry.pack()

        self.celular_label = ttk.Label(self.actualizar_usuario_window, text="Celular:")
        self.celular_label.pack()
        self.celular_entry = ttk.Entry(self.actualizar_usuario_window)
        self.celular_entry.pack()

        self.rol_label = ttk.Label(self.actualizar_usuario_window, text="Rol:")
        self.rol_label.pack()
        self.rol_entry = ttk.Entry(self.actualizar_usuario_window)
        self.rol_entry.pack()

        self.btn_actualizar = ttk.Button(
            self.actualizar_usuario_window, text="Actualizar", command=self.actualizar)
        self.btn_actualizar.pack()

    def actualizar(self):
        id = self.id_entry.get()
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        email = self.email_entry.get()
        dni = self.dni_entry.get()
        celular = self.celular_entry.get()
        rol = self.rol_entry.get()
        self.usuario_controller.actualizar_usuario(
            id, nombre, apellido, email, dni, celular, rol)
        self.actualizar_usuario_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_usuarios()

    def eliminar_usuario(self):
        self.eliminar_usuario_window = tk.Toplevel(self.root)
        self.eliminar_usuario_window.title("Eliminar Usuario")
        self.eliminar_usuario_window.geometry("400x400")

        self.id_label = ttk.Label(self.eliminar_usuario_window, text="ID:")
        self.id_label.pack()
        self.id_entry = ttk.Entry(self.eliminar_usuario_window)
        self.id_entry.pack()

        self.btn_eliminar = ttk.Button(
            self.eliminar_usuario_window, text="Eliminar", command=self.eliminar)
        self.btn_eliminar.pack()

    def eliminar(self):
        id = self.id_entry.get()
        self.usuario_controller.eliminar_usuario(id)
        self.eliminar_usuario_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_usuarios()
