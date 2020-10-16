from crearbd import *
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
import datetime
from tkcalendar import *
from Proveedor import *
from Producto import *
from Factura import *
from Detalle import *
from Cliente import *
from Producto import *
from Usuario import *
from Compra import *
from Pedido import *
import pandas as pd
from tabulate import tabulate
import csv
crearbd.crear_bd()
crearbd.tablaproveedor()
crearbd.tablacompra()
crearbd.tablaproducto()
crearbd.tablapedido()
crearbd.tablacliente()
crearbd.tablafactura()
crearbd.tabladetalle()
crearbd.tablausuario()
crearbd.triggerfactura()
crearbd.triggerproducto()
crearbd.close()

Pass_ = 1
Products = []
ProductsC = []

def GenerarR():
    Rep = tk.Toplevel(root)
    Rep.geometry("575x350")
    Rep.resizable(0, 0)
    Rep.title("Generar Reporte")
    Rep.focus_set()
    Rep.grab_set()

    Fi_ = Label(Rep, text = "Fecha inicial:")
    Fi_.place(x = 20, y = 20)
    Cali = Calendar(Rep, selectmode = "day", year = 2020, month = 10, day = 9, maxdate = datetime.date.today(), mindate = datetime.datetime(2019, 1, 1), date_pattern = 'y-mm-dd' )
    Cali.place(x = 20, y = 50)

    Ff_ = Label(Rep, text = "Fecha final:")
    Ff_.place(x = 300, y = 20)
    Calf = Calendar(Rep, selectmode = "day", year = 2020, month = 10, day = 9, maxdate = datetime.date.today(), mindate = datetime.datetime(2019, 1, 1), date_pattern = 'y-mm-dd' )
    Calf.place(x = 300, y = 50)   

    Button(Rep, text = "Generar Reporte", command = lambda: getDate(Cali, Calf, Rep)).place(x = 240, y = 275)

    Rep.wait_window(Rep)

def getDate(Cali, Calf, Rep):
        archivo = filedialog.askdirectory(title = "Guardar Reporte")
        if(archivo == ""):
            messagebox.showerror(message = "Debe de ingresar una direccion!!!", title = "Error")
            return
        R = factura.detallesmes(factura, Cali.get_date(), Calf.get_date())
        Tablita = tabulate(R, headers = ["Nombre", "Cantidad", "Total"], tablefmt='fancy_grid')
        ds = pd.DataFrame(["****  Reporte  ****", " ",
        "Fecha inicial: " + Cali.get_date(), "Fecha final: " + Calf.get_date(),
        " ", "Total de venta: " + str(round(float(factura.ganancias(factura, Cali.get_date(), Calf.get_date())),2)),
        "Total de compra: " +  str(round(float(factura.perdidas(factura,Cali.get_date(), Calf.get_date())),2)), " ",
        "Ganancias: " + str(round(float(factura.ganancias(factura, Cali.get_date(), Calf.get_date())) - float(factura.perdidas(factura,Cali.get_date(), Calf.get_date())), 2)),
        " ","Productos vendidos: ",Tablita])
        ds.to_csv(archivo + '/Reporte desde ' + Cali.get_date() + ' a ' + Calf.get_date() +'.txt', header=None, index=False, sep="\t", quoting=csv.QUOTE_NONE, quotechar="",  escapechar="_")
        Rep.destroy()

def M_Factura():
    if (IdF.get() == ""):
        messagebox.showerror(message = "Debe igresar la ID de la Factura!!!", title = "Error")
        return        

    DatF = factura.buscarfactura(factura, IdF.get())
    if (len(DatF) == 0):
        messagebox.showerror(message = "El ID ingresado no existe!!!", title = "Error")
        return        

    DatC = cliente.buscarcliente(cliente, DatF[0][3])
    DetF = detalle.buscardetalle(detalle, IdF.get()) 

    Fact = tk.Toplevel(root)
    Fact.geometry("400x500")
    Fact.resizable(0, 0)
    Fact.title("Factura")
    Fact.focus_set()
    Fact.grab_set()

    IDF_ = Label(Fact, text = "ID Factura:")
    IDF_.place(x = 10, y = 20)
    IDF = Entry(Fact, width = 17)
    IDF.place(x = 10, y = 40)

    CF_ = Label(Fact, text = "Cedula:")
    CF_.place(x = 10, y = 70)
    CF = Entry(Fact, width = 17)
    CF.place(x = 10, y = 90)

    NomF_ = Label(Fact, text = "Nombre:")
    NomF_.place(x = 140, y = 70)
    NomF = Entry(Fact, width = 17)
    NomF.place(x = 140, y = 90)

    ApeF_ = Label(Fact, text = "Apellido:")
    ApeF_.place(x = 280, y = 70)
    ApeF = Entry(Fact, width = 17)
    ApeF.place(x = 280, y = 90)

    TelF_ = Label(Fact, text = "Telefono:")
    TelF_.place(x = 10, y = 120)
    TelF = Entry(Fact, width = 17)
    TelF.place(x = 10, y = 140)

    FechF_ = Label(Fact, text = "Fecha:")
    FechF_.place(x = 140, y = 120)
    FechF = Entry(Fact, width = 17)
    FechF.place(x = 140, y = 140)

    TotF_ = Label(Fact, text = "Total:")
    TotF_.place(x = 280, y = 120)
    TotF = Entry(Fact, width = 17)
    TotF.place(x = 280, y = 140)

    IDF.insert(0, DatF[0][0])
    IDF.config(state = 'readonly')

    CF.insert(0, DatC[0][0])
    CF.config(state = 'readonly')

    NomF.insert(0, DatC[0][1])
    NomF.config(state = 'readonly')

    ApeF.insert(0, DatC[0][2])
    ApeF.config(state = 'readonly')

    TelF.insert(0, DatC[0][3])
    TelF.config(state = 'readonly')

    FechF.insert(0, DatF[0][1])
    FechF.config(state = 'readonly')

    TotF.insert(0, DatF[0][2])
    TotF.config(state = 'readonly')

    TabF = Table(Fact, title="", headers=["Cant", "Nombre", "P.U", "Total"], height = 13)
    TabF.place(x = 20, y = 160, width = 370)

    for row in DetF:
        print(row[2])
        print(row[3])
        #print(row[2] + "+" + row[3] + "= " + str(float(row[0]) * float(row[3])))
        TabF.add_row([row[2], (producto.buscarproducto(producto, row[0]))[0][1], row[3], str(round(float(row[2]) * float(row[3]), 2))])

    Fact.wait_window(Fact)

def B_P(Ruc, Emp, Nom, Ape, Dir, Tel):
    if (Ruc.get() == ""):
        messagebox.showerror(message = "Debe igresar el RUC del Proveedor!!!", title = "Error")
        return   
    P = proveedor.buscarproveedor(proveedor, Ruc.get())
    if(len(P) == 0):
        messagebox.showerror(message = "El Proveedor ingresado no existe!!!", title = "Error")
        return  
    Ruc.config(state = 'readonly')

    Emp.config(state = 'normal')
    Emp.delete(0, tk.END)
    Emp.insert(0, P[0][1])    

    Nom.config(state = 'normal')
    Nom.delete(0, tk.END)
    Nom.insert(0, P[0][2])    

    Ape.config(state = 'normal')
    Ape.delete(0, tk.END)
    Ape.insert(0, P[0][3])
    
    Dir.config(state = 'normal')
    Dir.delete(0, tk.END)
    Dir.insert(0, P[0][4])
    
    Tel.config(state = 'normal')
    Tel.delete(0, tk.END)
    Tel.insert(0, P[0][5])

