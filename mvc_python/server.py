from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
from app.controllers.task import TaskController
from app.models.task import TaskModel
from app.views.task import TaskView

model = TaskModel()
view = TaskView()
controller = TaskController(model, view)

# Variable global para almacenar mensajes temporales
message = None

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global message
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == '/':
            tasks = model.all()
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            response = view.index(tasks, message)
            message = None  # Limpiar el mensaje después de mostrarlo
            self.wfile.write(response.encode('utf-8'))

        elif path.startswith('/complete/'):
            task_id = int(path.split('/')[-1])
            task = model.find(task_id)
            if task:
                controller.complete(task_id)
                message = f"Tarea completada: {task.name}"
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()

        elif path.startswith('/delete/'):
            task_id = int(path.split('/')[-1])
            task = model.find(task_id)
            if task:
                task_name = task.name
                controller.delete(task_id)
                message = f"Tarea eliminada: {task_name}"
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
        
        elif path.startswith('/show/'):
            task_id = int(path.split('/')[-1])
            task = model.find(task_id)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(view.show(task).encode())

    def do_POST(self):
        global message
        if self.path == '/create':
            content_length = int(self.headers['Content-Length'])
            post_data = parse_qs(self.rfile.read(content_length).decode())
            task_name = post_data['name'][0]
            controller.create(task_name)
            message = f"Tarea creada: {task_name}"
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Servidor iniciado en http://localhost:8000")
    httpd.serve_forever()

if __name__ == "__main__":
    run()