"""
URL configuration for Bellyguard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('bienvenido/', bienvenido, name='bienvenido'),
    path('registrarse/', registrarse, name='registrarse'),
    path('mas_informacion/', mas_informacion, name='mas_informacion'),
    path('contacto/', contacto, name='contacto'),
    path('herramientas/', herramientas, name='herramientas'),
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('salir/', salir, name='salir'),
    path('bienvenido_nuevo/', bienvenido_nuevo, name='bienvenido_nuevo'),
    path('registro_semanas/', registro_semanas, name='registro_semanas'),
    path('editar_perfil_embarazo/', editar_perfil_embarazo, name='editar_perfil_embarazo'),

]
