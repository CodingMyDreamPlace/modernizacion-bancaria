**Modernización Bancaria**
Este proyecto es una aplicación web para la gestión de clientes, construida con Flask y SQLite y empaquetada con Docker. La aplicación permite realizar operaciones CRUD (crear, leer, actualizar y eliminar) sobre los registros de clientes.

**Requisitos**
Asegúrate de tener instalados los siguientes programas en tu máquina:
Docker
Docker Compose

**Instalación y Ejecución**
Sigue estos pasos para clonar el repositorio, construir la imagen Docker y ejecutar la aplicación:

**1) Clona este repositorio:**
git clone https://github.com/CodingMyDreamPlace/modernizacion-bancaria.git


cd modernizacion-bancaria

**2) Construye la imagen Docker:**
docker build -t modernizacion-bancaria .

**3) Accede a la aplicación:**
Abre tu navegador web y ve a http://localhost:5000 para acceder a la aplicación.

**Base de Datos**
El proyecto incluye una base de datos SQLite (database.db) ya poblada con datos de ejemplo. Si deseas utilizar una base de datos nueva, puedes eliminar database.db y ejecutar los scripts SQL proporcionados para crear una base de datos nueva.