def B_Pr(v1, v2, v3, v4):
    if (v1.get() == ""):
        messagebox.showerror(message = "Debe igresar el ID del Producto!!!", title = "Error")
        return   
    P = producto.buscarproducto(producto, v1.get())
    print(P)
    if(len(P) == 0):
        messagebox.showerror(message = "El Producto ingresado no existe!!!", title = "Error")
        return  
    v1.config(state = 'readonly')

    v2.config(state = 'normal')
    v2.delete(0, tk.END)
    v2.insert(0, P[0][1])    

    v3.config(state = 'normal')
    v3.delete(0, tk.END)
    v3.insert(0, P[0][2])    

    v4.config(state = 'normal')
    v4.delete(0, tk.END)
    v4.insert(0, P[0][3])

def B_C(v1, v2, v3, v4):
    if (v1.get() == ""):
        messagebox.showerror(message = "Debe igresar el CI del Cliente!!!", title = "Error")
        return   
    P = cliente.buscarcliente(cliente, v1.get())
    print(P)
    if(len(P) == 0):
        messagebox.showerror(message = "El Cliente no existe!!!", title = "Error")
        return  
    v1.config(state = 'readonly')

    v2.config(state = 'normal')
    v2.delete(0, tk.END)
    v2.insert(0, P[0][1])    

    v3.config(state = 'normal')
    v3.delete(0, tk.END)
    v3.insert(0, P[0][2])    

    v4.config(state = 'normal')
    v4.delete(0, tk.END)
    v4.insert(0, P[0][3])

def B_U(v1, v2, v3):
    if (v1.get() == ""):
        messagebox.showerror(message = "Debe igresar el Nombre de Usuario!!!", title = "Error")
        return   
    P = usuario.buscarusuario(usuario, v1.get())
    print(P)
    if(len(P) == 0):
        messagebox.showerror(message = "El Usuario no existe!!!", title = "Error")
        return  
    v1.config(state = 'readonly')

    v2.config(state = 'normal')
    v2.delete(0, tk.END)
    v2.insert(0, str(P[1]))    

    v3.config(state = 'readonly')
    if (P[2] == 'Administrador'):
        v3.current(0)
    else:
        v3.current(1)

def M_P(Ruc, Emp, Nom, Ape, Dir, Tel, MP):
    if Emp.get() == "" or Nom.get() == "" or Ape.get() == "" or Dir.get() == "" or Tel.get() == "":
        messagebox.showerror(message = "Debe llenar todos los campos!!!", title = "Error")
        return 
    proveedor.sql_modificarproveedor(proveedor, Ruc.get(), Emp.get(), Nom.get(), Ape.get(), Dir.get(), Tel.get())
    messagebox.showinfo(message="El Proveedor se ha actualizado con exito!!!", title="Actualizar")
    Lista = proveedor.listarprov(proveedor)
    TablaPrv.clean_rows()
    for row in Lista:
        TablaPrv.add_row(row)
    MP.destroy()

def M_Pr(v1, v2, v3, v4, MP):
    if v2.get() == "" or v3.get() == "" or v4.get() == "":
        messagebox.showerror(message = "Debe llenar todos los campos!!!", title = "Error")
        return 
    producto.sql_modificarproducto(producto, v1.get(), v2.get(), v3.get(), v4.get())
    messagebox.showinfo(message="El Producto se ha actualizado con exito!!!", title="Actualizar")
    Lista = producto.listarprod(producto)
    TablaPr.clean_rows()
    for row in Lista:
        TablaPr.add_row(row)
    MP.destroy()    

def M_C(v1, v2, v3, v4, MP):
    if v2.get() == "" or v3.get() == "" or v4.get() == "":
        messagebox.showerror(message = "Debe llenar todos los campos!!!", title = "Error")
        return 
    cliente.sql_modificarcliente(cliente, v1.get(), v2.get(), v3.get(), v4.get())
    messagebox.showinfo(message="El Cliente se ha actualizado con exito!!!", title="Actualizar")
    Lista = cliente.listarclientes(cliente)
    TablaC.clean_rows()
    for row in Lista:
        TablaC.add_row(row)
    MP.destroy()   

def M_U(v1, v2, v3, MP):
    if v2.get() == "" or v3.get() == "" :
        messagebox.showerror(message = "Debe llenar todos los campos!!!", title = "Error")
        return 
    usuario.sql_modificarusuariro(usuario, v1.get(), v2.get(), v3.get())
    messagebox.showinfo(message="El Usuario se ha actualizado con exito!!!", title="Actualizar")
    Lista = usuario.listarusers(usuario)
    TablaU.clean_rows()
    for row in Lista:
        TablaU.add_row(row)
    MP.destroy() 

def M_Proveedor():
    MP = tk.Toplevel(root)
    MP.geometry("400x170")
    MP.resizable(0, 0)
    MP.title("Editar Proveedor")
    MP.focus_set()
    MP.grab_set()

    RuP_ = Label(MP, text = "RUC:")
    RuP_.place(x = 10, y = 20)
    RuP = Entry(MP, width = 15,  validate='all',validatecommand=(validation, '%S'))
    RuP.place(x = 10, y = 40)

    EmpP_ = Label(MP, text = "Empresa:")
    EmpP_.place(x = 140, y = 20)
    EmpP = Entry(MP, width = 15) # Entry- Empresa del Proveedor
    EmpP.place(x = 140, y = 40)
    EmpP.config(state = 'readonly')

    NomP_ = Label(MP, text = "Nombre:")
    NomP_.place(x = 10, y=70)
    NomP = Entry(MP, width = 15) # Entry- Nombre del Proveedor
    NomP.place(x=10, y=90)
    NomP.config(state = 'readonly')

    ApeP_ = Label(MP, text = "Apellido:")
    ApeP_.place(x = 140, y=70)
    ApeP = Entry(MP, width = 15) # Entry- Apellido del Proveedor
    ApeP.place(x=140, y=90)
    ApeP.config(state = 'readonly')

    DirP_ = Label(MP, text = "Direccion:")
    DirP_.place(x = 280, y = 20)
    DirP = Entry(MP, width = 15) # Entry- Direccion del Proveedor
    DirP.place(x = 280, y = 40)
    DirP.config(state = 'readonly')

    TelP_ = Label(MP, text = "Telefono:")
    TelP_.place(x = 280, y = 70)
    TelP = Entry(MP, width = 15, validate='all',validatecommand=(validation, '%S')) # Entry- Telefono del Proveedor
    TelP.place(x = 280, y = 90)
    TelP.config(state = 'readonly')

    Button(MP, text = "Buscar", command = lambda: B_P(RuP, EmpP, NomP, ApeP, DirP, TelP)).place(x = 10, y = 130)
    Button(MP, text = "Guardar", command = lambda: M_P(RuP, EmpP, NomP, ApeP, DirP, TelP, MP)).place(x = 90, y = 130)

    MP.wait_window(MP)

