# Controlador que maneja las interacciones entre el modelo y la vista
class TaskController:
    def __init__(self, model, view):
        # Inicializa el controlador con las instancias del modelo y la vista
        self.model = model
        self.view = view

    def index(self, message=None):
        # Muestra la lista completa de tareas en la vista principal
        tasks = self.model.all()
        return self.view.index(tasks, message)

    def show(self, task_id):
        # Muestra el detalle de una tarea específica
        task = self.model.find(task_id)
        self.view.show(task)

    def create(self, name):
        # Crea una nueva tarea y muestra un mensaje de confirmación
        task = self.model.create(name)
        return "/"
    def update(self, task_id, name):
        # Actualiza el nombre de una tarea y muestra el resultado
        task = self.model.update(task_id, name)
        if task:
            return "/"
        return "/"

    def delete(self, task_id):
        # Elimina una tarea y muestra un mensaje de confirmación
        if self.model.delete(task_id):
            return "/"
        return "/"

    def complete(self, task_id):
        # Marca una tarea como completada y muestra el resultado
        task = self.model.complete(task_id)
        if task:
            return "/"
        return "/"