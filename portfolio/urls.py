from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
    path("proyectos/", views.project_list, name="project_list"),
    path("proyectos/<slug:slug>/", views.project_detail, name="project_detail"),
    path("articulos/", views.article_list, name="article_list"),
    path("articulos/<slug:slug>/", views.article_detail, name="article_detail"),
    path("bibliografia/", views.reference_list, name="reference_list"),
]
