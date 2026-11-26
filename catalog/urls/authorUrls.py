from django.urls import path

from catalog import views

urlpatterns = [
    path("", views.authorList, name="author_list"),
    path("<int:pk>/", views.authorDetail, name="author_detail"),
]
