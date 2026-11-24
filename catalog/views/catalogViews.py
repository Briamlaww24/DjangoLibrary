from django.shortcuts import get_object_or_404, render
from django.templatetags.static import static

from catalog.models.bookModel import Book


def searchBook(slug):
    return get_object_or_404(Book, slug=slug)


def list(request):
    return render(request, "catalog/list.html", {"libros": Book.objects.all()})


def token(request, slug):
    return render(request, "catalog/tokens.html", {"libro": searchBook(slug)})


def read(request, slug):
    libro = searchBook(slug)
    return render(request, "catalog/read.html", {
        "libro": libro,
        "pdf_url": static(f"catalog/pdf/{slug}.pdf"),
    })
