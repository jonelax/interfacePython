import tkinter as tki

root = tki.Tk()

def btnFuncion():
    ventanaDatos = tki.Toplevel(root)
    ventanaDatos.title("Datos ingresados")
    ventanaDatos.geometry("400x300")

    tki.Label(ventanaDatos, text = "Ruta archivo mes 1: " + entry1.get()).grid(row=0,column=0)
    tki.Label(ventanaDatos, text = "Ruta archivo mes 2: " + entry2.get()).grid(row=1,column=0)
    tki.Label(ventanaDatos, text = "Ruta archivo mes 3: " + entry3.get()).grid(row=2,column=0)
    tki.Label(ventanaDatos, text = "Ruta archivo mes 4: " + entry4.get()).grid(row=3,column=0)
    tki.Label(ventanaDatos, text = "Ruta archivo mes 5: " + entry5.get()).grid(row=4,column=0)
    tki.Label(ventanaDatos, text = "Ruta archivo mes 6: " + entry6.get()).grid(row=5,column=0)
    tki.Label(ventanaDatos, text = "Ruta archivo mes 7: " + entry7.get()).grid(row=6,column=0)
    tki.Label(ventanaDatos, text = "Ruta archivo mes 8: " + entry8.get()).grid(row=7,column=0)
    tki.Label(ventanaDatos, text = "Ruta archivo mes 9: " + entry9.get()).grid(row=8,column=0)
    tki.Label(ventanaDatos, text = "Ruta archivo mes 10: " + entry10.get()).grid(row=9,column=0)
    tki.Label(ventanaDatos, text = "Ruta archivo mes 11: " + entry11.get()).grid(row=10,column=0)
    tki.Label(ventanaDatos, text = "Ruta archivo mes 12: " + entry12.get()).grid(row=11,column=0)
    tki.Label(ventanaDatos, text = "Ruta output: " + entry13.get()).grid(row=12,column=0)
    tki.Label(ventanaDatos, text = "Nombre archivo output: " + entry14.get()).grid(row=13,column=0)
    tki.Label(ventanaDatos, text = "Mínimo de deuda: " + entry15.get()).grid(row=14,column=0)
    tki.Label(ventanaDatos, text = "Ruta archivo cuentas contables: " + entry16.get()).grid(row=15,column=0)

root.title("Interfaz")
root.geometry("900x600")

labelm1 = tki.Label(root, text = "Ruta archivo mes 1: ", height = 5, width = 20)
labelm1.config(font=("bold", 10))
labelm1.grid(row=0,column=0)

entry1=tki.Entry()
entry1.grid(row=0,column=1)
#
labelm2 = tki.Label(root, text = "Ruta archivo mes 2: ", height = 5, width = 20)
labelm2.config(font=("bold", 10))
labelm2.grid(row=1,column=0)

entry2=tki.Entry()
entry2.grid(row=1,column=1)
#
labelm3 = tki.Label(root, text = "Ruta archivo mes 3: ", height = 5, width = 20)
labelm3.config(font=("bold", 10))
labelm3.grid(row=2,column=0)

entry3=tki.Entry()
entry3.grid(row=2,column=1)
#
labelm4 = tki.Label(root, text = "Ruta archivo mes 4: ", height = 5, width = 20)
labelm4.config(font=("bold", 10))
labelm4.grid(row=3,column=0)

entry4=tki.Entry()
entry4.grid(row=3,column=1)
#
labelm5 = tki.Label(root, text = "Ruta archivo mes 5: ", height = 5, width = 20)
labelm5.config(font=("bold", 10))
labelm5.grid(row=4,column=0)

entry5=tki.Entry()
entry5.grid(row=4,column=1)
#
labelm6 = tki.Label(root, text = "Ruta archivo mes 6: ", height = 5, width = 20)
labelm6.config(font=("bold", 10))
labelm6.grid(row=5,column=0)

entry6=tki.Entry()
entry6.grid(row=5,column=1)
#
labelm7 = tki.Label(root, text = "Ruta archivo mes 7: ", height = 5, width = 20)
labelm7.config(font=("bold", 10))
labelm7.grid(row=0,column=2)

entry7=tki.Entry()
entry7.grid(row=0,column=3)
#
labelm8 = tki.Label(root, text = "Ruta archivo mes 8: ", height = 5, width = 20)
labelm8.config(font=("bold", 10))
labelm8.grid(row=1,column=2)

entry8=tki.Entry()
entry8.grid(row=1,column=3)
#
labelm9 = tki.Label(root, text = "Ruta archivo mes 9: ", height = 5, width = 20)
labelm9.config(font=("bold", 10))
labelm9.grid(row=2,column=2)

entry9=tki.Entry()
entry9.grid(row=2,column=3)
#
labelm10 = tki.Label(root, text = "Ruta archivo mes 10: ", height = 5, width = 20)
labelm10.config(font=("bold", 10))
labelm10.grid(row=3,column=2)

entry10=tki.Entry()
entry10.grid(row=3,column=3)
#
labelm11 = tki.Label(root, text = "Ruta archivo mes 11: ", height = 5, width = 20)
labelm11.config(font=("bold", 10))
labelm11.grid(row=4,column=2)

entry11=tki.Entry()
entry11.grid(row=4,column=3)
#
labelm12 = tki.Label(root, text = "Ruta archivo mes 12: ", height = 5, width = 20)
labelm12.config(font=("bold", 10))
labelm12.grid(row=5,column=2)

entry12=tki.Entry()
entry12.grid(row=5,column=3)
#
labelro = tki.Label(root, text = "Ruta output: ", height = 5, width = 20)
labelro.config(font=("bold", 10))
labelro.grid(row=0,column=4)

entry13=tki.Entry()
entry13.grid(row=0,column=5)
#
labelout = tki.Label(root, text = "Nombre archivo output: ", height = 5, width = 20)
labelout.config(font=("bold", 10))
labelout.grid(row=1,column=4)

entry14=tki.Entry()
entry14.grid(row=1,column=5)
#
labelde = tki.Label(root, text = "Mínimo de deuda: ", height = 5, width = 20)
labelde.config(font=("bold", 10))
labelde.grid(row=2,column=4)

entry15=tki.Entry()
entry15 .grid(row=2,column=5)
#
labelcc = tki.Label(root, text = "Ruta archivo\n cuentas contables:", height = 5, width = 20)
labelcc.config(font=("bold", 10))
labelcc.grid(row=3,column=4)

entry16=tki.Entry()
entry16 .grid(row=3,column=5)
#

btnEst = tki.Button(root,text = "Estimar", command = btnFuncion)
btnEst.config(font=("bold", 13),bg="white")
btnEst.grid(row=7,column=3)


root.mainloop()
