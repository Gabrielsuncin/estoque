from django.db import models

ESTADOS_CHOICES = (
    ('SP', 'SP'),
    ('RJ', 'RJ'),
    ('SC', 'SC'),
    ('MG', 'MG'),
    ('MS', 'MS'),
)


class Fornecedor(models.Model):
    nome_empresa = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=15)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=300)
    pessoa_contato = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
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
    funcionario = models.CharField(max_length=150)
    cargo_funcionario = models.CharField(max_length=150)
    estado = models.CharField(max_length=100, choices=ESTADOS_CHOICES)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=300)
    usuario = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    cpf = models.CharField(max_length=15)
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


class Genero(models.Model):
    genero = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.genero}'

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ['genero']


class Categoria(models.Model):
    categoria = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.categoria}'

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['categoria']


class Subcategoria(models.Model):
    subcategoria = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.subcategoria}'

    class Meta:
        verbose_name = 'Subcategoria'
        verbose_name_plural = 'Subcategorias'
        ordering = ['subcategoria']
