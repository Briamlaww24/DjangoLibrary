from django.urls import path

from home import views

urlpatterns = [
    path("login/", views.loginView, name="login"),
    path("logout/", views.logoutView, name="logout"),
    path("register/", views.registerView, name="register"),
]
