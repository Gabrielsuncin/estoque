from django.db import models
from django.contrib.auth.models import User

ESTADOS_CHOICES = (
    ('SP', 'SP'),
    ('RJ', 'RJ'),
    ('SC', 'SC'),
    ('MG', 'MG'),
    ('MS', 'MS'),
)


class Funcionario(models.Model):
    funcionario = models.OneToOneField(User, related_name="funcionario", on_delete=models.CASCADE)
    cargo_funcionario = models.CharField(max_length=150)
    estado = models.CharField(max_length=100, choices=ESTADOS_CHOICES)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=300)
    email = models.EmailField(max_length=120)
    cpf = models.CharField(max_length=15)
    image = models.ImageField(upload_to='controle_estoque/media/images', verbose_name="Imagem", null=True, blank=True)
    data_admissao = models.DateField('Admitido em', auto_now_add=True)
    data_demissao = models.DateField('Demitido em', auto_now_add=True)
    ativo = models.BooleanField(default=True)
    criado_por = models.OneToOneField(User, on_delete=models.CASCADE, related_name='funcionario_criado_por',
                                      editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_por = models.OneToOneField(User, on_delete=models.CASCADE, related_name='funcionario_atualizado_por',
                                          editable=False,
                                          null=True, blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.funcionario} - {self.cargo_funcionario}'

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['funcionario']
