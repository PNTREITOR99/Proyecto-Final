import sqlite3

class producto:
    idp = 0
    nombre = ''
    stock = 0
    costo = 0.0
    pvp = 0.0

    def __init__(self,idp,nombre,stock,costo):
        self.idp = idp
        self.nombre = nombre
        self.stock = stock
        self.costo = costo
        self.pvp = round(costo * 1.12,2)

    def setnombre(self,nombre):
        self.nombre = nombre

    def setstock(self,stock):
        self.stock = stock

    def setcosto(self,costo):
        self.costo = costo

    def setpvp(self):
        self.pvp = round(self.costo * 1.12,2)

    def getidp(self):
        return self.idp
    
    def getnombre(self):
        return self.nombre
    
    def getstock(self):
        return self.stock
    
    def getcosto(self):
        return self.costo
    
    def getpvp(self):
        return self.pvp

    def sql_agregarproducto(self):
        try:
            conexion = sqlite3.connect('gemita.db')
            conexion.execute("INSERT INTO producto (id, nombre, stock, costo, pvp)  VALUES(?,?,?,?,?)",(self.idp,self.nombre,self.stock,self.costo,self.pvp))
            conexion.commit()
        except sqlite3.IntegrityError:
            print("Producto existente")
        finally:
            conexion.close()

    def sql_modificarproducto(self, id, nombre, stock, costo):
        try:
            conexion = sqlite3.connect('gemita.db')
            conexion.execute("UPDATE producto SET nombre = ?, stock = ?, costo = ?, pvp = ? where id = ?", (nombre, stock, costo, str(float(costo)*1.12), id))
            conexion.commit()
            print('ya')
        except sqlite3.IntegrityError:
            print("No existe el producto")
        finally:
            conexion.close()

    def buscarproducto(self,id):
        aux = []
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM producto WHERE id = ?",(id,))
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

    def outofstock(self,id):
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT stock FROM producto WHERE id = ?",(id,))
            aux = cursor.fetchall()[0][0]
            if aux < 5:
                return True
            else:
                return False
        except:
            print('no')
        finally:
            cursor.close()
            conexion.close()

    def isonstock(self,id,cant):
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT stock FROM producto WHERE id = ?",(id,))
            aux = cursor.fetchall()[0][0]
            if aux < int(cant):
                return False
            else:
                return True
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conexion.close()
    
    def autoinc(self):
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT max(id) FROM producto")
            aux = cursor.fetchall()[0][0]
            print(type(aux))
            aux += 1
        except:
            print('no')
            aux = 1
        finally:
            return aux
            cursor.close()
            conexion.close()

    def restar(self,id,cant):
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT stock FROM producto WHERE id = ?",(id,))
            aux = cursor.fetchall()[0][0]
            print(aux)
            rest = int(aux) - cant
            conexion.execute("UPDATE producto SET stock = ? where id = ?", (rest, id))
            conexion.commit()
            print('ya')
        except sqlite3.IntegrityError:
            print("No existe el producto")
        finally:
            conexion.close()
    def listarprod(self):
        try:
            aux = []
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM producto")
            for x in cursor.fetchall():
                aux.append(list(x))
            return aux
        except:
            print('no')
        finally:
            cursor.close()
            conexion.close()