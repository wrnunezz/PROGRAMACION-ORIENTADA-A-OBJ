import tkinter as tk

#crear la ventana
app=tk.Tk()
app.geometry('600x600')
app.title("Ejemplo ")
app.configure(background='blue')
# variables
entrada= tk.StringVar(app)
lista_datos = []

# función de agregar datos
def agregar_dato():
    texto_ingresado = entrada.get()
    if texto_ingresado:
        lista.insert(tk.END,texto_ingresado)
        entrada.set("")
    else:
        print("Campo nulo")



# componentes
tk.Label(app, text="Ingrese el valor : ", font=('Arial',10)).pack(pady=10)
tk.Entry(app,fg='black', bg='white',font=('Arial',10),textvariable=entrada).pack(pady=10)
tk.Button(app, text="Agregar",font=('Arial',10),bg='red', fg='white', command=agregar_dato).pack (pady=10)
# lista para agregar datos
lista = tk.Listbox(app,font=('Arial',12),width=40,height=20)
lista.pack(pady=10)













app.mainloop()