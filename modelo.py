import sqlite3
import re
import pymongo
from pymongo import MongoClient


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
            # self.conexion_mongo = self.client
            self.client = pymongo.MongoClient("localhost", 27017)
            self.db = self.client[d_val]
            self.collection = self.db["Productos"]
            self.mi_diccionario = {"producto": "", "precio": "", "cantidad": ""}
            self.registro = self.collection.insert_one(self.mi_diccionario)
            print(self.registro)
        elif e_val == "R":
            self.con = sqlite3.connect(d_val)
            return self.con
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


class Abmc(
    DataBase
):  # No estoy seguro si ABMC debia ser una clase hija porque no esta especificado en el enunciado.
    def alta(
        self,
        producto,
        cantidad,
        precio,
        tree,
        d_val,
    ):
        cadena = producto
        patron = "^[A-Za-záéíóú]*$"  # regex para el campo cadena
        if re.match(patron, cadena):
            print(producto, cantidad, precio)
            self.con = sqlite3.connect(d_val)
            cursor = self.con.cursor()
            # con = self.conexion()
            # cursor = con.cursor()
            data = (producto, cantidad, precio)
            sql = "INSERT INTO productos(producto, cantidad, precio) VALUES(?, ?, ?)"
            cursor.execute(sql, data)
            self.con.commit()
            print("Estoy en alta todo ok")
            self.actualizar_treeview(tree, d_val)
        else:
            print("error en campo producto")

    def actualizar_treeview(self, mitreview, d_val):
        records = mitreview.get_children()
        for element in records:
            mitreview.delete(element)

        sql = "SELECT * FROM productos ORDER BY id ASC"
        self.con = sqlite3.connect(d_val)
        cursor = self.con.cursor()
        datos = cursor.execute(sql)

        resultado = datos.fetchall()
        for fila in resultado:
            print(fila)
            mitreview.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))


"""
    def consultar():
        global compra
        print(compra)

def borrar(tree):
    valor = tree.selection()
    print(valor)   #('I005',)
    item = tree.item(valor)
    print(item)    #{'text': 5, 'image': '', 'values': ['daSDasd', '13.0', '2.0'], 'open': 0, 'tags': ''}
    print(item['text'])
    mi_id = item['text']

    con=conexion()
    cursor=con.cursor()
    #mi_id = int(mi_id)
    data = (mi_id,)
    sql = "DELETE FROM productos WHERE id = ?;"
    cursor.execute(sql, data)
    con.commit()
    tree.delete(valor)

"""
