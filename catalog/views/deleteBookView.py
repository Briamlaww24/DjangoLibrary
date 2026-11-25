from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from catalog.views.bookAccess import get_manageable_book


@login_required
@require_http_methods(["GET", "POST"])
def delete_book(request, slug):
    book = get_manageable_book(request, slug)
    if request.method == "POST":
        book.delete()
        return redirect("catalog:list")
    return render(request, "catalog/deleteBook.html", {"book": book})
