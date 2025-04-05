class TaskView:
    def index(self, tasks, message=None):
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Task Manager</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    line-height: 1.6;
                    color: #333;
                }}
                h1 {{
                    color: #2c3e50;
                    border-bottom: 2px solid #eee;
                    padding-bottom: 10px;
                }}
                ul {{
                    list-style-type: none;
                    padding: 0;
                }}
                li {{
                    margin: 10px 0;
                    padding: 15px;
                    background: #f8f9fa;
                    border-radius: 5px;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                }}
                .task-info {{
                    flex-grow: 1;
                }}
                .task-actions a {{
                    margin-left: 10px;
                    padding: 5px 10px;
                    text-decoration: none;
                    border-radius: 3px;
                    font-size: 0.9em;
                }}
                .complete-btn {{
                    background-color: #28a745;
                    color: white;
                }}
                .delete-btn {{
                    background-color: #dc3545;
                    color: white;
                }}
                form {{
                    margin-top: 30px;
                    background: #f8f9fa;
                    padding: 20px;
                    border-radius: 5px;
                }}
                input {{
                    padding: 10px;
                    width: 100%;
                    box-sizing: border-box;
                    margin-bottom: 10px;
                    border: 1px solid #ddd;
                    border-radius: 3px;
                }}
                button {{
                    padding: 10px 20px;
                    background: #007bff;
                    color: white;
                    border: none;
                    border-radius: 3px;
                    cursor: pointer;
                    font-size: 1em;
                }}
                button:hover {{
                    background: #0069d9;
                }}
                .message {{
                    padding: 10px;
                    margin: 20px 0;
                    border-radius: 3px;
                }}
                .success {{
                    background-color: #d4edda;
                    color: #155724;
                }}
                .error {{
                    background-color: #f8d7da;
                    color: #721c24;
                }}
            </style>
        </head>
        <body>
            <h1>Task Manager</h1>
            {f'<div class="message success">{message}</div>' if message else ''}
            <ul>
        """
        
        for task in tasks:
            status = "✓" if task.completed else "✗"
            status_class = "completed" if task.completed else "pending"
            html += f"""
            <li class="{status_class}">
                <div class="task-info">
                    <span class="status">{status}</span>
                    <span class="task-id">{task.id}:</span>
                    <span class="task-name">{task.name}</span>
                </div>
                <div class="task-actions">
                    <a href="/complete/{task.id}" class="complete-btn">{"Reabrir" if task.completed else "Completar"}</a>
                    <a href="/delete/{task.id}" class="delete-btn">Eliminar</a>
                </div>
            </li>
            """
        
        html += """
            </ul>
            
            <form action="/create" method="post">
                <h2>Añadir Nueva Tarea</h2>
                <input type="text" name="name" required placeholder="¿Qué necesitas hacer?" autofocus>
                <button type="submit">Agregar Tarea</button>
            </form>
        </body>
        </html>
        """
        return html

    def show(self, task):
        if task:
            status = "✓" if task.completed else "✗"
            return f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Detalle de Tarea</title>
                <meta charset="UTF-8">
                <link rel="stylesheet" href="/static/style.css">
            </head>
            <body>
                <h1>Detalle de Tarea</h1>
                <div class="task-detail">
                    <p><strong>ID:</strong> {task.id}</p>
                    <p><strong>Nombre:</strong> {task.name}</p>
                    <p><strong>Estado:</strong> [{status}]</p>
                </div>
                <a href="/">Volver al listado</a>
            </body>
            </html>
            """
        return self.error_message("Tarea no encontrada")

    def error_message(self, text):
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Error</title>
            <meta charset="UTF-8">
        </head>
        <body>
            <div class="message error">{text}</div>
            <a href="/">Volver al listado</a>
        </body>
        </html>
        """