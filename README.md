Lo primero que debemos hacer es crear un entorno virtual. Este comando crea un entorno virtual de Python llamado .venv en el directorio actual:

```bash
python3 -m venv .venv
```
Luego, activamos el entorno virtual:
```
source .venv/bin/activate
```
Ahora, instalamos las dependencias necesarias. Este comando instala todas las bibliotecas que están listadas en el archivo requirements.txt:

```
pip install -r requirements.txt
```

Finalmente, corremos el script para ejecutar el programa:

```
python test_openair_api.py
```
Cuando el Token expira, hay que correr el script de abajo y en la pestaña que se 7050007 Blend360 LLC, eso refreshea el token

```
python oauth2_openair.py
```


