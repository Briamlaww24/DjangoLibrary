from django.urls import path

from catalog.views.editBookView import edit_book

urlpatterns = [
    path("<slug:slug>/edit/", edit_book, name="edit"),
]
