# Task Manager MVC Python

Una aplicación simple de gestión de tareas implementada en Python utilizando el patrón de diseño MVC (Modelo-Vista-Controlador). La aplicación permite crear, completar y eliminar tareas a través de una interfaz web.

## Características

- Interfaz web moderna y responsive
- Crear nuevas tareas
- Marcar tareas como completadas
- Eliminar tareas
- Actualizaciones en tiempo real con mensajes de estado

## Requisitos

- Docker
- Docker Compose

## Estructura del Proyecto

```
mvc_python/
├── app/
│   ├── controllers/
│   │   └── task.py
│   ├── models/
│   │   └── task.py
│   └── views/
│       └── task.py
├── server.py
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Patrón MVC

- **Modelo** (`app/models/task.py`): Maneja la lógica de negocio y el almacenamiento de las tareas
- **Vista** (`app/views/task.py`): Genera la interfaz de usuario en HTML
- **Controlador** (`app/controllers/task.py`): Coordina las interacciones entre el modelo y la vista

## Iniciar la Aplicación

1. Clona el repositorio:
   ```bash
   git clone git@github.com:illuminaki/mvc_python_basic.git
   cd mvc_python
   ```

2. Construye y ejecuta los contenedores con Docker Compose:
   ```bash
   docker-compose up --build
   ```

3. Accede a la aplicación en tu navegador:
   ```
   http://localhost:8000
   ```

## Desarrollo

Para desarrollar nuevas características:

1. La aplicación se monta en un volumen de Docker, por lo que los cambios en el código se reflejan automáticamente
2. Si realizas cambios en las dependencias, necesitarás reconstruir la imagen:
   ```bash
   docker-compose up --build
   ```

## Detener la Aplicación

Para detener la aplicación:

```bash
docker-compose down
```
