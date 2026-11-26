from django.contrib import admin

from catalog.forms import AuthorForm, CategoryForm, LoanForm
from catalog.models import Author, Book, Category, Loan
from catalog.roles import isCatalogAdmin


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "category", "rating", "owner")
    list_filter = ("category", "genre")
    search_fields = ("title", "slug", "authors__name")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("authors",)

    def has_add_permission(self, request):
        return isCatalogAdmin(request.user) and super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        return isCatalogAdmin(request.user) and super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        return isCatalogAdmin(request.user) and super().has_delete_permission(request, obj)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    form = AuthorForm
    list_display = ("name", "biography")
    list_filter = ("books__category",)
    search_fields = ("name", "biography")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ("name", "description")
    list_filter = ("books__genre",)
    search_fields = ("name", "description")


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    form = LoanForm
    list_display = ("book", "borrower", "borrowed_on", "due_on", "status")
    list_filter = ("status", "borrowed_on", "due_on")
    search_fields = ("book__title", "borrower__username")
