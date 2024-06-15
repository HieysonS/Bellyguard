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
from django.conf import settings
from django.contrib.staticfiles.urls import static

from webapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name='inicio'),
    # Rutas de Registro y Inicio de sesion
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('bienvenido/', bienvenido, name='bienvenido'),
    path('registrarse/', registrarse, name='registrarse'),
    # Rutas de pagina de inicio
    path('mas_informacion/', mas_informacion, name='mas_informacion'),
    path('contacto/', contacto, name='contacto'),
    path('herramientas/', herramientas, name='herramientas'),
    # Perfil
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    # Ruta del logout
    path('salir/', salir, name='salir'),
    # Ruta de bienvenida de usuario registrado
    path('bienvenido_nuevo/', bienvenido_nuevo, name='bienvenido_nuevo'),
    # Ruta de Registro del perfil embarazo
    path('registro_semanas/', registro_semanas, name='registro_semanas'),
    path('editar_perfil_embarazo/', editar_perfil_embarazo, name='editar_perfil_embarazo'),
    # Funciones adicionales
    path('ver_formacion/', info_embarazo, name='ver_formacion'),
    path('notificaciones/', notificaciones, name='notificaciones'),
    # Rutas de Registro de datos
    path('registro_historial_medico/', registro_historial_medico, name='registro_historial_medico'),
    path('registro_antecedentes_familiares/', registro_antecedentes_familiares, name='registro_antecedentes_familiares'),
    path('registro_estilo_vida/', registro_estilo_vida, name='registro_estilo_vida'),
    path('registro_sintomas/', registro_sintomas, name='registro_sintomas'),
    # Rutas de ML
    path('predecir_preeclampsia/', predecir_preeclampsia, name='predecir_preeclampsia'),
    path('predecir_fecha_parto/', predecir_fecha_parto, name='predecir_fecha_parto'),
    path('predecir_parto_prematuro/', predecir_parto_prematuro, name='predecir_parto_prematuro'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