def M_Producto():
    MP = tk.Toplevel(root)
    MP.geometry("400x170")
    MP.resizable(0, 0)
    MP.title("Editar Producto")
    MP.focus_set()
    MP.grab_set()

    IDP_ = Label(MP, text = "ID:")
    IDP_.place(x = 10, y = 20)
    IDP = Entry(MP, width = 15,  validate='all',validatecommand=(validation, '%S'))
    IDP.place(x = 10, y = 40)

    StoP_ = Label(MP, text = "Stock:")
    StoP_.place(x = 140, y = 70)
    StoP = Entry(MP, width = 15, validate='all',validatecommand=(validation, '%S')) 
    StoP.place(x = 140, y = 90)
    StoP.config(state = 'readonly')

    NomP_ = Label(MP, text = "Nombre:")
    NomP_.place(x = 10, y=70)
    NomP = Entry(MP, width = 15)
    NomP.place(x=10, y=90)
    NomP.config(state = 'readonly')

    CosP_ = Label(MP, text = "Costo:")
    CosP_.place(x = 280, y=70)
    CosP = Entry(MP, width = 15, validate='all',validatecommand=(Vdecimal, '%P'))
    CosP.place(x=280, y=90)
    CosP.config(state = 'readonly')

    Button(MP, text = "Buscar", command = lambda: B_Pr(IDP, NomP, StoP, CosP)).place(x = 10, y = 130)
    Button(MP, text = "Guardar", command = lambda: M_Pr(IDP, NomP, StoP, CosP, MP)).place(x = 90, y = 130)
    MP.wait_window(MP)

def M_Cliente():
    MC = tk.Toplevel(root)
    MC.geometry("400x170")
    MC.resizable(0, 0)
    MC.title("Editar Cliente")
    MC.focus_set()
    MC.grab_set()

    CeC_ = Label(MC, text = "Cedula:")
    CeC_.place(x = 10, y = 20)
    CeC = Entry(MC, width = 15, validate='all',validatecommand=(validation, '%S'))
    CeC.place(x = 10, y = 40)

    NoC_ = Label(MC, text = "Nombre:")
    NoC_.place(x = 140, y = 70)
    NoC = Entry(MC, width = 15) 
    NoC.place(x = 140, y = 90)
    NoC.config(state = 'readonly')

    ApC_ = Label(MC, text = "Apellido:")
    ApC_.place(x = 10, y=70)
    ApC = Entry(MC, width = 15)
    ApC.place(x=10, y=90)
    ApC.config(state = 'readonly')

    TeC_ = Label(MC, text = "Telefono:")
    TeC_.place(x = 280, y=70)
    TeC = Entry(MC, width = 15, validate='all',validatecommand=(Vdecimal, '%P'))
    TeC.place(x=280, y=90)
    TeC.config(state = 'readonly')

    Button(MC, text = "Buscar", command = lambda: B_C(CeC, NoC, ApC, TeC)).place(x = 10, y = 130)
    Button(MC, text = "Guardar", command = lambda: M_C(CeC, NoC, ApC, TeC, MC)).place(x = 90, y = 130)
    MC.wait_window(MC)

def M_Usuario():
    MU = tk.Toplevel(root)
    MU.geometry("400x90")
    MU.resizable(0, 0)
    MU.title("Editar Usuario")
    MU.focus_set()
    MU.grab_set()

    UsU_ = Label(MU, text = "Usuario:")
    UsU_.place(x = 10, y = 10)
    UsU = Entry(MU, width = 15) 
    UsU.place(x = 10, y = 31)

    CoU_ = Label(MU, text = "Contraseña:")
    CoU_.place(x = 140, y=10)
    CoU = Entry(MU, width = 15)
    CoU.place(x=140, y=31)
    CoU.config(state = 'readonly')

    TiU_ = Label(MU, text = "Telefono:")
    TiU_.place(x = 280, y=10)
    TiU = ttk.Combobox(MU, state="readonly")
    TiU["values"] = ["Administrador", "Empleado"]
    TiU.place(x = 280, y = 31, width = 100, height = 19)

    Button(MU, text = "Buscar", command = lambda: B_U(UsU, CoU, TiU)).place(x = 10, y = 60)
    Button(MU, text = "Guardar", command = lambda: M_U(UsU, CoU, TiU, MU)).place(x = 90, y = 60)
    MU.wait_window(MU)

def only_numbers(char):
    return char.isdigit()

def only_decimal(P):
    if not P:
        return True
    if "." in P and len(P.split(".")[-1]) > 2:
        return False
    try:
        float(P)
    except ValueError:
        return False
    return True

def L_Proveedor():    
    RUCP.delete(0, tk.END)
    EmpresaP.delete(0, tk.END)
    NombreP.delete(0, tk.END)
    ApellidoP.delete(0, tk.END)
    DireccionP.delete(0, tk.END)
    TelefonoP.delete(0, tk.END)

def L_Producto():
    IdPr.delete(0, tk.END)
    NombrePr.delete(0, tk.END)
    GastoPr.delete(0, tk.END)

def L_Cliente():
    CedC.delete(0, tk.END)
    NomC.delete(0, tk.END)
    ApeC.delete(0, tk.END)
    TelC.delete(0, tk.END)

def L_Usuario():
    UwU.delete(0, tk.END)
    ConU.delete(0, tk.END)
    TipU.set("")
   

def B_FCliente():
    if(IdCF.get() == ""):
        messagebox.showerror(message = "Debe igresar la ID del Cliente!!!", title = "Error")
        return
    Fac = factura.buscarfacturacliente(factura, IdCF.get())
    TablaF.clean_rows()
    if(len(Fac) == 0):
        messagebox.showerror(message = "El Cliente no ha comprado o no existe", title = "Error")
        return
    print(Fac)
    for row in Fac:
        TablaF.add_row([row[0], row[1], row[2]])

def G_Proveedor():
    if (RUCP.get() == "" or EmpresaP.get() == "" or NombreP.get() == "" or ApellidoP.get() == "" or DireccionP.get() == "" or TelefonoP.get() == ""):
        messagebox.showerror(message = "Debe llenar todos los campos!!!", title = "Error")
        return
    Prove = proveedor(RUCP.get(), EmpresaP.get(), NombreP.get(), ApellidoP.get(), DireccionP.get(), TelefonoP.get())
    if Prove.sql_agregarproveedor() == False:
        messagebox.showerror(message = "El Proveedor ya existe!!!", title = "Error")
        return
    Lista = Prove.listarprov()
    TablaPrv.clean_rows()
    for row in Lista:
        TablaPrv.add_row(row)
    L_Proveedor()
    messagebox.showinfo(message = "Se ha registrado el Proveedor con exito!!!", title = "Exito")

