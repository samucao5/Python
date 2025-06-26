"""
URL configuration for setup project.

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
from usuario_2.views import criar_conta, token, retorno_dos_dados


urlpatterns = [
    path('admin/', admin.site.urls),
    path('criar_conta/', criar_conta, name='criar_conta'),
    path('token/', token, name='token'),
    path('retorno_dos_dados/',retorno_dos_dados,name='retorno_dos_dados'),
    
]
