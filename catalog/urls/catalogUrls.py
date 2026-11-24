from django.urls import path

from catalog.views.catalogViews import token, read, list

app_name = "catalog"

urlpatterns = [
    path("", list, name="list"),

    path("<slug:slug>/", token, name="token"),
    path("<slug:slug>/read/", read, name="read"),
]