def G_Producto():
    if (NombrePr.get() == "" or GastoPr.get() == ""):
        messagebox.showerror(message = "Debe llenar todos los campos!!!", title = "Error")
        return
    Produc = producto(producto.autoinc(producto), NombrePr.get(),0, float(GastoPr.get()))
    Produc.sql_agregarproducto()
    Lista = Produc.listarprod()
    TablaPr.clean_rows()
    for row in Lista:
        TablaPr.add_row(row)
    messagebox.showinfo(message = "Se ha registrado el Producto con exito!!!", title = "Exito")
    IdPr.config(state = "normal")
    L_Producto()    
    IdPr.insert(0, str(producto.autoinc(producto)))
    IdPr.config(state = "readonly")

def G_Cliente():
    if (CedC.get() == "" or NomC.get() == "" or ApeC.get() == "" or TelC.get() == ""):
        messagebox.showerror(message = "Debe llenar todos los campos!!!", title = "Error")
        return
    Cli = cliente(CedC.get(), NomC.get(), ApeC.get(), TelC.get())
    if (Cli.sql_agregarcliente() == False):
        messagebox.showerror(message = "El Cliente ya existe!!!", title = "Error")
        return
    Lista = Cli.listarclientes()
    TablaC.clean_rows()
    for row in Lista:
        TablaC.add_row(row)
    messagebox.showinfo(message = "Se ha registrado el Cliente con exito!!!", title = "Exito")
    L_Cliente()

def G_Usuario():
    if (UwU.get() == "" or ConU.get() == "" or TipU.get() == ""):
        messagebox.showerror(message = "Debe llenar todos los campos!!!", title = "Error")
        return
    Us = usuario(UwU.get(), ConU.get(), TipU.get())
    if (Us.sql_agregarusuario() == False):
        messagebox.showerror(message = "El Cliente ya existe!!!", title = "Error")
        return    
    Lista = Us.listarusers()
    TablaU.clean_rows()
    for row in Lista:
        TablaU.add_row(row)     
    messagebox.showinfo(message = "Se ha registrado el Usuario con exito!!!", title = "Exito")
    L_Usuario()

def BuscarC():
    if(CIC.get() == ""):
        messagebox.showerror(message = "Debe ingresar la CI del Cliente!!!", title = "Error")
        return
    D = cliente.buscarcliente(cliente, CIC.get())
    if (len(D) == 0):
        messagebox.showerror(message = "El Cliente no ha sido registrado!!!\nRegistrelo en la pestaña \"Clientes\".", title = "Error")
        CIC.delete(0, tk.END)
        return
    NombreC.config(state = 'normal')
    NombreC.delete(0, tk.END)
    NombreC.insert(0, D[0][1])
    NombreC.config(state = 'readonly')

    ApellidosC.config(state = 'normal')
    ApellidosC.delete(0, tk.END)
    ApellidosC.insert(0, D[0][2])
    ApellidosC.config(state = 'readonly')

    TelefonoC.config(state = 'normal')
    TelefonoC.delete(0, tk.END)
    TelefonoC.insert(0, D[0][3])
    TelefonoC.config(state = 'readonly')

def BuscarP():
    if(Ruc.get() == ""):
        messagebox.showerror(message = "Debe ingresar el RUC del Proveedor!!!", title = "Error")
        return
    D = proveedor.buscarproveedor(proveedor, Ruc.get())
    if (len(D) == 0):
        messagebox.showerror(message = "El Proveedor no ha sido registrado!!!\nRegistrelo en la pestaña \"Proveedores\".", title = "Error")
        Ruc.delete(0, tk.END)
        return
    NomP.config(state = 'normal')
    NomP.delete(0, tk.END)
    NomP.insert(0, D[0][2])
    NomP.config(state = 'readonly')

    ApeP.config(state = 'normal')
    ApeP.delete(0, tk.END)
    ApeP.insert(0, D[0][3])
    ApeP.config(state = 'readonly')

    TelP.config(state = 'normal')
    TelP.delete(0, tk.END)
    TelP.insert(0, D[0][5])
    TelP.config(state = 'readonly')
    
    EmpP.config(state = 'normal')
    EmpP.delete(0, tk.END)
    EmpP.insert(0, D[0][1])
    EmpP.config(state = 'readonly')

    DirP.config(state = 'normal')
    DirP.delete(0, tk.END)
    DirP.insert(0, D[0][4])
    DirP.config(state = 'readonly')

def FinalizarC():
    if CIC.get() == "":
        messagebox.showerror(message = "Debe ingresar la CI del Cliente")
        return
    D = cliente.buscarcliente(cliente, CIC.get())
    if (len(D) == 0):
        messagebox.showerror(message = "El Cliente no ha sido registrado!!!\nRegistrelo en la pestaña \"Clientes\".", title = "Error")
        CIC.delete(0, tk.END)
        return
    if (len(Products) == 0):
        messagebox.showerror(message = "No existen productos registrados!!!", title = "Error")
        return
    id = factura.autoinc(factura)
    print("ID:" + str(id))
    F = factura(id, 0, CIC.get())
    F.sql_agregarfactura()
    P = ""
    for i in Products:
        D = detalle(i[0], id, int(i[1]))        
        D.sql_agregardetalle()
        D.setpvp()
        if producto.outofstock(producto, i[0]) == True:
            P = P + "\n-> " +str(producto.buscarproducto(producto, i[0])[0][1])
    if P != "":
        messagebox.showwarning(message = "Los siguientes productos estan por agotar su stock:" + P, title = "Alerta de Stock")
    messagebox.showinfo(message = "Factura almacenada con exito!!", title = "GG")
    LimpiarFact()
    Lista = producto.listarprod(producto)
    TablaPr.clean_rows()
    for row in Lista:
        TablaPr.add_row(row)


def FinalizarC_():
    if Ruc.get() == "":
        messagebox.showerror(message = "Debe ingresar el Ruc del Proveedor")
        return
    D = proveedor.buscarproveedor(proveedor, Ruc.get())
    if (len(D) == 0):
        messagebox.showerror(message = "El Proveedor no ha sido registrado!!!\nRegistrelo en la pestaña \"Proveedores\".", title = "Error")
        Ruc.delete(0, tk.END)
        return
    if (len(ProductsC) == 0):
        messagebox.showerror(message = "No existen productos registrados!!!", title = "Error")
        return
    id = compra.autoinc(compra)
    F = compra(id, 0, Ruc.get())
    F.sql_agregarcompra()
    for i in ProductsC:
        D = pedido(id, i[0], int(i[1]), producto.buscarproducto(producto, i[0])[0][3])
        D.sql_agregarpedido()
    messagebox.showinfo(message = "Compra almacenada con exito!!", title = "Exito")
    LimpiarFact_()
    Lista = producto.listarprod(producto)
    TablaPr.clean_rows()
    for row in Lista:
        TablaPr.add_row(row)

def LimpiarF():
    if messagebox.askyesno(message="¿Seguro que desea limpiar la factura?", title="Limpiar") == False:
        return
    LimpiarFact()

