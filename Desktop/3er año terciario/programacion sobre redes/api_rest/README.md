# PFO 2: Sistema de Gestión de Tareas con API (Flask + SQLite)

Este proyecto es la Práctica Formativa Obligatoria 2 de la materia Programación sobre Redes. Consiste en una API REST desarrollada en Python utilizando Flask, con autenticación y persistencia de datos en SQLite, además de un cliente en consola para interactuar con los endpoints.

## Requisitos previos
- Python 3.x instalado.
- Instalar las dependencias ejecutando: `pip install Flask requests`

## Instrucciones para ejecutar el proyecto
1. Abrir una terminal en la carpeta del proyecto.
2. Levantar el servidor ejecutando: `python servidor.py`
3. Se generará automáticamente el archivo `base_datos.db`.
4. Dejar esa terminal abierta. Abrir **otra** terminal nueva.
5. En la nueva terminal, ejecutar el cliente: `python cliente.py`
6. Utilizar el menú interactivo para registrar un usuario, hacer login y consultar las tareas.

## Endpoints de la API
- **POST /registro**: Recibe JSON `{"usuario": "...", "contraseña": "..."}`.
- **POST /login**: Verifica credenciales y devuelve éxito o error.
- **GET /tareas**: Devuelve un HTML de bienvenida.