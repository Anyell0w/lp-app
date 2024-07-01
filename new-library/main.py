# main.py
import tkinter as tk
from tkinter import messagebox as mb
from views.main_view import MainView

if __name__ == '__main__':

    #login

    root = tk.Tk()
    lbl1 = tk.Label(root, text="Usuario", bg="white")
    lbl1.pack()
    lbl1.place(x=10, y=10)
    
    lbl2 = tk.Label(root, text="Contraseña", bg="white")
    lbl2.pack()
    lbl2.place(x=10, y=40)
    
    entry1 = tk.Entry(root, width=20)
    entry1.pack()
    entry1.place(x=100, y=10)
    entry2 = tk.Entry(root, width=20)
    entry2.pack()
    entry2.place(x=100, y=40)
    
    def login():
        username = entry1.get()
        password = entry2.get()
        rol = "admin"
        if username == "admin" and password == "admin":
            mb.showinfo("Login", "Operación exitosa")
            app = MainView(root,rol)
            root.geometry("1500x800")
        elif username == "user" and password == "user":
            mb.showinfo("Login", "Operación exitosa")
            rol = "user"
            app = MainView(root,rol)
            root.geometry("1500x800")
        else:
            mb.showerror("Login", "Usuario o contraseña incorrectos")

    
    button = tk.Button(root, text="Login", command=login, font="Helvetica 12")
    button.pack()
    button.place(x=227, y=70)
    
    root.resizable(0, 0)
    root.configure(bg="black")
    root.iconbitmap("./images/Logo_UNAP.ico")
    root.geometry("540x250")
    root.title("Login")
    
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

    image = tk.PhotoImage(file="./images/images.png")
    label = tk.Label(root, image=image)
    label.pack()
    label.place(x=300, y=10)
    
    def main_window():
        root.destroy()
        app = MainView(root)
    
    root.mainloop()

