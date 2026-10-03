# Portafolio

Django organiza y presenta la historia. Los sistemas externos (GitHub, notebooks,
dashboards, PDFs, datos) contienen la evidencia y los artefactos pesados.

## Estructura

```
config/                  Configuración del proyecto Django
portfolio/
  models.py              Project, Resource (recursos externos), Article
  admin.py               Donde se escribe el contenido
  views.py / urls.py     Páginas públicas
  templatetags/          Filtro |markdown
templates/               Plantillas HTML
static/css/main.css      Estilos
```

Cada **proyecto** se cuenta en secciones (todas en Markdown, las vacías no se muestran):
contexto → problema → proceso → decisiones → implementación → resultado,
más una lista de **recursos externos** enlazados.

## Uso

```bash
py -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python manage.py migrate
.venv\Scripts\python manage.py createsuperuser
.venv\Scripts\python manage.py runserver
```

- Escribir contenido: http://127.0.0.1:8000/admin/
- Ver el sitio: http://127.0.0.1:8000/

Solo se muestra en el sitio lo que tenga marcado **publicado**.
