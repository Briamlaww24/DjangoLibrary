from django.urls import include, path

app_name = "catalog"

urlpatterns = [
    path("entities/categories/", include("catalog.urls.categoryUrls")),
    path("entities/authors/", include("catalog.urls.authorUrls")),
    path("entities/loans/", include("catalog.urls.loanUrls")),
    path("", include("catalog.urls.bookUrls")),
]
