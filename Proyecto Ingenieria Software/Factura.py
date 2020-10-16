import sqlite3

class factura:
    idf = 0
    total = 0.0
    idcliente = ''

    def __init__(self,idf,total,idcliente):
        self.idf = idf
        self.total = total
        self.idcliente = idcliente

    def getidf(self):
        return self.idf

    def gettotal(self):
        return self.total

    def getidcliente(self):
        return self.idcliente

    def sql_agregarfactura(self):
        try:
            conexion = sqlite3.connect('gemita.db')
            conexion.execute("INSERT INTO factura (id, fecha, total, id_cliente) VALUES(?,CURRENT_DATE,?,?)",(self.idf,self.total,self.idcliente))
            conexion.commit()
        except sqlite3.IntegrityError:
            print('Ya existe la factura')
        finally:
            conexion.close()

    def buscarfactura(self,id):
        aux = []
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM factura WHERE id = ?",(id,))
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

    def buscarfacturacliente(self,id):
        aux = []
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM factura WHERE id_cliente = ?",(id,))
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
            cursor.execute("SELECT max(id) FROM factura")
            aux = cursor.fetchall()[0][0]
            aux += 1
            return aux
        except:
            print('no')
        finally:
            cursor.close()
            conexion.close()

    def detallesmes(self, fechaini, fechafin):
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT producto.nombre, sum(detalle.cantidad), sum(detalle.pvp) FROM detalle JOIN producto ON detalle.producto_id = producto.id INNER JOIN factura ON detalle.factura_id = factura.id WHERE factura.fecha between ? and ? group by producto.id order by sum(detalle.cantidad) ASC",(fechaini,fechafin))
            aux = cursor.fetchall()
            lala = []
            for e in aux:
                lala.append(list(e))
            return lala
        except:
            print('no')
        finally:
            cursor.close()
            conexion.close()

    def pedidosmes(self, fechaini, fechafin):
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT producto.nombre, sum(pedido.cantidad), sum(pedido.costo) FROM pedido JOIN producto ON pedido.producto_id = producto.id INNER JOIN compra ON pedido.compra_numero = compra.numero WHERE compra.fecha in (?,?) group by producto.id order by sum(pedido.cantidad) ASC",(fechaini,fechafin))
            aux = cursor.fetchall()
            lala = []
            for e in aux:
                lala.append(list(e))
            return lala
        except:
            print('no')
        finally:
            cursor.close()
            conexion.close()

    def ganancias(self, fechaini, fechafin):
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT sum(total) FROM factura WHERE fecha between ? and ?",(fechaini,fechafin))
            aux = list(cursor.fetchall())[0][0]
            return aux
        except:
            print('no')
        finally:
            cursor.close()
            conexion.close()

    def perdidas(self, fechaini, fechafin):
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT sum(total) FROM compra WHERE fecha between ? and ?",(fechaini,fechafin))
            aux = list(cursor.fetchall())[0][0]
            return aux
        except:
            print('no')
        finally:
            cursor.close()
            conexion.close()

    #def total_(self,x,y):
    #    total = x - y
    #    return total
