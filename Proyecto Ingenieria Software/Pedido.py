import sqlite3

class pedido:
    idc = 0
    idp = 0
    cantidad = 0
    costo = 0.0

    def __init__(self,idc,idp,cantida,costo):
        self.idc = idc
        self.idp = idp
        self.cantidad = cantida
        self.costo = costo * cantida

    def getidc(self):
        return self.idc

    def getidp(self):
        return self.idp

    def getcantidad(self):
        return self.cantidad

    def getcosto(self):
        return self.costo

    def sql_agregarpedido(self):
        try:
            conexion = sqlite3.connect('gemita.db')
            conexion.execute("INSERT INTO pedido (compra_numero, producto_id, cantidad,costo)  VALUES(?,?,?,?)",(self.idc,self.idp,self.cantidad,self.costo))
            conexion.commit()
        except sqlite3.IntegrityError:
            print("Pedido existente")
        finally:
            conexion.close()

    def buscarpedido(self,compra):
        aux = []
        try:
            #print(compra)
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM pedido WHERE compra_numero = ?",(compra,))
            #print(cursor.fetchall())
            for x in cursor.fetchall():
                aux.append(list(x))
            #print(aux)
            return True
        except:
            #print("no")
            return False
        finally:
            return aux
            cursor.close()
            conexion.close()

    def buscarpedidoproducto(self,id):
        aux = []
        try:
            #print(compra)
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM pedido WHERE producto_id = ?",(id,))
            #print(cursor.fetchall())
            for x in cursor.fetchall():
                aux.append(list(x))
            #print(aux)
            return True
        except:
            #print("no")
            return False
        finally:
            return aux
            cursor.close()
            conexion.close()