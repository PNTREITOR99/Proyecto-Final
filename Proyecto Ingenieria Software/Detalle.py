import sqlite3

class detalle:
    idp = 0
    idf = 0
    cant = 0
    pvp = 0

    def __init__(self, idp, idf, cant):
        self.idp = idp
        self.idf = idf
        self.cant = cant
        #self.pvp = 0.0
        self.setpvp()

    def setpvp(self):
        conexion = sqlite3.connect('gemita.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT pvp FROM producto WHERE id = ?", (self.idp,))
        lala = list(cursor.fetchone())[0]
        cursor.close()
        self.pvp = lala * self.cant

    def getidp(self):
        return self.idp

    def getidf(self):
        return self.idf

    def getcant(self):
        return self.cant

    def getpvp(self):
        return self.pvp

    def sql_agregardetalle(self):
        try:
            conexion = sqlite3.connect('gemita.db')
            conexion.execute("INSERT INTO detalle (producto_id, factura_id, cantidad, pvp)  VALUES(?,?,?,?)",(self.idp,self.idf,self.cant,self.pvp))
            conexion.commit()
        except sqlite3.IntegrityError:
            print("Producto existente")
        finally:
            conexion.close()

    def buscardetalle(self,id):
        aux = []
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM detalle WHERE factura_id = ?",(id,))
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

    def buscardetalleproducto(self,id):
        aux = []
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM detalle WHERE producto_id = ?",(id,))
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
