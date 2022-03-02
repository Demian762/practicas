from tkinter import *

def calcular():
    """
    Esto es un docstring, no es un comentario normal    
    """
    try:
        tcp=float(factura.get())
    except:
        factura.set("")
    
    if propinopcion.get()==1:
        tcp=round(tcp*1.05,2)
    elif propinopcion.get()==2:
        tcp=round(tcp*1.1,2)
    elif propinopcion.get()==3:
        tcp=round(tcp*1.15,2)
    total.set(str(tcp))

    tpc=tcp/comensales.get()
    porcomensal.set(str(round(tpc,2)))


raiz=Tk()
raiz.title("Calculadora de propinas")
raiz.geometry("300x250")

# -------------------TITULO----------------------------

frameTitle=Frame(raiz)
frameTitle.pack()

Label(frameTitle,text="\nCalculadora de propinas\n").pack()

# -------------------INPUT--------------------------------

frameInput=Frame(raiz)
frameInput.pack()

facturaLabel=Label(frameInput,text="Factura")
facturaLabel.grid(column=0,row=0)
factura=StringVar()
facturaEntry=Entry(frameInput,textvariable=factura)
facturaEntry.grid(column=1,row=0,columnspan=3)

propinaLabel=Label(frameInput,text="% de propina")
propinaLabel.grid(column=0,row=1)
propinopcion=IntVar()
rabu1=Radiobutton(frameInput,text="5%",variable=propinopcion,value=1)
rabu1.grid(column=1,row=1)
rabu2=Radiobutton(frameInput,text="10%",variable=propinopcion,value=2)
rabu2.grid(column=2,row=1)
rabu3=Radiobutton(frameInput,text="15%",variable=propinopcion,value=3)
rabu3.grid(column=3,row=1)

comensalesLabel=Label(frameInput,text="Cant comensales")
comensalesLabel.grid(row=3,column=0)
numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
comensales=IntVar()
comensales.set(numeros[0])
comensalesMenu=OptionMenu(frameInput,comensales,*numeros)
comensalesMenu.grid(column=1,row=3,columnspan=3)

# -----------------OUTPUT-----------------------------------

frameOutput=Frame(raiz)
frameOutput.pack()

separador=Label(frameOutput,text="----------------------------------------------------")
separador.grid(column=0,row=0,columnspan=3)

total=StringVar()
totalLabel=Label(frameOutput,text="Total con propina")
totalLabel.grid(column=0,row=1)
totalEntry=Entry(frameOutput,textvariable=total)
totalEntry.grid(column=1,row=1)

porcomensal=StringVar()
divididoLabel=Label(frameOutput,text="Cada comensal paga")
divididoLabel.grid(column=0,row=2)
divididoEntry=Entry(frameOutput,textvariable=porcomensal)
divididoEntry.grid(column=1,row=2)

calcularBoton=Button(frameOutput,text="Calcular",command=lambda:calcular())
calcularBoton.grid(column=0,row=3,columnspan=3,pady=10)
calcularBoton.config(pady=5,padx=15)

raiz.mainloop()