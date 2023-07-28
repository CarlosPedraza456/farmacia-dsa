# Farmacia. Guia de descarga y ejecución

## Requisitos Previos

Antes de ejecutar este proyecto, asegúrate de tener instalado lo siguiente:

-Sistema operativo: Windows 7 a 10, con 2GB RAM (4GB preferiblemente)
-Python: 3.11.4 o más reciente
-Django 4.2 o más reciente
-pip (intalador de paquetes de python) 
- Git

## Instalación Python
1. Ve al sitio web oficial de Python: https://www.python.org/
2. Descarga la última versión estable de Python para tu sistema operativo.
3. Ejecuta el instalador y sigue las instrucciones del asistente de instalación.
4. Asegúrate de marcar la opción "Agregar Python x.x a PATH" durante la instalación para que Python sea accesible desde la línea de comandos.
5. Asegurate de activar la casilla que instala PIP (package installer for Python)

## Instalación proyecto

Abrimos la terminal de nuestra preferencia

1. Clona el repositorio:

   ```bash
   git clone https://github.com/CarlosPedraza456/farmacia-dsa

2. Ejecutamos el comando para irnos a la carpeta de nuesro proyecto clonado
    cd farmacia-dsa
3. Crea un entorno virtual (opcional, pero se recomienda):
    python -m venv venv
4. Activar el entorno virtual (Windows):
    venv\Scripts\activate
4.1 En caso de estar usando un PowerShell usar el siguiente comando antes de activar el entorno virtual
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
5. Instala las dependencias del proyecto usando pip:
    pip install -r requirements.txt

 ## Ejecucion del sistema
 1. Ejecutamos los siguientes comandos para aplicar las migraciones a la base de datos:
     python manage.py makemigrations
     python manage.py migrate
 2. Crea un superusuario (para acceder al panel de administración de Django):
    python manage.py createsuperuser
 3. Ejecuta el servidor de desarrollo:
    python manage.py runserver
 4. Abre tu navegador web y visita http://127.0.0.1:8000/ para ver la aplicación en ejecución.
 5. Para acceder al panel de administración de Django, visita http://127.0.0.1:8000/admin/ e ingresa las credenciales del superusuario que creaste en el paso 2.


