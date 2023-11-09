
from tkinter import *

def conta_vogais(): 
    string = input.get().lower() # para que a comparação não seja sensível a maiuscula/minuscula 
    result = {} 
    vogais = 'aeiou' 
    for i in vogais: 
        if i in string: 
            result[i] = string.count(i) 
    lbl.configure(text=result)        

tela = Tk()
tela.geometry('300x300')

input = Entry()
input.pack()

lbl = Label(text='')
lbl.pack()

btn = Button(text='contar',command=conta_vogais)
btn.pack()

tela.mainloop()
