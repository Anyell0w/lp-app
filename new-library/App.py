import tkinter as tk
from tkinter import messagebox as mb

class MainView:
# login window
    root = tk.Tk()

    lbl1 = tk.Label(root, text="Usuario", bg="white")
    lbl1.pack()
    lbl1.place(x=10, y=10)

    lbl2 = tk.Label(root, text="Contraseña", bg="white")
    lbl2.pack()
    lbl2.place(x=10, y=40)

    # login function
    entry1 = tk.Entry(root, width=20)
    entry1.pack()
    entry1.place(x=100, y=10)
    entry2 = tk.Entry(root, width=20)
    entry2.pack()
    entry2.place(x=100, y=40)


    def login():
        username = entry1.get()
        password = entry2.get()
        if username == "admin" and password == "admin":
            mb.showinfo("Login", "Operación exitosa")
            main_window()
        else:
            mb.showerror("Login", "Usuario o contraseña incorrectos")


    button = tk.Button(root, text="Login", command=login, font="Helvetica 12")
    button.pack()
    button.place(x=227, y=70)

    # estilizando la ventana

    root.resizable(0, 0)
    root.configure(bg="black")
    root.iconbitmap("./images/Logo_UNAP.ico")
    root.geometry("540x250")
    root.title("Login")

    # estilizando el boton y los labels

    button.config(bg="white", fg="black", padx=10,
                font="Sans 12", relief="solid", foreground="black",
                activebackground="white")
    lbl1.config(bg="black", fg="white", padx=10,
                relief="solid", font="Helvetica 12")
    lbl2.config(bg="black", fg="white", padx=10,
                relief="solid", font="Helvetica 12")
    entry1.config(show="", font="Helvetica 12", bd=2)
    entry2.config(show="*", font="Helvetica 12", bd=2)
    entry1.place(x=110)
    entry2.place(x=110)

    # agregando imagen al costado de la ventana con grid
    image = tk.PhotoImage(file="./images/images.png")
    label = tk.Label(root, image=image)
    label.pack()
    label.place(x=300, y=5)


    # register func

    def register():
        mb.askquestion("Register", "¿Desea registrarse?")


    lbl3 = tk.Label(root, text="¿No tienes cuenta?", bg="black", fg="white")
    lbl3.pack()
    lbl3.place(x=12, y=180)

    button2 = tk.Button(root, text="Regístrate", command=register)
    button2.pack()
    button2.place(x=30, y=200)


    # main window after login

    def main_window():
        root = tk.Tk()
        root.destroy()
        root2 = tk.Tk()
        root2.geometry("500x500")
        root2.title("Main Window")
        root2.resizable(0, 0)
        root2.configure(bg="black")
        root2.iconbitmap("./images/Logo_UNAP.ico")
        # menu bar
        menubar = tk.Menu(root2)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nuevo")
        filemenu.add_command(label="Abrir")
        filemenu.add_command(label="Guardar")
        filemenu.add_command(label="Cerrar")
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=root2.quit)
        menubar.add_cascade(label="Archivo", menu=filemenu)
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Cortar")
        editmenu.add_command(label="Copiar")
        editmenu.add_command(label="Pegar")
        menubar.add_cascade(label="Editar", menu=editmenu)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Ayuda")
        helpmenu.add_command(label="Acerca de...")
        menubar.add_cascade(label="Ayuda", menu=helpmenu)
        root2.config(menu=menubar)
        root2.mainloop()


    # run the app
    root.mainloop()
