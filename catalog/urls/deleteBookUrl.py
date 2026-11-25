from django.urls import path

from catalog.views.deleteBookView import delete_book

urlpatterns = [
    path("<slug:slug>/delete/", delete_book, name="delete"),
]
