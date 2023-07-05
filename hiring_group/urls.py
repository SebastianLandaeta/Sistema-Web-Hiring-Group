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
from hiring_group.views import index, inicio_sesion, registro, lista_ofertas
from hiring_group.views import detalle_oferta, postulacion, lista_postulaciones
from hiring_group.views import contratacion, nomina, plantillaParametros,Lista_empresas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('inicio_sesion/', inicio_sesion),
    path('registro/', registro),
    path('lista_ofertas/', lista_ofertas),
    path('detalle_oferta/<int:oferta_id>/', detalle_oferta),
    path('postulacion/<int:oferta_id>/', postulacion),
    path('lista_postulaciones/', lista_postulaciones),
    path('contratacion/<int:oferta_id>/', contratacion),
    path('nomina/<int:empresa_id>/', nomina),
    path('plantillaParametros/', plantillaParametros),
    path('Lista_Empresas/',Lista_empresas),
]