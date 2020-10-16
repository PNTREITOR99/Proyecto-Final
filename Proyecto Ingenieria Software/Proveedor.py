import sqlite3

class proveedor:
    ruc = ''
    empresa = ''
    nombre = ''
    apellido = ''
    direccion = ''
    telefono = ''

    def __init__(self,ruc,empresa,nombre,apellido,direccion,telefono):
        self.ruc = ruc
        self.empresa = empresa
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

    def settelefono(self,telefono):
        self.telefono = telefono

    def setdireccion(self,direccion):
        self.direccion = direccion

    def setnombresapellidos(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def getruc(self):
        return self.ruc

    def getempresa(self):
        return self.empresa

    def getnombre(self):
        return self.nombre

    def getapellido(self):
        return self.apellido

    def getdireccion(self):
        return self.direccion

    def gettelefono(self):
        return self.telefono

    def sql_agregarproveedor(self):
        try:
            conexion = sqlite3.connect('gemita.db')
            conexion.execute("INSERT INTO proveedor (ruc, empresa, nombre, apellido, direccion, telefono)  VALUES(?,?,?,?,?,?)",(self.ruc,self.empresa,self.nombre,self.apellido,self.direccion,self.telefono))
            conexion.commit()
            return True
        except sqlite3.IntegrityError:
            print("Proveedor existente")
            return False
        finally:
            conexion.close()

    def sql_modificarproveedor(self, ruc, empresa, nombre, apellido, direccion, telefono):
        try:
            conexion = sqlite3.connect('gemita.db')
            conexion.execute("UPDATE proveedor SET empresa = ?, nombre = ?,apellido = ?, direccion = ?, telefono = ? WHERE ruc = ?",(empresa, nombre,apellido,direccion,telefono,ruc))
            conexion.commit()
        except sqlite3.IntegrityError:
            print("No existe el proveedor")
        finally:
            conexion.close()

    def buscarproveedor(self,ruc):
        aux = []
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM proveedor WHERE ruc = ?",(ruc,))
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

    def listarprov(self):
        try:
            aux = []
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM proveedor")
            for x in cursor.fetchall():
                aux.append(list(x))
            return aux
        except:
            print('no')
        finally:
            cursor.close()
            conexion.close()