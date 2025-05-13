Este README describe los pasos necesarios para conectarse a la API REST de OpenAir.

OpenAir es una plataforma de gestión de servicios profesionales desarrollada por NetSuite, que permite a las organizaciones planificar, gestionar y facturar proyectos y recursos. Para integrar una aplicación con la API, es necesario crear una aplicación en OpenAir. Una vez creada, la aplicación proporciona dos tipos de tokens:

Access Token, con una duración de 15 minutos, utilizado para autenticar las solicitudes a la API.

Refresh Token, con una duración de 1 día, que permite obtener nuevos Access Tokens sin intervención del usuario.

Si el Refresh Token expira (después de 24 horas sin renovación) o se revoca, será necesario volver a autenticar y autorizar la aplicación, tal como se indica en el paso llamado "Refrescar el token Oauth2".

# Manual de uso:

### Creación un entorno virtual:

Creamos un entorno virtual de Python llamado .venv en el directorio actual:
```bash
python3 -m venv .venv
```
### Activación del entorno virtual

```
source .venv/bin/activate
```
### Instalación de las dependencias:

Este comando instalará todas las bibliotecas listadas en el archivo requirements.txt:
```
pip install -r requirements.txt
```

### Prueba conexión al endpoint de usuarios:

Ejecutamos el siguiente script para conectarnos al endpoint /users de la API REST de OpenAir. Este script obtiene todos los usuarios de OpenAir, y crea una tabla llamada users_summary con las columnas id,firstName,lastName y email.
```
python users.py
```
### Obtención de los time entries de proyectos billable:

Este script primero consulta el endpoint /project-tasks para identificar los proyectos billables, es decir, facturables a clientes.
Luego, se conecta al endpoint /time-entries para obtener las cargas de horas en OpenAir, pero solo de los proyectos billables, dentro de un rango de fechas especificado.
Los datos se guardan en una tabla llamada billable_hours_summary, con las siguientes columnas: userId, total_billable_hours, start_date y end_date.

```
python time_entries.py
```
### Refrescar el token OAuth2:

Cuando el token expira, ejecutamos el siguiente script dentro de la carpeta access_openair. En el navegador, selecciona la cuenta correspondiente a 7050007 Blend360 LLC para refrescar el token:
```
python oauth2_openair.py
```

### Para correr tests pytests:
Parados en main ejecutamos:
```
PYTHONPATH=. pytest tests/
```
