from django.urls import path, include

from catalog.views.catalogViews import token, read, list

app_name = "catalog"

urlpatterns = [
    path("", list, name="list"),
    path("", include("catalog.urls.createBookUrl")),
    path("<slug:slug>/", token, name="token"),
    path("<slug:slug>/read/", read, name="read"),
]
