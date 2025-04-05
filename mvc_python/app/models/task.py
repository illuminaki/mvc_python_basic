# Clase que representa una tarea individual en el sistema
class Task:
    def __init__(self, id, name, completed=False):
        # Inicializa una nueva tarea con un ID único, nombre y estado de completado
        self.id = id
        self.name = name
        self.completed = completed

# Modelo que maneja la lógica de negocio y almacenamiento de las tareas
class TaskModel:
    def __init__(self):
        # Inicializa la lista de tareas y el contador de IDs
        self.tasks = []
        self.next_id = 1

    def create(self, name):
        # Crea una nueva tarea con el nombre proporcionado y un ID único
        task = Task(self.next_id, name)
        self.tasks.append(task)
        self.next_id += 1
        return task

    def all(self):
        # Retorna la lista completa de tareas
        return self.tasks

    def find(self, task_id):
        # Busca una tarea por su ID y la retorna, o None si no existe
        return next((task for task in self.tasks if task.id == task_id), None)

    def update(self, task_id, name):
        # Actualiza el nombre de una tarea existente
        task = self.find(task_id)
        if task:
            task.name = name
            return task
        return None

    def delete(self, task_id):
        # Elimina una tarea de la lista por su ID
        task = self.find(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def complete(self, task_id):
        # Marca una tarea como completada
        task = self.find(task_id)
        if task:
            task.completed = True
            return task
        return None