from django.urls import path

from catalog import views

urlpatterns = [
    path("", views.categoryList, name="category_list"),
    path("create/", views.categoryCreate, name="category_create"),
    path("<int:pk>/", views.categoryDetail, name="category_detail"),
    path("<int:pk>/edit/", views.categoryEdit, name="category_edit"),
    path("<int:pk>/delete/", views.categoryDelete, name="category_delete"),
]
