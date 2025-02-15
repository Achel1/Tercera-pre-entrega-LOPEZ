# Tercera-pre-entrega-LOPEZ
Gamezone
¡Bienvenido a Gamezone! Este proyecto está diseñado para gestionar y explorar información sobre juegos, jugadores, plataformas y personajes en un entorno web. A continuación, encontrarás una guía paso a paso para configurar y usar tu página web.

Usuario de administrador
user:Profe
Contraseña:profe123

Requisitos
Python (versión 3.7 o superior)
Django (versión 5.1 o superior)
Virtualenv (opcional pero recomendado)
Instalación
1. Clonar el Repositorio
Primero, clona el repositorio de GitHub a tu máquina local:

bash
Copiar código
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_DIRECTORIO>
2. Crear un Entorno Virtual
Es una buena práctica usar un entorno virtual para gestionar las dependencias del proyecto:

bash
Copiar código
python -m venv env
Activa el entorno virtual:

En Windows:

bash
Copiar código
env\Scripts\activate
En macOS/Linux:

bash
Copiar código
source env/bin/activate
3. Instalar las Dependencias
Instala las dependencias del proyecto usando pip:

bash
Copiar código
pip install -r requirements.txt
4. Configurar la Base de Datos
Asegúrate de que la base de datos esté configurada correctamente. Luego, realiza las migraciones para crear las tablas necesarias:

bash
Copiar código
python manage.py migrate
5. Crear un Superusuario (Opcional)
Si deseas acceder al panel de administración de Django, crea un superusuario:

bash
Copiar código
python manage.py createsuperuser
6. Ejecutar el Servidor
Inicia el servidor de desarrollo de Django:

bash
Copiar código
python manage.py runserver
Ahora puedes acceder a tu aplicación web en http://127.0.0.1:8000/Gamezone/inicio/

Uso de la Aplicación
1. Crear Nuevos Registros
Juegos: Ve a la página de juegos para agregar nuevos títulos, géneros, etc.
Jugadores: Agrega nuevos jugadores con nombre y nivel.
Personajes: Añade personajes con nombre y descripción.
Plataformas: Registra nuevas plataformas con nombre y fabricante.
2. Buscar Información
Utiliza el formulario de búsqueda en la página de inicio para encontrar información específica sobre juegos, jugadores, plataformas y personajes.

3. Ver Resultados
Los resultados de búsqueda se mostrarán en una página de resultados, donde podrás ver las plataformas, juegos, jugadores y personajes que coinciden con tu consulta.

Estructura de Archivos
gamezone/: Directorio principal del proyecto.
gamezone/settings.py: Configuración del proyecto.
gamezone/urls.py: Configuración de las URLs.
gamezone/views.py: Lógica de la vista para manejar las solicitudes.
gamezone/templates/: Archivos de plantilla HTML para la interfaz de usuario