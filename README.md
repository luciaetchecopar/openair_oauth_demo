1. Crear un entorno virtual

Primero, creamos un entorno virtual de Python llamado .venv en el directorio actual:
```bash
python3 -m venv .venv
```
2. Activar el entorno virtual

```
source .venv/bin/activate
```
3. Instalar las dependencias

Este comando instalará todas las bibliotecas listadas en el archivo requirements.txt:
```
pip install -r requirements.txt
```

4. Probar la conexión al endpoint de usuarios

Ejecutamos el siguiente script para conectarnos al endpoint /users de la API REST de OpenAir:
```
python test_users.py
```
5. Obtener los time entries de proyectos billables

Este script primero consulta el endpoint /project-tasks para identificar los proyectos billables. Luego, se conecta al endpoint /time-entries y filtra los resultados por estos proyectos:

```
python test_time_entries.py
```
6. Refrescar el token OAuth2

Cuando el token expira, ejecutamos el siguiente script. En el navegador, selecciona la cuenta correspondiente a 7050007 Blend360 LLC para refrescar el token:
```
python oauth2_openair.py
```


