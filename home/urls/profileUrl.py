from django.urls import path
from home.views.profileView import profile

urlpatterns = [
    path('profile/', profile, name='profile'),
]