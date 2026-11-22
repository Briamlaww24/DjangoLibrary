from django.urls import path
from home.views.homeView import home

urlpatterns = [
    path('', home, name='home'),
]