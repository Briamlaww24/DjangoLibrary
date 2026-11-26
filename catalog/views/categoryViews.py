from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models.deletion import ProtectedError
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import never_cache

from catalog.forms import CategoryForm
from catalog.models import Category


@never_cache
@login_required
@permission_required("catalog.view_category", raise_exception=True)
def categoryList(request):
    return render(request, "catalog/categories/list.html", {"categories": Category.objects.all()})


@never_cache
@login_required
@permission_required("catalog.view_category", raise_exception=True)
def categoryDetail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, "catalog/categories/detail.html", {"category": category})


@never_cache
@login_required
@permission_required("catalog.add_category", raise_exception=True)
@require_http_methods(["GET", "POST"])
def categoryCreate(request):
    form = CategoryForm(request.POST) if request.method == "POST" else CategoryForm()
    if request.method == "POST" and form.is_valid():
        category = form.save()
        messages.success(request, "Categoría creada exitosamente.")
        return redirect(category)
    return render(request, "catalog/categories/form.html", {"form": form})


@never_cache
@login_required
@permission_required("catalog.change_category", raise_exception=True)
@require_http_methods(["GET", "POST"])
def categoryEdit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST, instance=category) if request.method == "POST" else CategoryForm(instance=category)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Categoría actualizada exitosamente.")
        return redirect(category)
    return render(request, "catalog/categories/form.html", {"form": form, "category": category})


@never_cache
@login_required
@permission_required("catalog.delete_category", raise_exception=True)
@require_http_methods(["GET", "POST"])
def categoryDelete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        try:
            category.delete()
        except ProtectedError:
            messages.error(request, "La categoría tiene libros asociados y no se puede borrar.")
            return redirect(category)
        messages.success(request, "Categoría eliminada exitosamente.")
        return redirect("catalog:category_list")
    return render(request, "catalog/categories/delete.html", {"category": category})
