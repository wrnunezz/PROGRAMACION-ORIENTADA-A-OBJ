"""
Utilizar Tkinter para crear la interfaz de usuario.
Implementar un campo de entrada (Entry) para añadir nuevas tareas.
Incluir botones para añadir tareas, marcar como completadas, y eliminar tareas.
Mostrar las tareas en una lista o algún componente adecuado.
Manejo de Eventos de Clic:

Asignar funciones que se ejecutarán cuando los usuarios interactúen con los botones.
Atajos de Teclado:

Permitir añadir una nueva tarea presionando la tecla "Enter" después de escribir en el campo de entrada.
Implementar un atajo de teclado para marcar la tarea seleccionada como completada (por ejemplo, tecla "C").
Implementar un atajo de teclado para eliminar la tarea seleccionada (por ejemplo, tecla "Delete" o "D").
Permitir cerrar la aplicación usando la tecla "Escape".

"""
import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("500x500")

        # Lista de tareas
        self.tasks = []

        # Campo de entrada
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        # Lista de tareas (Listbox)
        self.task_listbox = tk.Listbox(self.root, height=15, width=50)
        self.task_listbox.pack(pady=10)

        # Botones
        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=10)

        self.complete_button = tk.Button(self.root, text="Completar Tarea", command=self.complete_task)
        self.complete_button.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Eliminar Tarea")
        self.delete_button.pack(pady=10)

        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())  # Enter para añadir tarea
        self.root.bind("<C>", lambda event: self.complete_task())  # "C" para completar tarea
        self.root.bind("<D>", lambda event: self.delete_task())    # "D" para eliminar tarea
        self.root.bind("<Delete>", lambda event: self.delete_task())  # Tecla Delete para eliminar tarea
        self.root.bind("<Escape>", lambda event: self.root.quit())  # Escape para salir

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada después de añadir
        else:
            messagebox.showerror("Error", "No se encuentra una tarea.")

    def complete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks[index]["completed"] = True
            self.update_task_listbox()
        else:
            messagebox.showerror("Error", "No se encuentra una tarea seleccionada.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        # Añadir tareas a la lista
        for task in self.tasks:
            display_task = task["task"]
            if task["completed"]:
                display_task += "  (completada)"
            self.task_listbox.insert(tk.END, display_task)

    def delete_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_task_listbox()
        else:
            messagebox.showwarning("Advertencia", "No hay tarea seleccionada para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
