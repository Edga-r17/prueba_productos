# Proyecto de Gestión de Productos

Este proyecto es una aplicación de gestión de productos construida con Django para el backend y React para el frontend.

### Stack :computer:

El proyecto está construido sobre el siguiente stack tecnológico:

- Python 3.9.0
- Django 4.2.14
- Django REST Framework
- PostgreSQL
- Node.js y npm

### Instalación :tools:

## Backend

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/Edga-r17/Prueba-Full-Stack.git
    ```

2. Entrar al repositorio:
    ```bash
    cd Prueba-Full-Stack
    ```

3. Crear archivo `.env` en la raíz del proyecto con el contenido de las variables globales:
    ```env
    DB_NAME='prueba'
    DB_USER='postgres'
    DB_PASSWORD='postgres'
    DB_HOST='localhost'
    DB_PORT=5432
    DJANGO_SETTINGS_MODULE='prueba.settings'
    ```

4. Crear el ambiente virtual usando [pyenv](https://github.com/pyenv/pyenv#installation).

5. Activar el ambiente virtual:
    ```bash
    pyenv activate <nombre del ambiente creado>
    ```

6. Correr el comando `source .env` para exportar las variables del archivo anterior.

7. Instalar las dependencias del proyecto:
    ```bash
    pip install -r requirements.txt
    ```

8. Crear la base de datos en PostgreSQL:

    1. Iniciar sesión en PostgreSQL:
        ```bash
        sudo -u postgres psql
        ```
    2. Crear la base de datos y el usuario:
        ```sql
        CREATE DATABASE prueba;
        ```

9. Aplicar las migraciones y ejecutar el servidor:
    ```bash
    python manage.py migrate
    python manage.py runserver 8006
    ```

El servidor de desarrollo estará disponible en [http://localhost:8006/](http://localhost:8006/).

## Frontend

1. Navegar al directorio del frontend e instalar las dependencias:
    ```bash
    cd frontend
    npm install
    ```

2. Levantar el proyecto:
    ```bash
    npm start
    ```

El servidor de desarrollo estará disponible en [http://localhost:3000/](http://localhost:3000/).

## Uso

- Visita [http://localhost:3000/](http://localhost:3000/) en tu navegador para interactuar con la aplicación.
- Puedes listar, añadir, editar y eliminar productos usando la interfaz de usuario.


 