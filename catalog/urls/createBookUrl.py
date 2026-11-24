from django.urls import path

from catalog.views.createBookView import createBook

urlpatterns = [
    path("create/", createBook, name="create"),
]