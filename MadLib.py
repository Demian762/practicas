#from ctypes import alignment ESTO SE PUSO SOLO!
from tkinter import *

raiz=Tk()
raiz.title("Historia Loca")
raiz.geometry("400x600")

titulo=Label(raiz,text="Historia Loca")
titulo.grid(row=0,column=0,columnspan=2,pady=20)

var1label=Label(raiz,text="Año lejano en el futuro: ")
var1label.grid(row=1,column=0,sticky=W)
var1entry=Entry(raiz)
var1entry.grid(row=1,column=1,sticky=E,padx=50)
var2label=Label(raiz,text="Forma geométrica (3D): ")
var2label.grid(row=2,column=0,sticky=W)
var2entry=Entry(raiz)
var2entry.grid(row=2,column=1,sticky=E,padx=50)
var3label=Label(raiz,text="Material de construcción:")
var3label.grid(row=3,column=0,sticky=W)
var3entry=Entry(raiz)
var3entry.grid(row=3,column=1,sticky=E,padx=50)
var4label=Label(raiz,text="Adjetivo (masc, singular):")
var4label.grid(row=4,column=0,sticky=W)
var4entry=Entry(raiz)
var4entry.grid(row=4,column=1,sticky=E,padx=50)
var5label=Label(raiz,text="Verbo en gerundio:")
var5label.grid(row=5,column=0,sticky=W)
var5entry=Entry(raiz)
var5entry.grid(row=5,column=1,sticky=E,padx=50)
var6label=Label(raiz,text="Número:")
var6label.grid(row=6,column=0,sticky=W)
var6entry=Entry(raiz)
var6entry.grid(row=6,column=1,sticky=E,padx=50)
var7label=Label(raiz,text="Adjetivo (masc, plural):")
var7label.grid(row=7,column=0,sticky=W)
var7entry=Entry(raiz)
var7entry.grid(row=7,column=1,sticky=E,padx=50)
var8label=Label(raiz,text="Color:")
var8label.grid(row=8,column=0,sticky=W)
var8entry=Entry(raiz)
var8entry.grid(row=8,column=1,sticky=E,padx=50)
var9label=Label(raiz,text="Otro número:")
var9label.grid(row=9,column=0,sticky=W)
var9entry=Entry(raiz)
var9entry.grid(row=9,column=1,sticky=E,padx=50)
var10label=Label(raiz,text="Fruta:")
var10label.grid(row=10,column=0,sticky=W)
var10entry=Entry(raiz)
var10entry.grid(row=10,column=1,sticky=E,padx=50)
var11label=Label(raiz,text="Mamífero:")
var11label.grid(row=11,column=0,sticky=W)
var11entry=Entry(raiz)
var11entry.grid(row=11,column=1,sticky=E,padx=50)
var12label=Label(raiz,text="Verbo en infinitivo:")
var12label.grid(row=12,column=0,sticky=W)
var12entry=Entry(raiz)
var12entry.grid(row=12,column=1,sticky=E,padx=50)
var13label=Label(raiz,text="insectos (masc, plural):")
var13label.grid(row=13,column=0,sticky=W)
var13entry=Entry(raiz)
var13entry.grid(row=13,column=1,sticky=E,padx=50)
var14label=Label(raiz,text="adjetivo (masc, plural):")
var14label.grid(row=14,column=0,sticky=W)
var14entry=Entry(raiz)
var14entry.grid(row=14,column=1,sticky=E,padx=50)

def completo():
    
    texto.set("En el año " + var1entry.get() + " yo estaba viviendo con mi familia en un \n"
    + var2entry.get() + " irregular hecho de " + var3entry.get() + ". Por el cielo vimos \n"
    "que se acercaba un OVNI " + var4entry.get() + ". Estaba " + var5entry.get() + " sobre\n"
    " el jardín de nuestro " + var2entry.get() + " cuando aterrizó y de él salieron\n"
    + var6entry.get() + " extraterrestres. Eran muy " + var7entry.get() + " y de color \n"
    + var8entry.get() + ". Tenían " + var9entry.get() + " piernas y la cabeza en forma de \n"
    + var10entry.get() + ". Nos quedamos con cara de " + var11entry.get() + " y nos dio por \n"
    + var12entry.get() + ". Se debieron asustar, porque empezaron a moverse como \n"
    + var13entry.get() + " " + var14entry.get() + " y se fueron.")

aceptar=Button(raiz,text="Continuar",command=completo)
aceptar.grid(row=15,columnspan=2,pady=20)
aceptar.config(padx=10)

texto=StringVar()
cuento_completo=Label(raiz,textvariable=texto)
cuento_completo.grid(row=16,columnspan=2)

raiz.mainloop()