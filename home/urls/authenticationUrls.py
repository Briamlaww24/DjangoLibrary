from django.urls import path
from home.views.authenticationViews import FreeLibraryLoginView, FreeLibraryLogoutView, FreeLibraryRegisterView

urlpatterns = [
    path('login/', FreeLibraryLoginView.as_view(), name='login'),
    path('logout/', FreeLibraryLogoutView.as_view(), name='logout'),
    path('register/', FreeLibraryRegisterView.as_view(), name='register'),
]