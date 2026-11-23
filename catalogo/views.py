from django.http import Http404
from django.shortcuts import render
from django.templatetags.static import static

from catalogo.muestras import LIBROS


def buscar_libro(slug):
    try:
        return LIBROS[slug]
    except KeyError as error:
        raise Http404("Libro no encontrado") from error


def lista(request):
    return render(request, "catalogo/lista.html", {"libros": LIBROS.values()})


def ficha(request, slug):
    return render(request, "catalogo/ficha.html", {"libro": buscar_libro(slug)})


def leer(request, slug):
    libro = buscar_libro(slug)
    return render(request, "catalogo/leer.html", {
        "libro": libro,
        "pdf_url": static(f"catalogo/pdf/{slug}.pdf"),
    })
