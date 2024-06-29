import tkinter as tk
from tkinter import ttk
from controllers.categoria_controller import CategoriaController

class CategoriaView:
    def __init__(self, root, categoria_controller):
        self.root = root
        self.categoria_controller = categoria_controller
        self.create_widgets()
        self.cargar_categorias()

    def create_widgets(self):
        self.search_frame = ttk.Frame(self.root)
        self.search_frame.pack(fill='x')

        self.search_label = ttk.Label(self.search_frame, text="Buscar:")
        self.search_label.pack(side='left', padx=(5, 0))

        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.pack(side='left', padx=(5, 5), fill='x', expand=True)

        self.search_button = ttk.Button(self.search_frame, text="Buscar", command=self.buscar_categorias)
        self.search_button.pack(side='left')

        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Descripcion"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripcion", text="Descripcion")
        self.tree.pack(expand=True, fill='both')

        self.btn_nueva = ttk.Button(self.root, text="Nueva Categoria", command=self.nueva_categoria)
        self.btn_nueva.pack(side="left")

        self.btn_actualizar = ttk.Button(self.root, text="Actualizar Categoria", command=self.actualizar_categoria)
        self.btn_actualizar.pack(side="left")

        self.btn_eliminar = ttk.Button(self.root, text="Eliminar Categoria", command=self.eliminar_categoria)
        self.btn_eliminar.pack(side="left")

    def cargar_categorias(self):
        for categoria in self.categoria_controller.obtener_categorias():
            self.tree.insert('', 'end', values=(categoria.id, categoria.nombre, categoria.descripcion))

    def buscar_categorias(self):
        query = self.search_entry.get().lower()
        categorias = self.categoria_controller.obtener_categorias()
        filtered = [categoria for categoria in categorias if query in categoria.nombre.lower() or query in categoria.descripcion.lower()]

        self.tree.delete(*self.tree.get_children())
        for categoria in filtered:
            self.tree.insert('', 'end', values=(categoria.id, categoria.nombre, categoria.descripcion))

    def nueva_categoria(self):
        self.nueva_categoria_window = tk.Toplevel(self.root)
        self.nueva_categoria_window.title("Nueva Categoria")
        self.nueva_categoria_window.geometry("200x200")

        self.lbl_nombre = ttk.Label(self.nueva_categoria_window, text="Nombre")
        self.lbl_nombre.pack()
        self.entry_nombre = ttk.Entry(self.nueva_categoria_window)
        self.entry_nombre.pack()

        self.lbl_descripcion = ttk.Label(self.nueva_categoria_window, text="Descripción")
        self.lbl_descripcion.pack()
        self.entry_descripcion = ttk.Entry(self.nueva_categoria_window)
        self.entry_descripcion.pack()

        self.btn_guardar = ttk.Button(self.nueva_categoria_window, text="Guardar", command=self.guardar_categoria)
        self.btn_guardar.pack()

    def guardar_categoria(self):
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        self.categoria_controller.agregar_categoria(nombre, descripcion)
        self.nueva_categoria_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_categorias()

    def actualizar_categoria(self):
        self.actualizar_categoria_window = tk.Toplevel(self.root)
        self.actualizar_categoria_window.title("Actualizar Categoria")
        self.actualizar_categoria_window.geometry("200x200")

        self.lbl_id = ttk.Label(self.actualizar_categoria_window, text="ID")
        self.lbl_id.pack()
        self.entry_id = ttk.Entry(self.actualizar_categoria_window)
        self.entry_id.pack()

        self.lbl_nombre = ttk.Label(self.actualizar_categoria_window, text="Nombre")
        self.lbl_nombre.pack()
        self.entry_nombre = ttk.Entry(self.actualizar_categoria_window)
        self.entry_nombre.pack()

        self.lbl_descripcion = ttk.Label(self.actualizar_categoria_window, text="Descripción")
        self.lbl_descripcion.pack()
        self.entry_descripcion = ttk.Entry(self.actualizar_categoria_window)
        self.entry_descripcion.pack()

        self.btn_actualizar = ttk.Button(self.actualizar_categoria_window, text="Actualizar", command=self.actualizar)
        self.btn_actualizar.pack()

    def actualizar(self):
        id = self.entry_id.get()
        nombre = self.entry_nombre.get()
        descripcion = self.entry_descripcion.get()
        self.categoria_controller.actualizar_categoria(id, nombre, descripcion)
        self.actualizar_categoria_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_categorias()

    def eliminar_categoria(self):
        self.eliminar_categoria_window = tk.Toplevel(self.root)
        self.eliminar_categoria_window.title("Eliminar Categoria")
        self.eliminar_categoria_window.geometry("200x200")

        self.lbl_id = ttk.Label(self.eliminar_categoria_window, text="ID")
        self.lbl_id.pack()
        self.entry_id = ttk.Entry(self.eliminar_categoria_window)
        self.entry_id.pack()

        self.btn_eliminar = ttk.Button(self.eliminar_categoria_window, text="Eliminar", command=self.eliminar)
        self.btn_eliminar.pack()

    def eliminar(self):
        id = self.entry_id.get()
        self.categoria_controller.eliminar_categoria(id)
        self.eliminar_categoria_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_categorias()
