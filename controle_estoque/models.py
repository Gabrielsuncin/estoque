from django.db import models


ESTADOS_CHOICES = (
        ('SP', 'SP'),
        ('RJ', 'RJ'),
        ('SC', 'SC'),
        ('MG', 'MG'),
        ('MS', 'MS'),
    )


class Fornecedor(models.Model):
    nome_empresa = models.CharField(max_length=150, null=False, blank=False)
    cnpj = models.CharField(max_length=15, null=False, blank=False)
    telefone = models.CharField(max_length=11, null=False, blank=False)
    endereco = models.CharField(max_length=300)
    pessoa_contato = models.CharField(max_length=100)
    created_at = models.DateField('Criado em', auto_now_add=True)
    updated_at = models.DateField('Atualizado em', auto_now=True)
    estado = models.CharField(max_length=100, choices=ESTADOS_CHOICES, default='SP')
    ativo = models.BooleanField(default=True)


    def __str__(self):
        return self.nome_empresa

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['nome_empresa']


class Funcionario(models.Model):
    funcionario = models.CharField(max_length=150, null=False, blank=False)
    cargo_funcionario = models.CharField(max_length=150, null=False, blank=False)
    estado = models.CharField(max_length=100, choices=ESTADOS_CHOICES)
    telefone = models.CharField(max_length=11, null=False, blank=False)
    endereco = models.CharField(max_length=300)
    usuario = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=15, null=False, blank=False)
    image = models.ImageField(upload_to='controle_estoque/media/images', verbose_name="Imagem", null=True, blank=True)
    data_admissao = models.DateField('Criado em', auto_now_add=True)
    data_demissao = models.DateField('Demitido em', auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.funcionario}, {self.cargo_funcionario}'

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['funcionario']