def LimpiarFact():    
    global Products
    Products = []

    SubT.config(state = 'normal')
    SubT.delete(0, tk.END)
    SubT.insert(0, "0.0")
    SubT.config(state = 'readonly')

    Iva.config(state = 'normal')
    Iva.delete(0, tk.END)
    Iva.insert(0, "0.0")
    Iva.config(state = 'readonly')

    Total.config(state = 'normal')
    Total.delete(0, tk.END)
    Total.insert(0, "0.0")
    Total.config(state = 'readonly')

    CIC.delete(0, tk.END)
    Id.delete(0, tk.END)
    Cant.delete(0, tk.END)

    NombreC.config(state = 'normal')
    NombreC.delete(0, tk.END)
    NombreC.config(state = 'readonly')

    ApellidosC.config(state = 'normal')
    ApellidosC.delete(0, tk.END)
    ApellidosC.config(state = 'readonly')

    TelefonoC.config(state = 'normal')
    TelefonoC.delete(0, tk.END)
    TelefonoC.config(state = 'readonly')

    TablaP.clean_rows()

def LimpiarF_():
    if messagebox.askyesno(message="¿Seguro que desea limpiar la factura?", title="Limpiar") == False:
        return
    LimpiarFact_()

def LimpiarFact_():    
    global Products
    ProductsC = []

    SubTP.config(state = 'normal')
    SubTP.delete(0, tk.END)
    SubTP.insert(0, "0.0")
    SubTP.config(state = 'readonly')

    IvaP.config(state = 'normal')
    IvaP.delete(0, tk.END)
    IvaP.insert(0, "0.0")
    IvaP.config(state = 'readonly')

    TotalP.config(state = 'normal')
    TotalP.delete(0, tk.END)
    TotalP.insert(0, "0.0")
    TotalP.config(state = 'readonly')

    Ruc.delete(0, tk.END)
    IdP.delete(0, tk.END)
    CantP.delete(0, tk.END)

    EmpP.config(state = 'normal')
    EmpP.delete(0, tk.END)
    EmpP.config(state = 'readonly')

    NomP.config(state = 'normal')
    NomP.delete(0, tk.END)
    NomP.config(state = 'readonly')

    ApeP.config(state = 'normal')
    ApeP.delete(0, tk.END)
    ApeP.config(state = 'readonly')

    TelP.config(state = 'normal')
    TelP.delete(0, tk.END)
    TelP.config(state = 'readonly')

    DirP.config(state = 'normal')
    DirP.delete(0, tk.END)
    DirP.config(state = 'readonly')

    TablaPC.clean_rows()

def EliminarP():
    Dats = TablaP.get_select()    
    try:
        Res = float(Dats[2]) * float(Dats[3])
    except IndexError:
        messagebox.showerror(message = "Debe seleccionar un registro!!!", title = "Error")
        return

    for i in Products:
        print(str(i[0]) + " <-> " + str(Dats[0]))
        if str(i[0]) == str(Dats[0]):            
            Products.pop(Products.index(i))
            break
    
    print(Products)
    SubT.config(state = 'normal')
    aux = float(SubT.get())
    SubT.delete(0, tk.END)
    SubT.insert(0, str(round((aux - Res), 2)))
    aux = float(SubT.get())
    SubT.config(state = 'readonly')

    Iva.config(state = 'normal')
    Iva.delete(0, tk.END)
    Iva.insert(0, str(round((aux * 0.12), 2)))
    Iva.config(state = 'readonly')

    Total.config(state = 'normal')
    aux = float(SubT.get())
    Total.delete(0, tk.END)
    Total.insert(0, str(round((aux * 1.12), 2)))
    Total.config(state = 'readonly')

    TablaP.delete()

def EliminarP_():
    Dats = TablaPC.get_select()    
    try:
        Res = float(Dats[2]) * float(Dats[3])
    except IndexError:
        messagebox.showerror(message = "Debe seleccionar un registro!!!", title = "Error")
        return

    for i in Products:
        print(str(i[0]) + " <-> " + str(Dats[0]))
        if str(i[0]) == str(Dats[0]):            
            ProductsC.pop(ProductsC.index(i))
            break
    
    print(ProductsC)
    SubTP.config(state = 'normal')
    aux = float(SubT.get())
    SubTP.delete(0, tk.END)
    SubTP.insert(0, str(round((aux - Res), 2)))
    aux = float(SubTP.get())
    SubTP.config(state = 'readonly')

    IvaP.config(state = 'normal')
    IvaP.delete(0, tk.END)
    IvaP.insert(0, str(round((aux * 0.12), 2)))
    IvaP.config(state = 'readonly')

    TotalP.config(state = 'normal')
    #aux = float(SubTP.get())
    TotalP.delete(0, tk.END)
    TotalP.insert(0, str(round((aux * 1.12), 2)))
    TotalP.config(state = 'readonly')

    TablaPC.delete()

def IngresarP():
    if (Id.get() == "" or Cant.get() == ""):
        messagebox.showerror(message = "Debe ingresar la ID y la Cantidad del Producto!!!", title = "Error")
        return
    Produc = producto.buscarproducto(producto, Id.get())
    if(len(Produc) == 0):
        messagebox.showerror(message = "El Producto no existe!!!", title = "Error")
        return
    if(producto.isonstock(producto, Id.get(), Cant.get()) == False):
        messagebox.showerror(message = "La cantidad ingresada excede el stock del producto!!!", title = "Error")
        return
    if(int(Cant.get()) == 0 or int(Cant.get()) < 0):
        messagebox.showwarning(message = "Ingrese una cantidad valida!!!", title = "Stock")
        return    
    for i in Products:
        if i[0] == Id.get():
            messagebox.showwarning(message = "Producto ya ingresado!!!", title = "Stock")
            return  

    TablaP.add_row([Produc[0][0], Produc[0][1], Cant.get(), Produc[0][4], round(float(Cant.get()) * float(Produc[0][4]), 2)])
    Products.append([Id.get(), Cant.get()])
    print(Products)
    Sb = float(SubT.get()) + (float(Cant.get()) * float(Produc[0][4]))
    SubT.config(state = 'normal')
    SubT.delete(0, tk.END)
    SubT.insert(0, str(round(Sb, 2)))
    SubT.config(state = 'readonly')

    Iva.config(state = 'normal')
    Iva.delete(0, tk.END)
    Iva.insert(0, str(round((Sb * 0.12), 2)))
    Iva.config(state = 'readonly')

    Total.config(state = 'normal')
    Total.delete(0, tk.END)
    Total.insert(0, str(round((Sb * 1.12), 2)))
    Total.config(state = 'readonly')

    Id.delete(0, tk.END)
    Cant.delete(0, tk.END)


