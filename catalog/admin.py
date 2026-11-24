from django.contrib import admin

from catalog.models.bookModel import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "genre", "rating", "description")
    prepopulated_fields = {"slug": ("title",)}