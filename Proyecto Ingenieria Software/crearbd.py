import sqlite3

conexion = ''

def crear_bd():
    global conexion
    try:
        conexion = sqlite3.connect("gemita.db")
    except:
        print("ya existe")

def tablaproveedor():
    try:
        conexion.execute("""CREATE TABLE proveedor(
        ruc CHAR(13) NOT NULL,
        empresa VARCHAR(45) NOT NULL,
        nombre VARCHAR(45) NOT NULL,
        apellido VARCHAR(45) NOT NULL,
        direccion VARCHAR(45) NOT NULL,
        telefono VARCHAR(10) NOT NULL,
        CONSTRAINT PK_Proveedor PRIMARY KEY(ruc))""")
    except sqlite3.OperationalError:
        return False

def tablacompra():
    try:
        conexion.execute("""CREATE TABLE compra(
        numero INT NOT NULL,
        fecha DATE NOT NULL,
        total double(5,2) NOT NULL,
        id_proveedor CHAR(13) NOT NULL,
        CONSTRAINT PK_Compra PRIMARY KEY(numero),
        CONSTRAINT FK_Proveedor FOREIGN KEY(id_proveedor) REFERENCES proveedor(ruc))""")
    except sqlite3.OperationalError:
        return False

def tablaproducto():
    try:
        conexion.execute("""CREATE TABLE producto(
        id INT NOT NULL,
        nombre VARCHAR(45) NOT NULL,
        stock INT NOT NULL default 0,
        costo double(5,2) NOT NULL,
        pvp double(5,2) NOT NULL default 0,
        CONSTRAINT PK_Producto PRIMARY KEY(id))""")
    except sqlite3.OperationalError:
        return False

def tablapedido():
    try:
        conexion.execute("""CREATE TABLE pedido(
        compra_numero INT NOT NULL,
        producto_id INT NOT NULL,
        cantidad INT NOT NULL,
        costo double(5,2) NOT NULL,
        CONSTRAINT PK_Pedido PRIMARY KEY(compra_numero, producto_id),
        CONSTRAINT FK_Compra FOREIGN KEY(compra_numero) REFERENCES compra(numero),
        CONSTRAINT FK_Producto FOREIGN KEY(producto_id) REFERENCES producto(id))""")
    except sqlite3.OperationalError:
        return False

def tablacliente():
    try:
        conexion.execute("""CREATE TABLE cliente(
        cedula CHAR(10) NOT NULL,
        nombres VARCHAR(45) NOT NULL,
        apellidos VARCHAR(45) NOT NULL,
        telefono VARCHAR(13),
        CONSTRAINT PK_Cliente PRIMARY KEY(cedula))""")
    except sqlite3.OperationalError:
        return False
    
def tablafactura():
    try:
        conexion.execute("""CREATE TABLE factura(
        id INT NOT NULL,
        fecha DATE NOT NULL,
        total double(5,2) NOT NULL,
        id_cliente CHAR(10) NOT NULL,
        CONSTRAINT PK_Factura PRIMARY KEY(id),
        CONSTRAINT FK_Cliente FOREIGN KEY(id_cliente) REFERENCES cliente(cedula))""")
    except sqlite3.OperationalError:
        return False

def tabladetalle():
    try:        
        conexion.execute("""CREATE TABLE detalle(
        producto_id INT NOT NULL,
        factura_id INT NOT NULL,
        cantidad INT NOT NULL,
        pvp double(5,2) NOT NULL,
        CONSTRAINT PK_Detalle PRIMARY KEY(producto_id, factura_id),
        CONSTRAINT FK_Product FOREIGN KEY(producto_id) REFERENCES producto(id),
        CONSTRAINT FK_Factura FOREIGN KEY(factura_id) REFERENCES factura(id))""")
    except sqlite3.OperationalError:
        return False

def tablausuario():
    try:        
        conexion.execute("""CREATE TABLE usuario(
        username VARCHAR NOT NULL,
        contrasena VARCHAR NOT NULL,
        tipo CHAR(13) NOT NULL,
        CONSTRAINT PK_Usuario PRIMARY KEY(username))""")
    except sqlite3.OperationalError:
        return False

def triggerfactura():
    try:
        conexion.execute("""Create trigger nuevafactura after insert On detalle for each row Begin Update factura Set total = total + new.pvp where id=new.factura_id; update producto set stock = stock - new.cantidad where id = new.producto_id; End;""")
    except sqlite3.OperationalError:
        return False

def triggercompra():
    try:
        conexion.execute("""create trigger triggercompra after insert On pedido for each row Begin Update compra Set total = total + new.costo where numero=new.compra_numero; update producto set stock = stock + new.cantidad where id = new.producto_id; End;""")
    except sqlite3.OperationalError:
        return False

def close():
    try:
        conexion.close()
    except:
        print('No se realizó la conexión')


crear_bd()
#tablaproveedor()
#tablacompra()
#tablaproducto()
#tablapedido()
#tablacliente()
#tablafactura()
#tabladetalle()
#tablausuario()
triggerfactura()
triggerproducto()
close()