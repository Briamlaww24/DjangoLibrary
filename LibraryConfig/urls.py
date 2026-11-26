"""
URL configuration for FreeLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path, include
from django.views.decorators.cache import never_cache
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('catalog/', include('catalog.urls')),
]

if settings.DEBUG:
    serveCatalogMedia = never_cache(login_required(
        permission_required("catalog.view_book", raise_exception=True)(serve)
    ))
    urlpatterns += static(
        settings.MEDIA_URL, view=serveCatalogMedia, document_root=settings.MEDIA_ROOT,
    )
