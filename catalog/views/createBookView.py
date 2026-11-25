from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from catalog.forms.bookCreationForm import BookCreationForm

@login_required
def createBook(request):
    if request.method == 'POST':
        form = BookCreationForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('catalog:token', slug=book.slug)
    else:
        form = BookCreationForm()

    return render(request, 'catalog/createBook.html', {'form': form})
