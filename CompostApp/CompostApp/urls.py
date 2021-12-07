"""cadastro URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django import urls
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import i18n

from django.conf.urls.i18n import i18n_patterns
from composteira import views
import insumo.views
import composteira.views

urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),
    # User Management
    path("accounts/", include("allauth.urls")),
    # Local
    path("", include("pages.urls", namespace="pages")),
    path('homeComposteira/',composteira.views.composteiraList, name="home-composteira"),
    path('homeComposteira/novaComposteira/',composteira.views.novaComposteira, name="nova-composteira"),
    path('homeComposteira/<int:id>/', composteira.views.composteiraView, name="composteira-view"),
    path('homeComposteira/editComposteira/<int:id>/', composteira.views.editComposteiraM, name="edit-composteira"),
    path('homeComposteira/deleteComposteira/<int:id>/', composteira.views.deleteComposteira, name="delete-composteira"),
    #re_path(r'addinsumo/', insumo.views.Cascadingdllitems, name="novo-insumo"),
    re_path(r'^addinsumo/',insumo.views.insumoList, name="novo-insumo"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += i18n_patterns (
    #path('', views.index),
    path('accounts/', include("allauth.urls")),
)