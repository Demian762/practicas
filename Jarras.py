from tkinter import *
from tkinter import messagebox

raiz = Tk()
raiz.title("Juego de Jarras")
raiz.geometry("380x300")
raiz.resizable(0,0)

explicacion=Label(raiz,text="Debes lograr que en la jarra izquierda queden 4 litros de agua")
explicacion.grid(column=0,row=0,columnspan=2,pady=20,padx=20)

jarra5=StringVar()
jarra5.set("0")
entry5=Entry(raiz,textvariable=jarra5)
entry5.grid(column=0,row=5)
jarra3=StringVar()
jarra3.set("0")
entry3=Entry(raiz,textvariable=jarra3)
entry3.grid(column=1,row=5)

def llenar(botella):

    if botella==5:
        jarra5.set("5")
    if botella==3:
        jarra3.set("3")

llena5=Button(raiz,text="Llenar jarra de 5 litros",command=lambda:llenar(5))
llena5.grid(column=0,row=1,pady=10)
llena3=Button(raiz,text="Llenar jarra de 3 litros",command=lambda:llenar(3))
llena3.grid(column=1,row=1,pady=10)

def vaciar(botella):

    if botella==5:
        jarra5.set("0")
    if botella==3:
        jarra3.set("0")

llena5=Button(raiz,text="Vaciar jarra de 5 litros",command=lambda:vaciar(5))
llena5.grid(column=0,row=2,pady=10)
llena3=Button(raiz,text="Vaciar jarra de 3 litros",command=lambda:vaciar(3))
llena3.grid(column=1,row=2,pady=10)

def pasar5a3():
    j5=int(jarra5.get())
    j3=int(jarra3.get())
    j5n=j5-(3-j3)
    j3n=j3+j5
    if j5n<0:
        j5n=0
    if j3n>3:
        j3n=3
    jarra5.set(str(j5n))
    jarra3.set(str(j3n))
    if jarra5.get()=="4":
        ganar=messagebox.askokcancel("Felicitaciones!!","¿Desea continuar?")
        if ganar:
            jarra5.set("0")
            jarra3.set("0")
        else:
            raiz.destroy()

def pasar3a5():
    j5=int(jarra5.get())
    j3=int(jarra3.get())
    j5n=j5+j3
    j3n=j3-(5-j5)
    if j5n>5:
        j5n=5
    if j3n<0:
        j3n=0
    jarra5.set(str(j5n))
    jarra3.set(str(j3n))
    if jarra5.get()=="4":
        ganar=messagebox.askokcancel("Felicitaciones!!","¿Desea continuar?")
        if ganar:
            jarra5.set("0")
            jarra3.set("0")
        else:
            raiz.destroy()


vaciar5=Button(raiz,text="5 >>>> 3",command=lambda:pasar5a3())
vaciar5.grid(column=0,row=3,pady=10)
vaciar3=Button(raiz,text="3 <<<< 5",command=lambda:pasar3a5())
vaciar3.grid(column=1,row=3,pady=10)

jarra5label=Label(raiz,text="Jarra 5 L:")
jarra5label.grid(column=0,row=4,pady=10)
jarra3label=Label(raiz,text="Jarra 3 L:")
jarra3label.grid(column=1,row=4,pady=10)





raiz.mainloop()