import sqlite3
import re
import pymongo
from pymongo import MongoClient
import json


# ##############################################
# MODELO
# ##############################################
class DataBase:
    def __init__(
        self,
    ):
        pass

    def conexion_bd(self, d_val, e_val):
        if e_val == "NR":
            self.client = pymongo.MongoClient("localhost", 27017)
            self.db = self.client[d_val]
            self.collection = self.db["Productos"]
            # self.mi_diccionario = {"producto": "", "precio": "", "cantidad": ""}
            # self.registro = self.collection.insert_one(self.mi_diccionario)
            # print(self.registro)
            print("conexion a BD No relacional")
        elif e_val == "":
            print("ingresar tipo de BD")
        elif e_val == "R":
            self.con = sqlite3.connect(d_val)
            return self.con
            print("pasa bloque conexion BD relacional")
        try:
            cursor = self.con.cursor()
            sql = """CREATE TABLE productos
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    producto varchar(20) NOT NULL,
                    cantidad real,
                    precio real)
            """
            cursor.execute(sql)
            self.con.commit()
        except:
            pass


class Abmc(DataBase):
    def alta(self, a_val, b_val, c_val, tree, d_val, e_val):
        if e_val == "R":
            cadena = a_val
            patron = "^[A-Za-záéíóú]*$"  # regex para el campo cadena
            if re.match(patron, cadena):
                print(a_val, b_val, c_val)
                self.con = sqlite3.connect(d_val)
                cursor = self.con.cursor()
                data = (a_val, b_val, c_val)
                sql = (
                    "INSERT INTO productos(producto, cantidad, precio) VALUES(?, ?, ?)"
                )
                cursor.execute(sql, data)
                self.con.commit()
                print("Estoy en alta todo ok")
                self.actualizar_treeview(tree, d_val, e_val)
            else:
                print("error en campo producto")
        elif e_val == "NR":
            self.client = pymongo.MongoClient("localhost", 27017)
            self.db = self.client[d_val]
            self.collection = self.db["Productos"]
            mi_diccionario = {
                "producto": a_val,
                "precio": b_val,
                "cantidad": c_val,
            }
            self.registro = self.collection.insert_one(mi_diccionario)
            print(mi_diccionario)

    def actualizar_treeview(self, mitreview, d_val, e_val):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)

        if e_val == "R":
            sql = "SELECT * FROM productos ORDER BY id ASC"
            self.con = sqlite3.connect(d_val)
            cursor = self.con.cursor()
            datos = cursor.execute(sql)

            resultado = datos.fetchall()
            for fila in resultado:
                print(fila)
                mitreview.insert(
                    "", 0, text=fila[0], values=(fila[1], fila[2], fila[3])
                )
        elif e_val == "NR":
            self.client = pymongo.MongoClient("localhost", 27017)
            self.db = self.client[d_val]
            self.collection = self.db["Productos"]
            resultado = self.collection.find(
                {"producto": "", "precio": "", "cantidad": ""}
            )
            for x in self.collection.find({}):
                print(x)

    def modifica(
        self,
        producto,
        cantidad,
        precio,
        tree,
        d_val,
    ):
        valor = tree.selection()
        item = tree.item(valor)
        mi_id = item["text"]
        sql = "UPDATE Usuarios SET producto = ?, cantidad = ?, precio = ?, WHERE id = ?"
        data = (
            producto,
            cantidad,
            precio,
            mi_id,
        )
        self.con = sqlite3.connect(d_val)
        cursor = self.con.cursor()
        cursor.execute(sql, data)
        self.con.commit()

    def borrar(self, tree, d_val, e_val, a_val):
        if e_val == "R":
            valor = tree.selection()
            print(valor)
            item = tree.item(valor)
            print(item)
            print(item["text"])
            mi_id = item["text"]

            self.con = sqlite3.connect(d_val)
            cursor = self.con.cursor()
            data = (mi_id,)
            sql = "DELETE FROM productos WHERE id = ?;"
            cursor.execute(sql, data)
            self.con.commit()

            tree.delete(valor)
        elif e_val == "NR":
            self.client = pymongo.MongoClient("localhost", 27017)
            self.db = self.client[d_val]
            self.collection = self.db["Productos"]
            self.collection.delete_one({"producto": (a_val)})
            print("producto eliminado: " + (a_val))
