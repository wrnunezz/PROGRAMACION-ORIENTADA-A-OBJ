# Interfaz grafica
import tkinter as tk

app = tk.Tk()
app.title(' Clase Encuentro')
app.geometry('500x500')

def mostra():
    print("hola")

tk.Button(
    app,
    text='Encuentro',
    bg='blue',
    fg='white',
    font=('Arial', 10, 'bold'),
    command=mostra,

).pack(side=tk.TOP, fill=tk.X)







app.mainloop()

