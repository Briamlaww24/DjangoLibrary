from django.urls import include, path

urlpatterns = [
    path("", include("home.urls.homeUrl")),
    path("auth/", include("home.urls.authenticationUrls")),
    path("", include("home.urls.profileUrl")),
]
