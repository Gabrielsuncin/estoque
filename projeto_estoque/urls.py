"""projeto_estoque URL Configuration

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
from django.contrib import admin
from django.urls import path, include
# from controle_estoque import urls as estoque_urls
from controle_estoque.urls import controle_estoque_urls
from controle_estoque.views import principal, generate_barcode, send_email_logs

urlpatterns = [
    # path('', include(estoque_urls)),
    path('admin/', admin.site.urls),
    path('', principal, name='principal'),
    path('barcode/', generate_barcode, name='barcode'),
    path('email/', send_email_logs, name='email'),
    path('vendas/', include(controle_estoque_urls)),
]
