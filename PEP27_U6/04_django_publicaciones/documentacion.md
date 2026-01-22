# USAR ENOTORNO VIRTUAL + DJANGO

Primero creamos un entorno virtual con F1 (terminal VS)
Python create enviroment > venv > interprete
Luego python select interprete > interprete venv

En terminal
1. Instalamos Django `pip install django~=5.0.0`
2. Usamos `django-admin startproject django_proyecto .`
    La explciación es `django-admin startproject <nombre(ubicación)`
    Esta es la carpeta de apoyo a la hora de crear nuestro proyecot
3. Arrancamos un servidor con `python manage.py runserver <puerto>`
    Por defecto es el 8000 si no se indica
4. `python manage.py migrate` crea tablas e inserts en la db
    Instalamos la extensión de SQLite Viewer para ver la info de la base de datos.

5. Creamos una aplicacion con `python manage.py startapp <nombre>`
    Y de esta forma se crea una carpeta con el nombre del proyecto y sus configuracioens
6. Nos vamos a django proyecto > settings.py > buscamos el array INSTALLED_APPS y ponemos el nombre de la aplicación que es `paginas` o `empresa`