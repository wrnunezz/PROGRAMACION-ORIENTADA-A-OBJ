"""
Utilizar Tkinter para crear la interfaz de usuario.
La aplicación debe tener un campo de entrada (Entry) para escribir nuevas tareas.
Incluir botones para "Añadir Tarea", "Marcar como Completada" y "Eliminar Tarea".
Mostrar las tareas actuales en un componente de lista (p. ej., Listbox o Treeview).
Manejo de Eventos:

Implementar manejadores de eventos para los botones y la entrada de texto.
Permitir la adición de tareas presionando la tecla Enter después de escribir una tarea.
Opcional: Implementar eventos adicionales de tu elección para mejorar la funcionalidad (p. ej., doble clic en una tarea para marcarla como completada).
"""
import tkinter as tk
from tkinter import messagebox


class TaskManager:
    def __init__(self,root):
        self.root = root
        self.root.title("Gesto de Tareas ")

        # LISTA DE TAREAS
        self.tasks=[]

        # campo de entrada
        self.entry = tk.Entry(root,width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>",self.add_task)
        # BOTONES
        self.add_button= tk.Button(root,text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady =5)

        self.complete_button = tk.Button(root,text="Marcar como Completada")
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root,text="Eliminar Tarea")
        self.delete_button.pack(pady=5)

        # lista de Tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=5)

    def add_task(self,event=None):
        task = self.entry.get().strip()
        if task:
            self.tasks.append(task)
            # llamar a mi componente
            self.update_task_listbox()
            self.entry.delete(0,tk.END)
        else:
            messagebox.showwarning("Advertencia","No se puede agregar un tarea vacia ")

    def update_task_listbox(self):
        self.task_listbox.delete(0,tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END,task)

if __name__ == "__main__":
    root = tk.Tk()
    app= TaskManager(root)
    root.mainloop()