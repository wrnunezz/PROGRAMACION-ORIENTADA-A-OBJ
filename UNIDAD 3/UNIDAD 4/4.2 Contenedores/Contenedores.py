# tkinter
"""
Utilizar Tkinter para diseñar la interfaz.
La aplicación debe tener una ventana principal que muestre una lista (TreeView) de eventos o tareas programadas, incluyendo detalles como la fecha, la hora y una breve descripción.
Incluir campos de entrada (Entry) para que el usuario pueda introducir la fecha, la hora y la descripción del nuevo evento o tarea.
Añadir botones para las acciones de "Agregar Evento", "Eliminar Evento Seleccionado" y "Salir".
"""
import tkinter as tk
from tkinter import ttk,messagebox
from datetime import date
import dateutil.utils
from tkcalendar import DateEntry
# crear la v p
root = tk.Tk()
root.title('Contenedores')
root.geometry('1000x500')


# crear contenedor
frame = ttk.Frame(root, padding ="10")
frame.grid(row=0, column=0, columnspan=2,sticky=tk.NSEW)

# agregar funciones
# agregar el evento

def agregar_evento():
    fecha=date_picker.get()
    hora= hora_entry.get()
    descripcion= descripcion_entry.get()

    tree.insert("","end",values=(fecha,hora,descripcion))

# funcion de eliminar evento
def eliminar_evento():
    selected_item =tree.selection()
    if selected_item:
        confirmacion = messagebox.askyesno("Esta seguro de eliminar ","Esta seguro ")

        if confirmacion:
            tree.delete(selected_item)
        else:
            messagebox.showwarning("Seleccione","Seleccione un item")



# crear titulo
titulo = ttk.Label(frame, text="Contenedores")
titulo.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)

# crear etiqueta y el campo de fecha
date_picker= DateEntry(frame, date_patter ='y-mm-dd',width=12)
date_picker.set_date(date.today())
date_picker.grid(row=1,column=0, pady=5)

# campo para hora
hora_label = ttk.Label(frame,text="Ingrese la hora :")
hora_label.grid(row=2,column=0,pady =5)

hora_entry = ttk.Entry(frame)
hora_entry.grid(row=2,column = 1)
# Realizar la descripción
descripcion_label= ttk.Label(frame, text="Descripcion")
descripcion_label.grid(row=3,column=0, pady=5)

descripcion_entry = ttk.Entry(frame)
descripcion_entry.grid(row=3,column = 1)

# creacipon de botones
agregar_boton= ttk.Button(frame,text="Agregar", command=agregar_evento)
agregar_boton.grid(row=4,column=0,pady=5)

#boton de eliminar
eliminar_boton= ttk.Button(frame,text="Eliminar", command=eliminar_evento)
eliminar_boton.grid(row=4,column=1,pady=5)


# # Crear el Treeview para mostrar la lista de eventos
tree = ttk.Treeview(frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.grid(row=5, column=0, columnspan=2, sticky="nsew")

tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción",text="Descripcion")


root.mainloop()



