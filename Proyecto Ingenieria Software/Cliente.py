import sqlite3

class cliente:
    cedula = ''
    nombres = ''
    apellidos = ''
    telefono = ''

    def __init__(self,cedula,nombres,apellidos,telefono):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.telefono = telefono

    def setnombres(self,nombres):
        self.nombres = nombres

    def setapellidos(self,apellidos):
        self.apellidos = apellidos

    def getcedula(self):
        return self.cedula

    def getnombres(self):
        return self.nombres

    def getapellidos(self):
        return self.apellidos

    def gettelefono(self):
        return self.telefono

    def sql_agregarcliente(self):
        try:
            conexion = sqlite3.connect('gemita.db')
            conexion.execute("INSERT INTO cliente (cedula, nombres, apellidos, telefono) VALUES(?,?,?,?)",(self.cedula,self.nombres,self.apellidos,self.telefono))
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.IntegrityError:
            print('Ya existe el cliente')
            conexion.close()
            return False
        #finally:            
        #    conexion.close()
        #    return True

    def sql_modificarcliente(self, cedula, nombres, apellidos, telefono):
        try:
            conexion = sqlite3.connect('gemita.db')
            conexion.execute("UPDATE cliente SET nombres = ?, apellidos = ?, telefono = ? WHERE cedula = ?",(nombres,apellidos,telefono,cedula))
            conexion.commit()
        except Exception as e:
            print(e)        
        #except sqlite3.IntegrityError:
        #    print('No existe el cliente')
        finally:
            conexion.close()

    def listarclientes(self):
        try:
            aux = []
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM cliente")
            for x in cursor.fetchall():
                aux.append(list(x))
            return aux
        except:
            print('no')
        finally:
            cursor.close()
            conexion.close()

    def buscarcliente(self,cedula):
        aux = []
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM cliente WHERE cedula = ?",(cedula,))
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