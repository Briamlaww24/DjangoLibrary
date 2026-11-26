from pathlib import Path

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
from django.db.models.deletion import ProtectedError
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.http import require_http_methods

from catalog.forms import BookCreationForm
from catalog.models import Book
from catalog.roles import isCatalogAdmin


def getManageableBook(request, slug):
    books = Book.objects.all()
    if not isCatalogAdmin(request.user):
        books = books.filter(owner=request.user)
    return get_object_or_404(books, slug=slug)


@never_cache
@login_required
@permission_required("catalog.view_book", raise_exception=True)
def bookList(request):
    return render(request, "catalog/books/list.html", {"libros": Book.objects.all()})


@never_cache
@login_required
@permission_required("catalog.view_book", raise_exception=True)
def bookDetail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "catalog/books/tokens.html", {
        "libro": book,
        "puedeGestionar": book.owner_id == request.user.pk or isCatalogAdmin(request.user),
    })


@never_cache
@login_required
@permission_required("catalog.view_book", raise_exception=True)
def bookRead(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "catalog/books/read.html", {
        "libro": book,
        "pdfUrl": reverse("catalog:book_pdf", args=[book.slug]),
    })


@never_cache
@login_required
@permission_required("catalog.view_book", raise_exception=True)
@require_http_methods(["GET", "HEAD"])
@xframe_options_sameorigin
def bookPdf(request, slug):
    book = get_object_or_404(Book, slug=slug)
    try:
        if book.pdf:
            document = book.pdf.open("rb")
        else:
            document = (Path(settings.BASE_DIR) / "catalog" / "assets" / "pdf" / f"{book.slug}.pdf").open("rb")
    except FileNotFoundError as error:
        raise Http404("PDF no encontrado") from error
    return FileResponse(document, content_type="application/pdf", filename=f"{book.slug}.pdf")


@never_cache
@login_required
@permission_required("catalog.add_book", raise_exception=True)
@require_http_methods(["GET", "POST"])
def createBook(request):
    form = BookCreationForm(request.POST, request.FILES) if request.method == "POST" else BookCreationForm()
    if request.method == "POST" and form.is_valid():
        book = form.save(commit=False)
        book.owner = request.user
        with transaction.atomic():
            book.save()
            form.save_m2m()
        messages.success(request, "Libro publicado exitosamente.")
        return redirect(book)
    return render(request, "catalog/books/createBook.html", {"form": form})


@never_cache
@login_required
@permission_required("catalog.change_book", raise_exception=True)
@require_http_methods(["GET", "POST"])
def editBook(request, slug):
    book = getManageableBook(request, slug)
    if request.method == "POST":
        form = BookCreationForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro actualizado exitosamente.")
            return redirect(book)
    else:
        form = BookCreationForm(instance=book)
    return render(request, "catalog/books/createBook.html", {"form": form, "book": book})


@never_cache
@login_required
@permission_required("catalog.delete_book", raise_exception=True)
@require_http_methods(["GET", "POST"])
def deleteBook(request, slug):
    book = getManageableBook(request, slug)
    if request.method == "POST":
        try:
            book.delete()
        except ProtectedError:
            messages.error(request, "El libro tiene préstamos registrados y no se puede borrar.")
            return redirect(book)
        messages.success(request, "Libro eliminado exitosamente.")
        return redirect("catalog:list")
    return render(request, "catalog/books/deleteBook.html", {"book": book})
