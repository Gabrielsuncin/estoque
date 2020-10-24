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

        db_table = 'fornecedor'


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
    created_at = models.DateField('Criado em', auto_now_add=True)
    updated_at = models.DateField('Atualizado em', auto_now=True)

    def __str__(self):
        return f'{self.funcionario}, {self.cargo_funcionario}'

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['funcionario']

        db_table = 'funcionario'


class Genero(models.Model):
    genero = models.CharField(max_length=15)
    created_at = models.DateField('Criado em', auto_now_add=True)
    updated_at = models.DateField('Atualizado em', auto_now=True)

    def __str__(self):
        return f'{self.genero}'

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ['genero']

        db_table = 'genero'

class Categoria(models.Model):
    categoria = models.CharField(max_length=30)
    created_at = models.DateField('Criado em', auto_now_add=True)
    updated_at = models.DateField('Atualizado em', auto_now=True)

    def __str__(self):
        return f'{self.categoria}'

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['categoria']

        db_table = 'categoria'


class Subcategoria(models.Model):
    subcategoria = models.CharField(max_length=30)
    created_at = models.DateField('Criado em', auto_now_add=True)
    updated_at = models.DateField('Atualizado em', auto_now=True)

    def __str__(self):
        return f'{self.subcategoria}'

    class Meta:
        verbose_name = 'Subcategoria'
        verbose_name_plural = 'Subcategorias'
        ordering = ['subcategoria']

        db_table = 'subcategoria'


class Produto(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    tamanho = models.CharField(max_length=10)
    cor = models.CharField(max_length=30)
    grade = models.CharField(max_length=30)
    min_pecas = models.PositiveSmallIntegerField()
    alerta_min = models.PositiveSmallIntegerField()
    total_pecas = models.PositiveSmallIntegerField()
    preco_compra = models.DecimalField(max_digits=6, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=6, decimal_places=2)
    ean = models.CharField(max_length=15)
    sku = models.CharField(max_length=10)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    created_at = models.DateField('Criado em', auto_now_add=True)
    updated_at = models.DateField('Atualizado em', auto_now=True)

    def __str__(self):
        return f'{self.nome}'

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['nome']

        db_table = 'produto'
