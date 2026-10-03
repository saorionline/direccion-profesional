import markdown as md
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def markdown(text):
    """Convierte Markdown a HTML. El contenido es confiable: solo se escribe desde el admin."""
    return mark_safe(md.markdown(text or "", extensions=["extra", "sane_lists"]))
