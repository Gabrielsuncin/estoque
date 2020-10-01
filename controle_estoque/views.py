from django.shortcuts import render, redirect
from random import randint
import barcode

# Create your views here.


def principal(request):
    return render(request, 'principal.html')


def generate_barcode(request):
    '''
    //TODO Criar essa função recebendo o número após ser checado no DB se o mesmo não existe
    Se não encontrar esse code_id no DB atribui o code_id ao produto
    Exemplo:
    obj = get_object_or_404(MyModel, pk=code_id)
    Se já existir gera outro code_id
    '''
    code_id = str(randint(100000000000, 999999999999))
    ean = barcode.get('ean13', code_id)
    ean.save(code_id)
    # return HttpResponse('Código de barras criado com sucesso!')
    return redirect('principal')


# //TODO A VIEW DE VENDAS DEVERÁ RETORNAR O PRODUTO E O PREÇO DO DB QUANDO FOR INSERIDO O CÓDIGO DO MESMO
# //TODO NA TABELA DE PRODUTOS COLOCAR PREÇO VAREJO E ATACADO