def IngresarP_():
    if (IdP.get() == "" or CantP.get() == ""):
        messagebox.showerror(message = "Debe ingresar la ID y la Cantidad del Producto!!!", title = "Error")
        return
    Produc = producto.buscarproducto(producto, IdP.get())
    if(len(Produc) == 0):
        messagebox.showerror(message = "El Producto no existe!!!\nIngreselo en la pestaña de \"Producto\"", title = "Error")
        return    
    if(int(CantP.get()) == 0 or int(CantP.get()) < 0):
        messagebox.showwarning(message = "Ingrese una cantidad valida!!!", title = "Stock")
        return    
    for i in Products:
        if i[0] == IdP.get():
            messagebox.showwarning(message = "Producto ya ingresado!!!", title = "Stock")
            return  

    TablaPC.add_row([Produc[0][0], Produc[0][1], CantP.get(), Produc[0][4], round(float(CantP.get()) * float(Produc[0][4]), 2)])
    ProductsC.append([IdP.get(), CantP.get()])
    print(ProductsC)
    Sb = float(SubTP.get()) + (float(CantP.get()) * float(Produc[0][4]))
    SubTP.config(state = 'normal')
    SubTP.delete(0, tk.END)
    SubTP.insert(0, str(round(Sb, 2)))
    SubTP.config(state = 'readonly')

    IvaP.config(state = 'normal')
    IvaP.delete(0, tk.END)
    IvaP.insert(0, str(round((Sb * 0.12), 2)))
    IvaP.config(state = 'readonly')

    TotalP.config(state = 'normal')
    TotalP.delete(0, tk.END)
    TotalP.insert(0, str(round((Sb * 1.12), 2)))
    TotalP.config(state = 'readonly')

    IdP.delete(0, tk.END)
    CantP.delete(0, tk.END)

class Table(tk.Frame):
    def __init__(self, parent=None, title="", headers=[], height=10, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self._title = tk.Label(self, text=title, font=("Helvetica", 16))
        self._headers = headers
        self._tree = ttk.Treeview(self,
                                  height=height,
                                  columns=self._headers, 
                                  show="headings")
        self._title.pack(side=tk.TOP, fill="x")

        vsb = ttk.Scrollbar(self, orient="vertical", command=self._tree.yview)
        vsb.pack(side='right', fill='y')
        hsb = ttk.Scrollbar(self, orient="horizontal", command=self._tree.xview)
        hsb.pack(side='bottom', fill='x')

        self._tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
        self._tree.pack(side="left", fill = "x", expand = True)

        for header in self._headers:
            self._tree.heading(header, text=header.title())
            self._tree.column(header, stretch=True,
                              width=tkFont.Font().measure(header.title()))
    def get_select(self):        
        return self._tree.item(self._tree.selection())['values']
    
    def clean_rows(self):
        for i in self._tree.get_children():
            self._tree.delete(i)

    def delete(self):
        try:
            selected_item = self._tree.selection()[0] ## get selected item
            self._tree.delete(selected_item)
        except IndexError:
            messagebox.showerror(message = "Debe seleccionar un registro!!!", title = "Error")

    def add_row(self, row):        
        self._tree.insert('', 'end', values=row)
        for i, item in enumerate(row):
            col_width = tkFont.Font().measure(item)
            if self._tree.column(self._headers[i], width=None) < col_width:
                    self._tree.column(self._headers[i], width=col_width)

root = Tk()
root.geometry("500x500")
root.resizable(0, 0)
root.title("GemiTreitorApps S.A")
validation = root.register(only_numbers)
Vdecimal = root.register(only_decimal)

log = Tk()
log.geometry("250x175")
log.resizable(0, 0)
log.title("Login")

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def Mostrar(): #Login
    if Us.get() == "" or Pass.get() == "":
        messagebox.showerror(message = "Debe llenar los campos!!!", title = "Error")
        return
    Uss = usuario.buscarusuario(usuario, Us.get())
    if len(Uss) == 0:
        messagebox.showinfo(message = "El Usuario ingresado no existe!!!", title = "Alerta")
        return
    if Pass.get() == Uss[0][1]:
        if Uss[0][2] == "Empleado":
            IdPr.config(state = 'disable')
            NombrePr.config(state = 'disable')
            GastoPr.config(state = 'disable')
            BG_.config(state = 'disable')
            BL_.config(state = 'disable')
            BE_.config(state = 'disable')            
            BE.config(state = 'disable')

            tab_control.hide(tab3)
            tab_control.hide(tab4)
            tab_control.hide(tab6)
            tab_control.hide(tab7)
        root.deiconify()
        log.destroy()
        return
    messagebox.showerror(message = "La contraseña ingresada es incorrecta!!!", title = "Error")

#Login
log_ = Frame(log, width = 250, height = 175)
log_.pack()

Esp1 = Label(log_, text = "")
Esp1.pack()
lab1 = Label(log_, text = "Usuario:")
lab1.pack()
Us = Entry(log_, width = 20)
Us.pack()
lab2 = Label(log_, text = "Contraseña:")
lab2.pack()
Pass = Entry(log_, width = 20, show = "*")
Pass.pack()
Esp2 = Label(log_, text = "")
Esp2.pack()
Button(log_, text = "Ingresar", command = Mostrar).pack()

log_.pack(expand = 1, fill = 'both')

#Principal
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control) # Caja
tab2 = ttk.Frame(tab_control) # Producto
tab3 = ttk.Frame(tab_control) # Proveedores
tab4 = ttk.Frame(tab_control) # Factura
tab5 = ttk.Frame(tab_control) # Clientes
tab6 = ttk.Frame(tab_control) # Usuarios
tab7 = ttk.Frame(tab_control) # Compra

tab_control.add(tab1, text = "Caja")
tab_control.add(tab2, text = "Producto")
tab_control.add(tab5, text = "Clientes")
tab_control.add(tab3, text = "Proveedores")
tab_control.add(tab7, text = "Compra")
tab_control.add(tab4, text = "Facturas")
tab_control.add(tab6, text = "Usuarios")

# Caja
Tabs = Frame(tab1, width = 400, height = 250)
Tabs.pack(side = BOTTOM, anchor = SW)
Tabs.config(relief = RAISED, bd = 4)
Tabs.pack_propagate(0)

Dat = Frame(tab1,width = 245, height = 235)
Dat.pack(side = LEFT, anchor = NW)
Dat.pack_propagate(0)
Dat.config(relief = RAISED, bd = 5)

Dat2 = Frame(tab1, width = 245, height = 235)
Dat2.pack(side = RIGHT, anchor = NE)
Dat2.config(relief = RAISED, bd = 5)
Dat2.pack_propagate(0)

#Der

Id_ = Label(Dat2, text = "Id Producto:")
Id_.place(x = 10, y = 20)
Id = Entry(Dat2, width = 10, validate='all',validatecommand=(validation, '%S'))
Id.place(x = 10, y = 40)

Cant_ = Label(Dat2, text = "Cantidad:")
Cant_.place(x = 100, y = 20)
Cant = Entry(Dat2, width = 10, validate='all',validatecommand=(validation, '%S'))
Cant.place(x = 100, y = 40)

Button(Dat2, text = "Ingresar", command = IngresarP).place(x = 10, y = 70)
Button(Dat2, text = "Eliminar", command = EliminarP ).place(x = 10, y = 110)

#Izq

CIC_ = Label(Dat, text = "CI:")
CIC_.place(x = 10, y = 10)
CIC = Entry(Dat, width = 11, validate='all',validatecommand=(validation, '%S'))
CIC.place(x = 10, y = 30)

NombreC_ = Label(Dat, text = "Nombre:")
NombreC_.place(x = 10, y = 60)
NombreC = Entry(Dat, width = 15)
NombreC.place(x = 10, y = 80)
NombreC.config(state = "readonly")

