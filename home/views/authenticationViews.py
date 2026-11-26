from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.db import transaction
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.http import require_http_methods, require_POST

from catalog.roles import CONSULTANTS
from home.forms import RegisterForm


@sensitive_post_parameters("password1", "password2")
@require_http_methods(["GET", "POST"])
def registerView(request):
    form = RegisterForm(request.POST) if request.method == "POST" else RegisterForm()
    if request.method == "POST" and form.is_valid():
        with transaction.atomic():
            user = form.save()
            user.groups.add(Group.objects.get(name=CONSULTANTS))
        return redirect(settings.LOGIN_URL)
    return render(request, "home/authentication/register.html", {"form": form})


@sensitive_post_parameters("password")
@require_http_methods(["GET", "POST"])
def loginView(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    nextUrl = request.POST.get("next") or request.GET.get("next", "")
    if not url_has_allowed_host_and_scheme(nextUrl, {request.get_host()}, require_https=request.is_secure()):
        nextUrl = ""
    form = AuthenticationForm(request, data=request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect(nextUrl or settings.LOGIN_REDIRECT_URL)
    return render(request, "home/authentication/login.html", {"form": form, "next": nextUrl})


@require_POST
def logoutView(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
