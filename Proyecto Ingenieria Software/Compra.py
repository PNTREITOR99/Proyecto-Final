import sqlite3

class compra:
    numero = 0
    fecha = ''
    total = 0.0
    idp = ''

    def __init__(self,numero,total,idp):
        self.numero = numero
        self.total = total
        self.idp = idp

    def getnumero(self):
        return self.numero

    def gettotal(self):
        return self.total

    def getidp(self):
        return self.idp

    def sql_agregarcompra(self):
        try:
            conexion = sqlite3.connect('gemita.db')
            conexion.execute("INSERT INTO compra (numero, fecha, total,id_proveedor)  VALUES(?,CURRENT_DATE,?,?)",(self.numero,self.total,self.idp))
            conexion.commit()
        except sqlite3.IntegrityError:
            print("Compra existente")
        finally:
            conexion.close()

    def buscarcompra(self,numero):
        aux = []
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM compra WHERE numero = ?",(numero,))
            for x in cursor.fetchall():
                aux.append(list(x))
            return True
        except:
            #print("no")
            return False
        finally:
            return aux
            cursor.close()
            conexion.close()

    def buscarcompraproveedor(self,id):
        aux = []
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM compra WHERE id_proveedor = ?",(id,))
            for x in cursor.fetchall():
                aux.append(list(x))
            return True
        except:
            #print("no")
            return False
        finally:
            return aux
            cursor.close()
            conexion.close()

    def autoinc(self):
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT max(numero) FROM compra")
            aux = cursor.fetchall()[0][0]
            aux += 1
            return aux
        except:
            print('no')
        finally:
            cursor.close()
            conexion.close()