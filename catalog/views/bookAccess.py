from django.shortcuts import get_object_or_404

from catalog.models.bookModel import Book


def get_manageable_book(request, slug):
    books = Book.objects.all()
    if not request.user.is_superuser:
        books = books.filter(owner=request.user)
    return get_object_or_404(books, slug=slug)
