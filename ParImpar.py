from tkinter import *

raiz=Tk()
raiz.title("Par o Impar")
raiz.geometry('350x200')
#raiz.config(bg="gray")

def parimpar(num):
    try:
        num=float(num)
    except ValueError:
        result.set("Por favor, ingrese un numero entero entre 0 y 100")
        numero.set('')
        return
    
    if num%1!=0 or num<0 or num>100:
        result.set("Por favor, ingrese un numero entero entre 0 y 100")
        numero.set('')
    else:
        if num%2==0:
            result.set(str(int(num)) + " es par.")
            numero.set('')
        else:
            result.set(str(int(num)) + " es impar.")
            numero.set('')
    

marco=Frame(raiz)
marco.config(pady=20,padx=30)
marco.pack()

numero=StringVar()
entryNumero=Entry(marco,textvariable=numero)
entryNumero.grid(row=1,pady=5)

boton=Button(marco,text=' ¿Par o impar? ',command=lambda:parimpar(entryNumero.get()))
boton.grid(row=2)

result=StringVar()

resultado=Label(marco,textvariable=result)
resultado.grid(row=3,pady=10)

salir=Button(marco,text="     Salir     ",command=lambda:exit())
salir.grid(row=4)

raiz.mainloop()