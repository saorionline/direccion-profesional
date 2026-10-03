from django.contrib import admin

from .models import Article, Project, Resource


class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "published", "order", "updated_at"]
    list_editable = ["published", "order"]
    search_fields = ["title", "summary"]
    prepopulated_fields = {"slug": ["title"]}
    inlines = [ResourceInline]
    fieldsets = [
        (None, {"fields": ["title", "slug", "summary", "published", "order"]}),
        ("Historia (Markdown)", {
            "fields": ["context", "problem", "process", "decisions", "implementation", "result"],
        }),
    ]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "published", "published_at", "updated_at"]
    list_editable = ["published"]
    search_fields = ["title", "summary", "body"]
    prepopulated_fields = {"slug": ["title"]}
