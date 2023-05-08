from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import modelo


# ##############################################
# VISTA
# ##############################################
class Panel:
    def __init__(self, window):
        self.root = window
        self.root.title("Tarea POO")
        self.titulo = Label(
            self.root,
            text="Ingrese sus datos",
            bg="DarkOrchid3",
            fg="thistle1",
            height=1,
            width=60,
        )
        self.titulo.grid(row=0, column=0, columnspan=5, padx=1, pady=1, sticky=W + E)

        try:
            print("pasa codigo")
        except:
            print("Error")
        self.producto = Label(self.root, text="Producto")
        self.producto.grid(row=1, column=0, sticky=W)
        self.cantidad = Label(self.root, text="Cantidad")
        self.cantidad.grid(row=2, column=0, sticky=W)
        self.precio = Label(self.root, text="Precio")
        self.precio.grid(row=3, column=0, sticky=W)
        self.base_datos = Label(self.root, text="Nombre BD")
        self.base_datos.grid(row=1, column=2, sticky=W)
        self.tipo_base_datos = Label(self.root, text="Tipo de BD [R/NR]")
        self.tipo_base_datos.grid(row=2, column=2, sticky=W)

        # Defino variables para tomar valores de campos de entrada
        self.a_val, self.b_val, self.c_val, self.d_val, self.e_val = (
            StringVar(),
            DoubleVar(),
            DoubleVar(),
            StringVar(),
            StringVar(),
        )
        w_ancho = 20

        self.entrada1 = Entry(self.root, textvariable=self.a_val, width=w_ancho)
        self.entrada1.grid(row=1, column=1)
        self.entrada2 = Entry(self.root, textvariable=self.b_val, width=w_ancho)
        self.entrada2.grid(row=2, column=1)
        self.entrada3 = Entry(self.root, textvariable=self.c_val, width=w_ancho)
        self.entrada3.grid(row=3, column=1)
        self.entrada4 = Entry(self.root, textvariable=self.d_val, width=w_ancho)
        self.entrada4.grid(row=1, column=3)
        self.entrada5 = Entry(self.root, textvariable=self.e_val, width=w_ancho)
        self.entrada5.grid(row=2, column=3)

        # -------------------------------------------------
        self.objeto1 = modelo.Abmc()

        self.objeto = modelo.DataBase()

        # --------------------------------------------------
        # TREEVIEW
        # --------------------------------------------------

        self.tree = ttk.Treeview(self.root)
        self.tree["columns"] = ("col1", "col2", "col3")
        self.tree.column("#0", width=90, minwidth=50, anchor=W)
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.column("col3", width=200, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Producto")
        self.tree.heading("col2", text="cantidad")
        self.tree.heading("col3", text="precio")
        self.tree.grid(row=10, column=0, columnspan=5)

        self.boton_alta = Button(
            self.root,
            text="Alta",
            command=lambda: self.objeto1.alta(
                self.a_val.get(),
                self.b_val.get(),
                self.c_val.get(),
                self.tree,
                self.d_val.get(),
                self.e_val.get(),
            ),
        )
        self.boton_alta.grid(row=6, column=1)

        self.boton_bd = Button(
            self.root,
            text="conectar/crear bd",
            command=lambda: self.objeto.conexion_bd(
                self.d_val.get(),
                self.e_val.get(),
            ),
        )
        self.boton_bd.grid(row=2, column=4)

        self.boton_modifica = Button(
            root,
            text="Modificar",
            command=lambda: self.objeto1.modifica(
                self.a_val,
                self.b_val,
                self.c_val,
                self.d_val,
                self.tree,
            ),
        )
        self.boton_modifica.grid(row=6, column=2)

        self.boton_consulta = Button(
            root,
            text="Consulta",
            command=lambda: self.objeto1.actualizar_treeview(
                self.tree,
                self.d_val.get(),
                self.e_val.get(),
            ),
        )

        self.boton_consulta.grid(row=6, column=4)

        self.boton_borrar = Button(
            root,
            text="Borrar",
            command=lambda: self.objeto1.borrar(
                self.tree, self.d_val.get(), self.e_val.get(), self.a_val.get()
            ),
        )
        self.boton_borrar.grid(row=6, column=3)


# #####################################
# Para mi futuro controlador
# #####################################
if __name__ == "__main__":
    root = Tk()
    mi_app = Panel(root)
    root.mainloop()
