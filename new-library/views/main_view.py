import tkinter as tk
from tkinter import ttk
from controllers.libro_controller import LibroController
from controllers.usuario_controller import UsuarioController
from controllers.prestamo_controller import PrestamoController
from controllers.categoria_controller import CategoriaController
from controllers.rol_controller import RolController

from views.libro_view import LibroView
from views.usuario_view import UsuarioView
from views.prestamo_view import PrestamoView
from views.categoria_view import CategoriaView
from views.rol_view import RolView


class MainView:
    def __init__(self, root, rol):
        self.root = root
        self.root.title("Sistema de Biblioteca")

        self.libro_controller = LibroController('./Biblioteca')
        self.usuario_controller = UsuarioController('./Biblioteca')
        self.prestamo_controller = PrestamoController('./Biblioteca')
        self.categoria_controller = CategoriaController('./Biblioteca')
        self.rol_controller = RolController('./Biblioteca')
        rol = self.rol_controller.get_rol(rol)
        if rol == "admin":
            self.create_widgets()
        elif rol == "user":
            self.create_widgets_user()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        # Frame y vista de Libros
        self.frame_libros = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_libros, text='Libros')
        self.libro_view = LibroView(self.frame_libros, self.libro_controller)

        # Frame y vista de Usuarios
        self.frame_usuarios = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_usuarios, text='Usuarios')
        self.usuario_view = UsuarioView(self.frame_usuarios, self.usuario_controller)

        # Frame y vista de Préstamos
        self.frame_prestamos = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_prestamos, text='Préstamos')
        self.prestamo_view = PrestamoView(self.frame_prestamos, self.prestamo_controller)

        # Frame y vista de Categorías
        self.frame_categorias = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_categorias, text='Categorías')
        self.categoria_view = CategoriaView(self.frame_categorias, self.categoria_controller)

        # Frame y vista de Roles
        self.frame_roles = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_roles, text='Roles')
        self.rol_view = RolView(self.frame_roles, self.rol_controller)

        # Estilos generales
        self.style = ttk.Style()
        self.style.configure('TButton', padding=6, relief='flat', background='#ccc')
        self.style.configure('TLabel', padding=6, relief='flat', background='#ccc')
        self.style.configure('TEntry', padding=6, relief='flat', background='#ccc')
        self.style.configure('TFrame', padding=6, relief='flat', background='#ccc')
        self.style.configure('TNotebook', padding=6, relief='flat', background='#ccc')
        self.style.configure('TNotebook.Tab', padding=6, relief='flat', background='#ccc')
        self.style.configure('TCombobox', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Heading', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Item', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Cell', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Row', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Column', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Item', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Item', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Item', padding=6, relief='flat', background='#ccc')

        # Estilos específicos
        # Estilos para las tablas
        self.style.configure('Treeview', rowheight=30)
        self.style.configure('Treeview.Heading', font=('Arial', 12))
        self.style.configure('Treeview', font=('Arial', 12))
        self.style.configure('Treeview', background='#ccc')
        self.style.configure('Treeview', fieldbackground='#ccc')
        self.style.configure('Treeview', foreground='black')
        self.style.configure('Treeview', selectbackground='#ccc')
        self.style.configure('Treeview', selectforeground='black')
        self.style.configure('Treeview', selectmode='browse')
        self.style.configure('Treeview', show='headings')
        self.style.configure('Treeview', takefocus=True)
        self.style.configure('Treeview', height=10)
        self.style.configure('Treeview', columns=('ID', 'Nombre', 'Descripción', 'Fecha de Creación'))
        self.style.configure('Treeview', displaycolumns=('ID', 'Nombre', 'Descripción', 'Fecha de Creación'))
        self.style.configure('Treeview', selectmode='browse')
        self.style.configure('Treeview', padding=6)
        self.style.configure('Treeview', relief='flat')

        # Fondo de la ventana
        self.root.configure(bg='#ccc')

        # Estilos de los botones
        self.style.configure('TButton', font=('Arial', 12))
        self.style.configure('TButton', background='#ccc')
        self.style.configure('TButton', foreground='black')
        self.style.configure('TButton', relief='flat')
        self.style.configure('TButton', padding=6)
        self.style.configure('TButton', width=20)
        self.style.configure('TButton', anchor='center')
        self.style.configure('TButton', takefocus=True)
        self.style.configure('TButton', cursor='hand2')


    def create_widgets_user(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill='both')

        # Frame y vista de Libros
        self.frame_libros = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_libros, text='Libros')
        self.libro_view = LibroView(self.frame_libros, self.libro_controller)

        # Frame y vista de Categoria
        self.frame_categorias = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_categorias, text='Categorías')
        self.categoria_view = CategoriaView(self.frame_categorias, self.categoria_controller)
         


        # Estilos generales
        self.style = ttk.Style()
        self.style.configure('TButton', padding=6, relief='flat', background='#ccc')
        self.style.configure('TLabel', padding=6, relief='flat', background='#ccc')
        self.style.configure('TEntry', padding=6, relief='flat', background='#ccc')
        self.style.configure('TFrame', padding=6, relief='flat', background='#ccc')
        self.style.configure('TNotebook', padding=6, relief='flat', background='#ccc')
        self.style.configure('TNotebook.Tab', padding=6, relief='flat', background='#ccc')
        self.style.configure('TCombobox', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Heading', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Item', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Cell', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Row', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Column', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Item', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Item', padding=6, relief='flat', background='#ccc')
        self.style.configure('Treeview.Item', padding=6, relief='flat', background='#ccc')

        # Estilos específicos
        self.style.configure('Treeview', rowheight=30)
        self.style.configure('Treeview.Heading', font=('Arial', 12))
        self.style.configure('Treeview', font=('Arial', 12))
        self.style.configure('Treeview', background='#ccc')
        self.style.configure('Treeview', fieldbackground='#ccc')
        self.style.configure('Treeview', foreground='black')
        self.style.configure('Treeview', selectbackground='#ccc')
        self.style.configure('Treeview', selectforeground='black')
        self.style.configure('Treeview', selectmode='browse')
        self.style.configure('Treeview', show='headings')
        self.style.configure('Treeview', takefocus=True)
        self.style.configure('Treeview', height=10)
        