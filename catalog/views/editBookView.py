from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from catalog.forms.bookCreationForm import BookCreationForm
from catalog.views.bookAccess import get_manageable_book


@login_required
@require_http_methods(["GET", "POST"])
def edit_book(request, slug):
    book = get_manageable_book(request, slug)
    if request.method == "POST":
        form = BookCreationForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("catalog:token", slug=book.slug)
    else:
        form = BookCreationForm(instance=book)
    return render(request, "catalog/createBook.html", {"form": form, "book": book})
