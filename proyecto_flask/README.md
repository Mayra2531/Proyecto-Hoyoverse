# Proyecto Flask - Lista de Hoyoverse

Miniaplicación en Flask para registrar y ver elementos (registro de personajes y armas del "Hoyoverse") usando listas de diccionarios en memoria.

Estructura:

- app.py -> aplicación Flask
- templates/ -> plantillas HTML (base, index, nuevo, ver)
- static/ -> archivos estáticos (style.css)
- requirements.txt -> dependencias

Cómo ejecutar (Windows PowerShell):

```powershell
python -m venv venv; .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Luego abrir http://127.0.0.1:5000 en el navegador.

Formularios disponibles:
- Registro de Personaje: nombre, rol/visión.
- Registro de Arma: nombre del arma, rareza.


La página ahora incluye una ilustración embebida en el hero que representa el tema Hoyoverse (personajes y armas). No es necesario añadir una imagen externa.
