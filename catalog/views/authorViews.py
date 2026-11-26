from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import never_cache

from catalog.models import Author


@never_cache
@login_required
@permission_required("catalog.view_author", raise_exception=True)
def authorList(request):
    return render(request, "catalog/authors/list.html", {"authors": Author.objects.all()})


@never_cache
@login_required
@permission_required("catalog.view_author", raise_exception=True)
def authorDetail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, "catalog/authors/detail.html", {"author": author})
