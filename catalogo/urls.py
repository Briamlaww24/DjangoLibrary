from django.urls import path

from . import views

app_name = "catalogo"

urlpatterns = [
    path("", views.lista, name="lista"),
    path("<slug:slug>/", views.ficha, name="ficha"),
    path("<slug:slug>/leer/", views.leer, name="leer"),
]
