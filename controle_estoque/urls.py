from rest_framework.routers import DefaultRouter
from .views import VendasViewSet


router = DefaultRouter()
router.register(r'', VendasViewSet, basename='vendas')
controle_estoque_urls = router.urls

"""
from django.urls import path
from .views import principal, generate_barcode, send_email_logs, vendas

urlpatterns = [
    path('', principal, name='principal'),
    path('barcode/', generate_barcode, name='barcode'),
    path('email/', send_email_logs, name='email'),
    path('vendas/', vendas, name='vendas'),
]
"""

