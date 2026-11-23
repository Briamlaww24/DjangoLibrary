from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from home.forms.registerForm import RegisterForm

class FreeLibraryLoginView(LoginView):
    template_name = 'home/authentication/login.html'
    redirect_authenticated_user = True

class FreeLibraryLogoutView(LogoutView):
    template_name = 'home/authentication/logout.html'
    next_page = 'login'

class FreeLibraryRegisterView(CreateView):
    template_name = 'home/authentication/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
