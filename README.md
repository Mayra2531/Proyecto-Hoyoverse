# Proyecto Flask - Lista de Hoyoverse

Miniaplicación en Flask para registrar y administrar personajes y armas del universo "Hoyoverse" usando listas de diccionarios en memoria.

## Estructura

- `app.py` → aplicación Flask y rutas de negocio.
- `templates/` → plantillas HTML (base, index, nuevo, ver).
- `static/` → archivos estáticos (principalmente `style.css`).
- `tests/` → scripts de comprobación rápida con el cliente de prueba.
- `requirements.txt` → dependencias mínimas.

## Cómo ejecutar (Windows PowerShell)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Luego abrir http://127.0.0.1:5000 en el navegador.

## Funcionalidad

- Registrar personajes con su nombre, rol, visión y nación.
- Registrar armas con su nombre y rareza.
- Visualizar los registros en tarjetas interactivas.
- Editar o borrar cualquier elemento desde un modal, con confirmaciones y vista previa de cambios antes de enviar el método `PUT` o `DELETE`.

> Nota: Toda la información vive en memoria (listas globales); reiniciar el servidor limpia los datos.
