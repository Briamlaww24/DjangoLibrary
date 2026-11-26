from django.urls import path

from catalog import views

urlpatterns = [
    path("", views.bookList, name="list"),
    path("create/", views.createBook, name="create"),
    path("<slug:slug>/", views.bookDetail, name="token"),
    path("<slug:slug>/read/", views.bookRead, name="read"),
    path("<slug:slug>/pdf/", views.bookPdf, name="book_pdf"),
    path("<slug:slug>/edit/", views.editBook, name="edit"),
    path("<slug:slug>/delete/", views.deleteBook, name="delete"),
]
