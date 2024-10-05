import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("600x400")

# Crear un contenedor principal
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="nsew")

# Etiqueta de título
titulo = ttk.Label(frame, text="Tareas Programadas", font=("Arial", 16))
titulo.grid(row=0, column=0, pady=10)

# Crear el Treeview
tree = ttk.Treeview(frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.grid(row=1, column=0, sticky="nsew")

# Definir los encabezados de columna
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")

# Ajustar el ancho de las columnas
tree.column("Fecha", width=100)
tree.column("Hora", width=100)
tree.column("Descripción", width=300)

# Datos de ejemplo
eventos = [
    ("2024-09-18", "10:00", "Reunión con el equipo de desarrollo"),
    ("2024-09-19", "14:30", "Revisión del proyecto"),
    ("2024-09-20", "09:00", "Presentación a clientes"),
]

# Insertar los eventos en el Treeview
for evento in eventos:
    tree.insert("", "end", values=evento)

# Crear scrollbars
scrollbar_vertical = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
scrollbar_vertical.grid(row=1, column=1, sticky="ns")
tree.configure(yscroll=scrollbar_vertical.set)

scrollbar_horizontal = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
scrollbar_horizontal.grid(row=2, column=0, sticky="ew")
tree.configure(xscroll=scrollbar_horizontal.set)

# Configuración para expandir el Treeview con la ventana
frame.rowconfigure(1, weight=1)
frame.columnconfigure(0, weight=1)

# Ejecutar la ventana
root.mainloop()
