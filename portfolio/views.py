from django.shortcuts import get_object_or_404, render

from .models import Article, Project


def home(request):
    return render(request, "portfolio/home.html", {
        "projects": Project.objects.filter(published=True)[:3],
        "articles": Article.objects.filter(published=True)[:3],
    })


def project_list(request):
    return render(request, "portfolio/project_list.html", {
        "projects": Project.objects.filter(published=True),
    })


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, published=True)
    return render(request, "portfolio/project_detail.html", {"project": project})


def article_list(request):
    return render(request, "portfolio/article_list.html", {
        "articles": Article.objects.filter(published=True),
    })


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, published=True)
    return render(request, "portfolio/article_detail.html", {"article": article})
