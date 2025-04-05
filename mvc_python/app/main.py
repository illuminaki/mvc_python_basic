from models.task import TaskModel
from views.task import TaskView
from controllers.task import TaskController

def main():
    model = TaskModel()
    view = TaskView()
    controller = TaskController(model, view)

    # Ejemplo de "rutas" simuladas
    print("=== Creando tareas ===")
    controller.create("Comprar leche")
    controller.create("Estudiar Python")

    print("\n=== Listando tareas ===")
    controller.index()

    print("\n=== Mostrando tarea 1 ===")
    controller.show(1)

    print("\n=== Actualizando tarea 1 ===")
    controller.update(1, "Comprar pan")

    print("\n=== Completando tarea 1 ===")
    controller.complete(1)

    print("\n=== Listando tareas actualizadas ===")
    controller.index()

    print("\n=== Eliminando tarea 2 ===")
    controller.delete(2)

    print("\n=== Listando tareas finales ===")
    controller.index()

if __name__ == "__main__":
    main()