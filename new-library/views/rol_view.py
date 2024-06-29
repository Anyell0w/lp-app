import tkinter as tk
from tkinter import ttk
from controllers.rol_controller import RolController


class RolView:
    def __init__(self, root, rol_controller):
        self.root = root
        self.rol_controller = rol_controller
        self.create_widgets()
        self.cargar_roles()

    def create_widgets(self):
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nombre"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.pack(expand=True, fill='both')

        self.btn_nuevo = ttk.Button(
            self.root, text="Nuevo Rol", command=self.nuevo_rol)
        self.btn_nuevo.pack(side="left")

        self.btn_actualizar = ttk.Button(
            self.root, text="Actualizar Rol", command=self.actualizar_rol)
        self.btn_actualizar.pack(side="left")

        self.btn_eliminar = ttk.Button(
            self.root, text="Eliminar Rol", command=self.eliminar_rol)
        self.btn_eliminar.pack(side="left")

        # Barra de búsqueda
        self.lbl_buscar = ttk.Label(self.root, text="Buscar:")
        self.lbl_buscar.pack(side="left")
        self.entry_buscar = ttk.Entry(self.root)
        self.entry_buscar.pack(side="left", padx=5)
        self.btn_buscar = ttk.Button(self.root, text="Buscar", command=self.buscar_roles)
        self.btn_buscar.pack(side="left")

    def cargar_roles(self):
        self.tree.delete(*self.tree.get_children())
        for rol in self.rol_controller.obtener_roles():
            self.tree.insert('', 'end', values=(rol.id, rol.nombre))

    def nuevo_rol(self):
        self.nuevo_rol_window = tk.Toplevel(self.root)
        self.nuevo_rol_window.title("Nuevo Rol")
        self.nuevo_rol_window.geometry("200x100")

        self.lbl_nombre = ttk.Label(self.nuevo_rol_window, text="Nombre")
        self.lbl_nombre.pack()
        self.entry_nombre = ttk.Entry(self.nuevo_rol_window)
        self.entry_nombre.pack()

        self.btn_guardar = ttk.Button(
            self.nuevo_rol_window, text="Guardar", command=self.guardar_rol)
        self.btn_guardar.pack()

    def guardar_rol(self):
        nombre = self.entry_nombre.get()
        self.rol_controller.agregar_rol(nombre)
        self.nuevo_rol_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_roles()

    def actualizar_rol(self):
        selected_item = self.tree.selection()
        if selected_item:
            rol_id = self.tree.item(selected_item)['values'][0]
            self.actualizar_rol_window = tk.Toplevel(self.root)
            self.actualizar_rol_window.title("Actualizar Rol")
            self.actualizar_rol_window.geometry("200x100")

            self.lbl_nombre = ttk.Label(self.actualizar_rol_window, text="Nombre")
            self.lbl_nombre.pack()
            self.entry_nombre = ttk.Entry(self.actualizar_rol_window)
            self.entry_nombre.pack()
            self.entry_nombre.insert(0, self.tree.item(selected_item)['values'][1])

            self.btn_guardar = ttk.Button(
                self.actualizar_rol_window, text="Guardar", command=lambda: self.guardar_actualizacion(rol_id))
            self.btn_guardar.pack()

    def guardar_actualizacion(self, rol_id):
        nombre = self.entry_nombre.get()
        self.rol_controller.actualizar_rol(rol_id, nombre)
        self.actualizar_rol_window.destroy()
        self.tree.delete(*self.tree.get_children())
        self.cargar_roles()

    def eliminar_rol(self):
        selected_item = self.tree.selection()
        if selected_item:
            rol_id = self.tree.item(selected_item)['values'][0]
            self.rol_controller.eliminar_rol(rol_id)
            self.tree.delete(selected_item)

    def buscar_roles(self):
        filtro = self.entry_buscar.get()
        self.tree.delete(*self.tree.get_children())
        if filtro:
            for rol in self.rol_controller.buscar_roles(filtro):
                self.tree.insert('', 'end', values=(rol.id, rol.nombre))
        else:
            self.cargar_roles()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestión de Roles")
    rol_controller = RolController("path_to_your_database.db")
    app = RolView(root, rol_controller)
    root.mainloop()
