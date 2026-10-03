from django.db import models
from django.urls import reverse


class Project(models.Model):
    """Un proyecto contado como historia. Los campos de texto aceptan Markdown."""

    title = models.CharField("título", max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.CharField(
        "resumen", max_length=300, blank=True,
        help_text="Una o dos líneas para el listado de proyectos.",
    )
    context = models.TextField("introducción / contexto", blank=True)
    problem = models.TextField("problema", blank=True)
    process = models.TextField("proceso", blank=True)
    decisions = models.TextField("decisiones", blank=True)
    implementation = models.TextField("implementación", blank=True)
    result = models.TextField("resultado", blank=True)

    published = models.BooleanField("publicado", default=False)
    order = models.PositiveIntegerField("orden", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolio:project_detail", args=[self.slug])

    def sections(self):
        """Secciones narrativas en orden, omitiendo las vacías."""
        fields = ["context", "problem", "process", "decisions", "implementation", "result"]
        return [
            (self._meta.get_field(name).verbose_name.capitalize(), getattr(self, name))
            for name in fields
            if getattr(self, name).strip()
        ]


class Resource(models.Model):
    """Enlace a evidencia externa: el artefacto pesado vive fuera de Django."""

    class Kind(models.TextChoices):
        GITHUB = "github", "GitHub"
        NOTEBOOK = "notebook", "Notebook"
        DASHBOARD = "dashboard", "Dashboard"
        PDF = "pdf", "PDF"
        DATA = "data", "Datos"
        DOCS = "docs", "Documentación"
        OTHER = "other", "Otro"

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="resources")
    kind = models.CharField("tipo", max_length=20, choices=Kind.choices)
    label = models.CharField("texto del enlace", max_length=200, blank=True)
    url = models.URLField("URL", max_length=500)
    order = models.PositiveIntegerField("orden", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "recurso externo"
        verbose_name_plural = "recursos externos"

    def __str__(self):
        return self.label or self.get_kind_display()


class Article(models.Model):
    """Artículo de blog. El cuerpo acepta Markdown."""

    title = models.CharField("título", max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.CharField("resumen", max_length=300, blank=True)
    body = models.TextField("contenido", blank=True)

    published = models.BooleanField("publicado", default=False)
    published_at = models.DateField("fecha de publicación", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-published_at", "-created_at"]
        verbose_name = "artículo"
        verbose_name_plural = "artículos"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolio:article_detail", args=[self.slug])
