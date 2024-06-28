# views/libro_view.py
import tkinter as tk
from tkinter import ttk
from controllers.libro_controller import LibroController


class LibroView:
    def __init__(self, root, libro_controller):
        self.root = root
        self.libro_controller = libro_controller
        self.create_widgets()
        self.cargar_libros()

    def create_widgets(self):

        self.search_frame = ttk.Frame(self.root)
        self.search_frame.pack(fill='x')

        self.search_label = ttk.Label(self.search_frame, text="Buscar:")
        self.search_label.pack(side='left', padx=(5, 0))

        self.search_entry = ttk.Entry(self.search_frame)
        self.search_entry.pack(side='left', padx=(5, 5), fill='x', expand=True)

        self.search_button = ttk.Button(self.search_frame, text="Buscar", command=self.buscar_libros)
        self.search_button.pack(side='left')

        self.tree = ttk.Treeview(self.root, columns=(
            "ID", "Titulo", "Autor", "Genero", "Año"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Titulo", text="Titulo")
        self.tree.heading("Autor", text="Autor")
        self.tree.heading("Genero", text="Genero")
        self.tree.heading("Año", text="Año")
        self.tree.pack(expand=True, fill='both')

        self.btn_nuevo = ttk.Button(
            self.root, text="Nuevo Libro", command=self.nuevo_libro)
        self.btn_nuevo.pack(side="left")

        self.btn_actualizar = ttk.Button(
            self.root, text="Actualizar Libro", command=self.actualizar_libro)
        self.btn_actualizar.pack(side="left")

        self.btn_eliminar = ttk.Button(
            self.root, text="Eliminar Libro", command=self.eliminar_libro)
        self.btn_eliminar.pack(side="left")

    def cargar_libros(self):
        for libro in self.libro_controller.obtener_libros():
            self.tree.insert('', 'end', values=(
                libro.id, libro.titulo, libro.autor, libro.genero, libro.año))

    def nuevo_libro(self):
        self.nuevo_libro_window = tk.Toplevel(self.root)
        self.nuevo_libro_window.title("Nuevo Libro")
        self.nuevo_libro_window.geometry("200x200")

        self.lbl_titulo = ttk.Label(self.nuevo_libro_window, text="Titulo")
        self.lbl_titulo.pack()
        self.entry_titulo = ttk.Entry(self.nuevo_libro_window)
        self.entry_titulo.pack()

        self.lbl_autor = ttk.Label(self.nuevo_libro_window, text="Autor")
        self.lbl_autor.pack()
        self.entry_autor = ttk.Entry(self.nuevo_libro_window)
        self.entry_autor.pack()

        self.lbl_genero = ttk.Label(self.nuevo_libro_window, text="Genero")
        self.lbl_genero.pack()
        self.entry_genero = ttk.Entry(self.nuevo_libro_window)
        self.entry_genero.pack()

        self.lbl_año = ttk.Label(self.nuevo_libro_window, text="Año")
        self.lbl_año.pack()
        self.entry_año = ttk.Entry(self.nuevo_libro_window)
        self.entry_año.pack()

        self.btn_guardar = ttk.Button(
            self.nuevo_libro_window, text="Guardar", command=self.guardar_libro)
        self.btn_guardar.pack()

    def guardar_libro(self):
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        genero = self.entry_genero.get()
        año = self.entry_año.get()
        self.libro_controller.agregar_libro(titulo, autor, genero, año)
        self.nuevo_libro_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_libros()

    def actualizar_libro(self):
        self.actualizar_libro_window = tk.Toplevel(self.root)
        self.actualizar_libro_window.title("Actualizar Libro")
        self.actualizar_libro_window.geometry("200x200")

        self.lbl_id = ttk.Label(self.actualizar_libro_window, text="ID")
        self.lbl_id.pack()
        self.entry_id = ttk.Entry(self.actualizar_libro_window)
        self.entry_id.pack()

        self.lbl_titulo = ttk.Label(
            self.actualizar_libro_window, text="Titulo")
        self.lbl_titulo.pack()
        self.entry_titulo = ttk.Entry(self.actualizar_libro_window)
        self.entry_titulo.pack()

        self.lbl_autor = ttk.Label(self.actualizar_libro_window, text="Autor")
        self.lbl_autor.pack()
        self.entry_autor = ttk.Entry(self.actualizar_libro_window)
        self.entry_autor.pack()

        self.lbl_genero = ttk.Label(
            self.actualizar_libro_window, text="Genero")
        self.lbl_genero.pack()
        self.entry_genero = ttk.Entry(self.actualizar_libro_window)
        self.entry_genero.pack()

        self.lbl_año = ttk.Label(self.actualizar_libro_window, text="Año")
        self.lbl_año.pack()
        self.entry_año = ttk.Entry(self.actualizar_libro_window)
        self.entry_año.pack()

        self.btn_guardar = ttk.Button(
            self.actualizar_libro_window, text="Guardar", command=self.guardar_actualizacion)
        self.btn_guardar.pack()

    def guardar_actualizacion(self):
        id = self.entry_id.get()
        titulo = self.entry_titulo.get()
        autor = self.entry_autor.get()
        genero = self.entry_genero.get()
        año = self.entry_año.get()
        self.libro_controller.actualizar_libro(id, titulo, autor, genero, año)
        self.actualizar_libro_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_libros()

    def eliminar_libro(self):
        self.eliminar_libro_window = tk.Toplevel(self.root)
        self.eliminar_libro_window.title("Eliminar Libro")
        self.eliminar_libro_window.geometry("200x200")

        self.lbl_id = ttk.Label(self.eliminar_libro_window, text="ID")
        self.lbl_id.pack()
        self.entry_id = ttk.Entry(self.eliminar_libro_window)
        self.entry_id.pack()

        self.btn_eliminar = ttk.Button(
            self.eliminar_libro_window, text="Eliminar", command=self.eliminar)
        self.btn_eliminar.pack()

    def eliminar(self):
        id = self.entry_id.get()
        self.libro_controller.eliminar_libro(id)
        self.eliminar_libro_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_libros()

    def buscar_libros(self):
        titulo = self.search_entry.get()
        self.tree.delete(*self.tree.get_children())
        for libro in self.libro_controller.buscar_libros(titulo):
            self.tree.insert('', 'end', values=(
                libro.id, libro.titulo, libro.autor, libro.genero, libro.año))