ApellidosC_ = Label(Dat, text = "Apellidos:")
ApellidosC_.place(x = 10, y = 110)
ApellidosC = Entry(Dat, width = 15)
ApellidosC.place(x = 10, y = 130)
ApellidosC.config(state = "readonly")

TelefonoC_ = Label(Dat, text = "Telefono:")
TelefonoC_.place(x = 10, y = 160)
TelefonoC = Entry(Dat, width = 15)
TelefonoC.place(x = 10, y = 180)
TelefonoC.config(state = "readonly")

Button(Dat, text = "Buscar", command = BuscarC).place(x = 100, y = 26)

TablaP = Table(Tabs, title="Productos", headers=["Id", "Nombre", "Cantidad", "Pre. U", "Total"], height = 10)
TablaP.pack(side = 'bottom', anchor = S, fill = 'both')

SubT_ = Label(tab1, text = "SubTotal:")
SubT_.place(x = 410, y = 250)
SubT = Entry(tab1, width = 10)
SubT.insert(0, "0.0")
SubT.config(state = 'readonly')
SubT.place(x = 410, y = 270)

Iva_ = Label(tab1, text = "Iva:")
Iva_.place(x = 410, y = 300)
Iva = Entry(tab1, width = 10)
Iva.insert(0, "0.0")
Iva.config(state = 'readonly')
Iva.place(x = 410, y = 320)

Total_ = Label(tab1, text = "Total:")
Total_.place(x = 410, y = 350)
Total = Entry(tab1, width = 10)
Total.insert(0, "0.0")
Total.config(state = 'readonly')
Total.place(x = 410, y = 380)

Button(tab1, text = "Finalizar", command = FinalizarC).place(x = 410, y = 410)
Button(tab1, text = "Limpiar", command = LimpiarF).place(x = 410, y = 440)

# Proveedores
#L1
L1 = Frame(tab3, width = 500, height = 500)
L1.pack(side = LEFT, anchor = NW)
L1.config(relief = RAISED, bd = 2)
L1.pack_propagate(0)

RUCP_ = Label(L1, text = "RUC:")
RUCP_.place(x = 10, y = 20)
RUCP = Entry(L1, width = 20, validate='all',validatecommand=(validation, '%S')) # Entry- RUC del Proveedor
RUCP.place(x = 10, y = 40)

EmpresaP_ = Label(L1, text = "Empresa:")
EmpresaP_.place(x = 170, y = 20)
EmpresaP = Entry(L1, width = 20) # Entry- Empresa del Proveedor
EmpresaP.place(x = 170, y = 40)

NombreP_ = Label(L1, text = "Nombre:")
NombreP_.place(x = 10, y=70)
NombreP = Entry(L1, width = 20) # Entry- Nombre del Proveedor
NombreP.place(x=10, y=90)

ApellidoP_ = Label(L1, text = "Apellido:")
ApellidoP_.place(x = 170, y=70)
ApellidoP = Entry(L1, width = 20) # Entry- Apellido del Proveedor
ApellidoP.place(x=170, y=90)

DireccionP_ = Label(L1, text = "Direccion:")
DireccionP_.place(x = 330, y = 20)
DireccionP = Entry(L1, width = 20) # Entry- Direccion del Proveedor
DireccionP.place(x = 330, y = 40)

TelefonoP_ = Label(L1, text = "Telefono:")
TelefonoP_.place(x = 330, y = 70)
TelefonoP = Entry(L1, width = 20, validate='all',validatecommand=(validation, '%S')) # Entry- Telefono del Proveedor
TelefonoP.place(x = 330, y = 90)

Button(L1, text = "Guardar", command = G_Proveedor).place(x = 10, y = 120)
Button(L1, text = "Limpiar", command = L_Proveedor).place(x = 100, y = 120)
Button(L1, text = "Editar", command = M_Proveedor).place(x = 400, y = 120)


TablaPrv = Table(L1, title="", headers=["Ruc", "Empresa", "Nombres", "Apellidos", "Direccion", "Telefono"], height = 11)

Lista = proveedor.listarprov(proveedor)
TablaPrv.clean_rows()
for row in Lista:
    TablaPrv.add_row(row)
TablaPrv.pack(side = 'bottom', anchor = S, fill = 'x')

ttk.Separator(L1, orient= HORIZONTAL).place(x = 10, y = 180, width = 470 )


# Producto
L2 = Frame(tab2, width = 500, height = 500)
L2.pack(side = LEFT, anchor = NW)
L2.config(relief = RAISED, bd = 2)
L2.pack_propagate(0)

IdPr_ = Label(L2, text = "ID:")
IdPr_.place(x = 10, y = 30)
IdPr = Entry(L2, width = 20, validate='all',validatecommand=(validation, '%S')) # Entry- Id del Producto
IdPr.place(x = 10, y = 50)
IdPr.insert(0, str(producto.autoinc(producto)))
IdPr.config(state = "readonly")

NombrePr_ = Label(L2, text = "Nombre:")
NombrePr_.place(x = 170, y = 30)
NombrePr = Entry(L2, width = 20) # Entry- Nombre del Producto
NombrePr.place(x = 170, y = 50)

GastoPr_ = Label(L2, text = "Precio:")
GastoPr_.place(x = 330, y = 30)
GastoPr = Entry(L2, width = 20, validate='all',validatecommand=(Vdecimal, '%P')) # Entry- Gastos del Producto
GastoPr.place(x = 330, y = 50)

BG_ = Button(L2, text = "Guardar", command = G_Producto)
BG_.place(x = 10, y = 120)
BL_ = Button(L2, text = "Limpiar", command = L_Producto)
BL_.place(x = 100, y = 120)
BE_ = Button(L2, text = "Editar", command = M_Producto)
BE_.place(x = 400, y = 120)

TablaPr = Table(L2, title="", headers=["Id", "Nombre", "Stock", "Precio", "PvP"], height = 11)

Lista = producto.listarprod(producto)
TablaPr.clean_rows()
for row in Lista:
    TablaPr.add_row(row)
TablaPr.pack(side = 'bottom', anchor = S, fill = 'x')

ttk.Separator(L2, orient= HORIZONTAL).place(x = 10, y = 180, width = 470 )

# Compra

TabsP = Frame(tab7, width = 400, height = 250)
TabsP.pack(side = BOTTOM, anchor = SW)
TabsP.config(relief = RAISED, bd = 4)
TabsP.pack_propagate(0)

DatP = Frame(tab7,width = 245, height = 235)
DatP.pack(side = LEFT, anchor = NW)
DatP.pack_propagate(0)
DatP.config(relief = RAISED, bd = 5)

DatP2 = Frame(tab7, width = 245, height = 235)
DatP2.pack(side = RIGHT, anchor = NE)
DatP2.config(relief = RAISED, bd = 5)
DatP2.pack_propagate(0)

#Der

IdP_ = Label(DatP2, text = "Id Producto:")
IdP_.place(x = 10, y = 20)
IdP = Entry(DatP2, width = 10, validate='all',validatecommand=(validation, '%S'))
IdP.place(x = 10, y = 40)

CantP_ = Label(DatP2, text = "Cantidad:")
CantP_.place(x = 100, y = 20)
CantP = Entry(DatP2, width = 10, validate='all',validatecommand=(validation, '%S'))
CantP.place(x = 100, y = 40)

