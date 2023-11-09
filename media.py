from tkinter import *

def calcular():
    media = (float(nota1.get()) + float(nota2.get()) + float(nota3.get())) / 3.0
    if media > 7.0: 
        print('valeu fera')
        lbl_resultado.configure(text='valeu fera')
    elif media > 5:
        print('ai mamae')
        lbl_resultado.configure(text='ai ai mamae')
    else:
        print('else')
        lbl_resultado.configure(text='else')

tela = Tk()
tela.geometry('300x300')
lbl1 = Label(text='Informe 03 notas')
lbl1.pack()

nota1 = Entry()
nota1.pack()
nota2 = Entry()
nota2.pack()
nota3 = Entry()
nota3.pack()

lbl_resultado = Label(text='')
lbl_resultado.pack()

btn = Button(text='calcular',command=calcular)
btn.pack()

tela.mainloop()