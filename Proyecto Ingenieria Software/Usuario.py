import sqlite3

class usuario:
    username = ''
    password = ''
    tipo = ''

    def __init__(self,username,password,tipo):
        self.username = username
        self.password = password
        self.tipo = tipo

    def setpassword(self,password):
        self.password = password

    def getusername(self):
        return self.username

    def getpassword(self):
        return self.password

    def gettipo(self):
        return self.tipo

    def sql_agregarusuario(self):
        try:
            conexion = sqlite3.connect('gemita.db')
            conexion.execute("INSERT INTO usuario (username, contrasena, tipo)  VALUES(?,?,?)",(self.username,self.password,self.tipo))
            conexion.commit()
            conexion.close()
            return True
        except sqlite3.IntegrityError:
            print("Usuario existente")
            conexion.close()
            return False
        
    def sql_modificarusuariro(self, usuario, contrasena, tipo):
        try:
            conexion = sqlite3.connect('gemita.db')
            conexion.execute("UPDATE usuario SET contrasena = ?, tipo = ? WHERE username = ?",(contrasena, tipo, usuario))
            conexion.commit()
        except sqlite3.IntegrityError:
            print("No existe usuario")
        finally:
            conexion.close()

    def buscarusuario(self,user):
        aux = []
        try:
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuario WHERE username = ?",(user,))
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

    def listarusers(self):
        try:
            aux = []
            conexion = sqlite3.connect('gemita.db')
            cursor = conexion.cursor()
            cursor.execute("SELECT username, tipo FROM usuario")
            for x in cursor.fetchall():
                aux.append(list(x))
            return aux
        except:
            print('no')
        finally:
            cursor.close()
            conexion.close()