Button(DatP2, text = "Ingresar", command = IngresarP_).place(x = 10, y = 130)
Button(DatP2, text = "Eliminar", command = EliminarP_).place(x = 100, y = 130)

#Izq

Ruc_ = Label(DatP, text = "RUC:")
Ruc_.place(x = 10, y = 10)
Ruc = Entry(DatP, width = 11, validate='all',validatecommand=(validation, '%S'))
Ruc.place(x = 10, y = 30)

EmpP_ = Label(DatP, text = "Empresa:")
EmpP_.place(x = 10, y = 60)
EmpP = Entry(DatP, width = 15)
EmpP.place(x = 10, y = 80)
EmpP.config(state = "readonly")

NomP_ = Label(DatP, text = "Nombre:")
NomP_.place(x = 10, y = 110)
NomP = Entry(DatP, width = 15)
NomP.place(x = 10, y = 130)
NomP.config(state = "readonly")

ApeP_ = Label(DatP, text = "Apellidos:")
ApeP_.place(x = 10, y = 160)
ApeP = Entry(DatP, width = 15)
ApeP.place(x = 10, y = 180)
ApeP.config(state = "readonly")

TelP_ = Label(DatP, text = "Telefono:")
TelP_.place(x = 130, y = 110)
TelP = Entry(DatP, width = 15)
TelP.place(x = 130, y = 130)
TelP.config(state = "readonly")

DirP_ = Label(DatP, text = "Direccion:")
DirP_.place(x = 130, y = 160)
DirP = Entry(DatP, width = 15)
DirP.place(x = 130, y = 180)
DirP.config(state = "readonly")

Button(DatP, text = "Buscar", command = BuscarP).place(x = 100, y = 26)

TablaPC = Table(TabsP, title="Productos", headers=["Id", "Nombre", "Cantidad", "Pre. U", "Total"], height = 10)
TablaPC.pack(side = 'bottom', anchor = S, fill = 'both')

SubTP_ = Label(tab7, text = "SubTotal:")
SubTP_.place(x = 410, y = 250)
SubTP = Entry(tab7, width = 10)
SubTP.insert(0, "0.0")
SubTP.config(state = 'readonly')
SubTP.place(x = 410, y = 270)

IvaP_ = Label(tab7, text = "Iva:")
IvaP_.place(x = 410, y = 300)
IvaP = Entry(tab7, width = 10)
IvaP.insert(0, "0.0")
IvaP.config(state = 'readonly')
IvaP.place(x = 410, y = 320)

TotalP_ = Label(tab7, text = "Total:")
TotalP_.place(x = 410, y = 350)
TotalP = Entry(tab7, width = 10)
TotalP.insert(0, "0.0")
TotalP.config(state = 'readonly')
TotalP.place(x = 410, y = 380)

Button(tab7, text = "Finalizar", command = FinalizarC_).place(x = 410, y = 410)
Button(tab7, text = "Limpiar", command = LimpiarF_).place(x = 410, y = 440)

# Facturas
IdCF_ = Label(tab4, text = "ID Cliente:")
IdCF_.place(x = 10, y = 40)
IdCF = Entry(tab4, width = 20, validate='all',validatecommand=(validation, '%S'))
IdCF.place(x = 10, y = 60)
Button(tab4, text = "Buscar", command = B_FCliente).place(x = 10, y = 90)

IdF_ = Label(tab4, text = "ID Factura:")
IdF_.place(x = 270, y = 40)
IdF = Entry(tab4, width = 20, validate='all',validatecommand=(validation, '%S'))
IdF.place(x = 270, y = 60)
Button(tab4, text = "Buscar", command = M_Factura).place(x = 270, y = 90)

Button(tab4, text = "Generar Reporte", command = GenerarR).place(x = 270, y = 120)

TablaF = Table(tab4, title="", headers=["ID Factura", "Fecha", "Total"], height = 12)
TablaF.pack(side = 'bottom', anchor = S, fill = 'x')

# Clientes
CedC_ = Label(tab5, text = "Cedula:")
CedC_.place(x = 10, y = 20)
CedC = Entry(tab5, width = 20, validate='all',validatecommand=(validation, '%S')) # Entry- Cedula del Cliente
CedC.place(x = 10, y = 40)

NomC_ = Label(tab5, text = "Nombre:")
NomC_.place(x = 10, y = 70)
NomC = Entry(tab5, width = 20) # Entry- Nombre del Cliente
NomC.place(x = 10, y = 90)

ApeC_ = Label(tab5, text = "Apellidos:")
ApeC_.place(x = 170, y=70)
ApeC = Entry(tab5, width = 20) # Entry- Apellidos del Cliente
ApeC.place(x=170, y=90)

TelC_ = Label(tab5, text = "Telefono:")
TelC_.place(x = 330, y = 70)
TelC = Entry(tab5, width = 20, validate='all',validatecommand=(validation, '%S')) # Entry- Telefono del Cliente
TelC.place(x = 330, y = 90)

Button(tab5, text = "Guardar", command = G_Cliente).place(x = 10, y = 120)
Button(tab5, text = "Limpiar", command = L_Cliente).place(x = 100, y = 120)
BE = Button(tab5, text = "Editar", command = M_Cliente)
BE.place(x = 400, y = 120)

TablaC = Table(tab5, title="", headers=["CI", "Nombre", "Apellidos", "Telefono"], height = 11)

Lista = cliente.listarclientes(cliente)
TablaC.clean_rows()
for row in Lista:
    TablaC.add_row(row)
TablaC.pack(side = 'bottom', anchor = S, fill = 'x')

ttk.Separator(tab5, orient= HORIZONTAL).place(x = 10, y = 180, width = 470 )


# Usuarios
UwU_ = Label(tab6, text = "Usuario:")
UwU_.place(x = 10, y = 50)
UwU = Entry(tab6, width = 20)
UwU.place(x = 10, y = 70)

ConU_ = Label(tab6, text = "Password:")
ConU_.place(x = 170, y=50)
ConU = Entry(tab6, width = 20)
ConU.place(x=170, y=70)

TipU_ = Label(tab6, text = "Tipo:")
TipU_.place(x = 330, y = 50)
TipU = ttk.Combobox(tab6, state="readonly")
TipU["values"] = ["Administrador", "Empleado"]
TipU.place(x = 330, y = 70)

Button(tab6, text = "Guardar", command = G_Usuario).place(x = 10, y = 105)
Button(tab6, text = "Limpiar", command = L_Usuario).place(x = 100, y = 105)
Button(tab6, text = "Editar", command = M_Usuario).place(x = 400, y = 105)

TablaU = Table(tab6, title="", headers=["Usuario", "Tipo"], height = 11)

Lista = usuario.listarusers(usuario)
TablaU.clean_rows()
for row in Lista:
    TablaU.add_row(row)
TablaU.pack(side = 'bottom', anchor = S, fill = 'x')

ttk.Separator(tab6, orient= HORIZONTAL).place(x = 10, y = 180, width = 470 )
tab_control.pack(expand = 1, fill = 'both')

center(root)
center(log)

root.withdraw()
log.mainloop()
root.mainloop()
