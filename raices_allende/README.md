# Raíces Allende — Proyecto Django

Tu página web convertida a un proyecto de Django (Python).

## Qué cambió
- El HTML ahora son **plantillas** dentro de `principal/templates/principal/`.
- `base.html` tiene el diseño común (encabezado, menú, estilos, pie de página).
- Cada página (`index.html`, `historia.html`, etc.) extiende de `base.html`.
- Los enlaces ya no son `A2.html`, sino rutas de Django: `{% url 'principal:historia' %}`.
- Las vistas están en `principal/views.py` y las direcciones en `principal/urls.py`.

## Cómo ejecutarlo (pasos)

1. Instala Python (si no lo tienes).
2. Abre una terminal en la carpeta `raices_allende/` (la que contiene `manage.py`).
3. Instala Django:
   ```
   pip install -r requirements.txt
   ```
4. Crea la base de datos (solo la primera vez):
   ```
   python manage.py migrate
   ```
5. Enciende el servidor:
   ```
   python manage.py runserver
   ```
6. Abre en tu navegador: **http://127.0.0.1:8000/**

## Estructura de carpetas
```
raices_allende/
├── manage.py                  (comandos de Django)
├── requirements.txt
├── raices_allende/            (configuración del proyecto)
│   ├── settings.py            (config general)
│   └── urls.py
└── principal/                 (tu app: las páginas del sitio)
    ├── views.py               (una función por página)
    ├── urls.py                (direcciones del sitio)
    ├── models.py              (para la base de datos, después)
    └── templates/principal/   (tus archivos HTML)
        ├── base.html          (diseño común)
        ├── index.html         (página principal)
        ├── historia.html      (antes A2.html)
        ├── tradiciones.html   (antes A3.html)
        ├── lugares.html       (antes A4.html)
        ├── gastronomia.html   (antes A5.html)
        ├── artesanias.html    (antes A6.html)
        └── contacto.html      (antes A7.html)
```

## Para editar el contenido
Solo modifica los archivos `.html` dentro de `templates/principal/`.
El texto, imágenes y enlaces se editan igual que en HTML normal.
