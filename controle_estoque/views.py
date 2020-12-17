import logging
from pathlib import Path
from django.conf import settings
from django.core import mail
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from controle_estoque.models import Produto
from random import randint
import barcode

from controle_estoque.serializers import VendasSerializer

logger = logging.getLogger('file')


def principal(request):
    return render(request, 'principal.html')


def generate_barcode(self):
    '''
    //TODO Criar essa função recebendo o número após ser checado no DB se o mesmo não existe
    Se não encontrar esse code_id no DB atribui o code_id ao produto
    Exemplo:
    obj = get_object_or_404(MyModel, pk=code_id)
    Se já existir gera outro code_id
    '''
    code_id = str(randint(7890000000000, 7899999999999))
    ean_number = barcode.get('ean13', code_id)
    barcodes_folder = Path(__file__).resolve().parent / "barcodes"
    ean_number.save()
    return HttpResponse(f'Código de barras {ean_number} criado com sucesso!')


def send_email_logs(request):
    logger.info('Email enviado com sucesso!')
    filename = 'logs.log'

    email_default = settings.DEFAULT_FROM_EMAIL

    with open(filename) as logfile:
        mail.EmailMessage(
            'Novo log gerado',
            'Mensagem de teste de envio de email do Django',
            email_default,
            [email_default],
            attachments=[(filename, logfile.read(), 'text/plain')]
        ).send()

    return HttpResponse('Email enviado com sucesso!')


class VendasViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = VendasSerializer


# //TODO A VIEW DE VENDAS DEVERÁ RETORNAR O PRODUTO E O PREÇO DO DB QUANDO FOR INSERIDO O CÓDIGO DO MESMO
