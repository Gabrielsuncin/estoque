from django.shortcuts import render
from projeto_estoque.settings import STATIC_URL


def index(request):
    context = {
        'profile_photo': STATIC_URL + 'assets/img/theme/avocado.png',
        'fullname': f'{request.user.first_name} {request.user.last_name}',
    }
    if request.user.funcionario.image:
        context['profile_photo'] = request.user.funcionario.image.url
    return render(request, 'index.html', context)
