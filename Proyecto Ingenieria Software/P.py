from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from tkcalendar import *
import datetime
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
from Proveedor import *
from Producto import *
from Factura import *
from Detalle import *
from Cliente import *
from Producto import *
import pandas as pd
from tabulate import tabulate
import csv

#name = simpledialog.askstring(title="Test",prompt="What's your Name?:")
#print(name)

Rep = Tk()
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

def getDate():
    archivo = filedialog.askdirectory(title = "Guardar Reporte")
    if(archivo == ""):
        messagebox.showerror(message = "Debe de ingresar una direccion!!!", title = "Error")
        return
    print(archivo)
    R = factura.detallesmes(factura, Cali.get_date(), Calf.get_date())
    Tablita = tabulate(R, headers = ["Nombre", "Cantidad", "Total"], tablefmt='fancy_grid')
    ds = pd.DataFrame(["****Reporte****", " ",
     "Fecha inicial: " + Cali.get_date(), "Fecha final: " + Calf.get_date(),
     " ", "Total de venta: " + str(round(float(factura.ganancias(factura, Cali.get_date(), Calf.get_date())),2)),
     "Total de compra: " +  str(round(float(factura.perdidas(factura,Cali.get_date(), Calf.get_date())),2)), " ",
     "Ganancias: " + str(round(float(factura.ganancias(factura, Cali.get_date(), Calf.get_date())) - float(factura.perdidas(factura,Cali.get_date(), Calf.get_date())), 2)),
     " ","Productos vendidos: ",Tablita])
    ds.to_csv(archivo + '/Reporte desde ' + Cali.get_date() + ' a ' + Calf.get_date() +'.txt', header=None, index=False, sep="\t", quoting=csv.QUOTE_NONE, quotechar="",  escapechar="_")
    Rep.quit()

Button(Rep, text = "Generar Reporte", command = getDate).place(x = 240, y = 275)

Rep.mainloop()


# MU = Tk()
# MU.geometry("267x90")
# MU.resizable(0, 0)
# MU.title("Registrar Producto")
# MU.focus_set()
# MU.grab_set()

# N_ = Label(MU, text = "Nombre:")
# N_.place(x = 77, y = 10)
# N = Entry(MU, width = 20)
# N.place(x = 77, y = 30)

# Button(MU, text = "Guardar").place(x = 107, y = 55)

# MU.mainloop()



# class Table(tk.Frame):
#     def __init__(self, parent=None, title="", headers=[], height=10, *args, **kwargs):
#         tk.Frame.__init__(self, parent, *args, **kwargs)
#         self._title = tk.Label(self, text=title, font=("Helvetica", 16))
#         self._headers = headers
#         self._tree = ttk.Treeview(self,
#                                   height=height,
#                                   columns=self._headers, 
#                                   show="headings")
#         self._title.pack(side=tk.TOP, fill="x")

#         # Agregamos dos scrollbars 
#         vsb = ttk.Scrollbar(self, orient="vertical", command=self._tree.yview)
#         vsb.pack(side='right', fill='y')
#         hsb = ttk.Scrollbar(self, orient="horizontal", command=self._tree.xview)
#         hsb.pack(side='bottom', fill='x')

#         self._tree.configure(xscrollcommand=hsb.set, yscrollcommand=vsb.set)
#         self._tree.pack(side="left", fill = "x", expand = True)

#         for header in self._headers:
#             self._tree.heading(header, text=header.title())
#             self._tree.column(header, stretch=True,
#                               width=tkFont.Font().measure(header.title()))

#     def clean_rows(self):
#         for i in self._tree.get_children():
#             self._tree.delete(i)

#     def add_row(self, row):        
#         self._tree.insert('', 'end', values=row)
#         for i, item in enumerate(row):
#             col_width = tkFont.Font().measure(item)
#             if self._tree.column(self._headers[i], width=None) < col_width:
#                     self._tree.column(self._headers[i], width=col_width)


# Fact = Tk()
# Fact.geometry("400x500")
# Fact.resizable(0, 0)
# Fact.title("Factura")

# DatF = factura.buscarfactura(factura, "2")
# DatC = cliente.buscarcliente(cliente, DatF[0][3])
# DetF = detalle.buscardetalle(detalle, "2")

# IDF_ = Label(Fact, text = "ID Factura:")
# IDF_.place(x = 10, y = 20)
# IDF = Entry(Fact, width = 17)
# IDF.place(x = 10, y = 40)

# CF_ = Label(Fact, text = "Cedula:")
# CF_.place(x = 10, y = 70)
# CF = Entry(Fact, width = 17)
# CF.place(x = 10, y = 90)

# NomF_ = Label(Fact, text = "Nombre:")
# NomF_.place(x = 140, y = 70)
# NomF = Entry(Fact, width = 17)
# NomF.place(x = 140, y = 90)

# ApeF_ = Label(Fact, text = "Apellido:")
# ApeF_.place(x = 280, y = 70)
# ApeF = Entry(Fact, width = 17)
# ApeF.place(x = 280, y = 90)

# TelF_ = Label(Fact, text = "Telefono:")
# TelF_.place(x = 10, y = 120)
# TelF = Entry(Fact, width = 17)
# TelF.place(x = 10, y = 140)

# FechF_ = Label(Fact, text = "Fecha:")
# FechF_.place(x = 140, y = 120)
# FechF = Entry(Fact, width = 17)
# FechF.place(x = 140, y = 140)

# TotF_ = Label(Fact, text = "Total:")
# TotF_.place(x = 280, y = 120)
# TotF = Entry(Fact, width = 17)
# TotF.place(x = 280, y = 140)

# IDF.insert(0, DatF[0][0])
# IDF.config(state = 'disable')

# CF.insert(0, DatC[0][0])
# CF.config(state = 'disable')

# NomF.insert(0, DatC[0][1])
# NomF.config(state = 'disable')

# ApeF.insert(0, DatC[0][2])
# ApeF.config(state = 'disable')

# TelF.insert(0, DatC[0][3])
# TelF.config(state = 'disable')

# FechF.insert(0, DatF[0][1])
# FechF.config(state = 'disable')

# TotF.insert(0, DatF[0][2])
# TotF.config(state = 'disable')

# TabF = Table(Fact, title="", headers=["Cant", "Nombre", "P.U", "Total"], height = 13)
# TabF.place(x = 20, y = 160, width = 370)

# for row in DetF:
#     print(row[2])
#     print(row[3])
#     #print(row[2] + "+" + row[3] + "= " + str(float(row[0]) * float(row[3])))
#     TabF.add_row([row[2], (producto.buscarproducto(producto, row[0]))[0][1], row[3], round(float(row[2]) * float(row[3]), 2)])

# print(producto.buscarproducto(producto, 1)[0][1])

# Fact.mainloop()