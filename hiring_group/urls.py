"""hiring_group URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from hiring_group.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('inicio_sesion/', inicio_sesion, name='login'),
    path('registro_postulantes/', registro_postulantes),
    path('lista_ofertas/', lista_ofertas),
    path('inicio_valido', inicio_valido, name='inicio valido'),
    path('detalle_oferta/<int:oferta_id>/', detalle_oferta),
    path('postulacion/<int:oferta_id>/', postulacion),
    path('lista_postulaciones/', lista_postulaciones),
    path('contratacion/<int:oferta_id>/', contratacion),
    path('nomina/<int:empresa_id>/', nomina),
    path('registro_empresa/', registro_empresa),
    path('cerrar_sesion/',cerrar_sesion),
    path('registro_ac/', registro_area_conocimiento, name='areas_de_conocimiento'),
    path('registro_banco/',registro_banco),
    path('inicio_uempresa/',inicio_uempresa, name='inicio empresa'),
    path('inicio_upostulante/',inicio_upostulante, name='inicio postulante'),
    path('inicio_ucontratado/',inicio_ucontratado, name='inicio contratado'),
    path('inicio_hg/',inicio_uhg, name='inicio hg'),
    path('ofertas/', ofertas_list, name='ofertas_list'),
    path('ofertas/eliminar/<int:oferta_id>/', eliminar_oferta, name='eliminar_oferta'),
    path('ofertas/editar/<int:oferta_id>/', editar_oferta, name='editar_oferta'),
    path('modificar_usuario/',modificar_usuario,name='modificar_usuario'),
]