import os
from pathlib import Path

from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User, UserManager
import barcode
from random import randint

from django.http import request

ESTADOS_CHOICES = (
    ('SP', 'SP'),
    ('RJ', 'RJ'),
    ('SC', 'SC'),
    ('MG', 'MG'),
    ('MS', 'MS'),
)

VENDAS_STATUS = (
    ('Concluída', 'Concluída'),
    ('Cancelada', 'Cancelada'),
)


class Fornecedor(models.Model):
    nome_empresa = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=15)
    telefone = models.CharField(max_length=11)
    endereco = models.CharField(max_length=300)
    pessoa_contato = models.CharField(max_length=100)
    email = models.EmailField(max_length=120)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fornecedor_criado_por', editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fornecedor_atualizado_por',
                                       editable=False,
                                       null=True, blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)
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
    usuario = models.CharField(max_length=30)
    email = models.EmailField(max_length=120)
    cpf = models.CharField(max_length=15)
    image = models.ImageField(upload_to='controle_estoque/media/images', verbose_name="Imagem", null=True, blank=True)
    data_admissao = models.DateField('Admitido em', auto_now_add=True)
    data_demissao = models.DateField('Demitido em', auto_now_add=True)
    ativo = models.BooleanField(default=True)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='funcionario_criado_por',
                                   editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='funcionario_atualizado_por',
                                       editable=False,
                                       null=True, blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.funcionario} - {self.cargo_funcionario}'

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['funcionario']

        db_table = 'funcionario'


class Genero(models.Model):
    genero = models.CharField(max_length=15)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='genero_criado_por', editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='genero_atualizado_por',
                                       editable=False,
                                       null=True, blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.genero}'

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
        ordering = ['genero']

        db_table = 'genero'


class Categoria(models.Model):
    categoria = models.CharField(max_length=30)
    codigo = models.CharField(max_length=3)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categoria_criado_por', editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='categoria_atualizado_por',
                                       editable=False,
                                       null=True, blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.categoria}'

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['categoria']

        db_table = 'categoria'


class Subcategoria(models.Model):
    subcategoria = models.CharField(max_length=30)
    codigo = models.CharField(max_length=3)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subcategoria_criado_por',
                                   editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subcategoria_atualizado_por',
                                       editable=False,
                                       null=True, blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subcategoria}'

    def save(self, *args, **kwargs):
        # //TODO FAZER FILTER
        subcategorias = Subcategoria.objects.all()
        codigos = [i.codigo for i in subcategorias]
        if not self.codigo in codigos:
            super(Subcategoria, self).save(*args, **kwargs)
        else:
            self.codigo = 'NUL'
            super(Subcategoria, self).save()

    class Meta:
        verbose_name = 'Subcategoria'
        verbose_name_plural = 'Subcategorias'
        ordering = ['subcategoria']

        db_table = 'subcategoria'


class TamanhoProduto(models.Model):
    tamanho = models.CharField(max_length=2)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tamanho_criado_por', editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_por = models.ForeignKey(User, on_delete=models.CASCADE,
                                       related_name='tamanho_atualizado_por', editable=False, null=True, blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.tamanho}'

    # def save(self, *args, **kwargs):
    #     self.tamanho = f"{self.tamanho}{(2 - len(self.tamanho))*'0'}"
    #     super(TamanhoProduto, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Tamanho do Produto'
        verbose_name_plural = 'Tamanho dos Produtos'
        ordering = ['tamanho']

        db_table = 'tamanho_produto'


class Produto(models.Model):
    descricao = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    tamanho = models.ForeignKey(TamanhoProduto, on_delete=models.PROTECT)
    cor = models.CharField(max_length=30)
    grade = models.CharField(max_length=30)
    min_pecas = models.PositiveSmallIntegerField()
    alerta_min = models.PositiveSmallIntegerField()
    limite_alerta_min = models.BooleanField(default=False, editable=False)
    total_pecas = models.PositiveSmallIntegerField()
    preco_compra = models.DecimalField(max_digits=6, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=6, decimal_places=2)
    motivo_alteracao_preco = models.CharField(max_length=300, null=True)
    auto_pedido = models.BooleanField(default=False)
    ean = models.CharField(max_length=13, editable=False)
    sku = models.CharField(max_length=10, editable=False)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='produto_criado_por', editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_por = models.ForeignKey(User, on_delete=models.CASCADE,
                                       related_name='produto_atualizado_por', editable=False, null=True, blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.ean}'

    def generate_barcode(self):
        '''
        //TODO Criar essa função recebendo o número após ser checado no DB se o mesmo não existe
        Se não encontrar esse code_id no DB atribui o code_id ao produto
        Se já existir gera outro code_id
        '''
        code_id = str(randint(7890000000000, 7899999999999))
        # //TODO SE NÃO FOR SALVAR O BARCODE, RETIRAR ESSE TRECHO
        # ean_number = barcode.get('ean13', code_id)
        # barcodes_folder = Path(__file__).resolve().parent / "barcodes"
        # ean_number.save(os.path.join(barcodes_folder, code_id))
        return code_id

    def save(self, *args, **kwargs):
        motivo = self.motivo_alteracao_preco

        tamanho_sku = f"{self.tamanho}{(2 - len(self.tamanho.tamanho))*'0'}"
        self.limite_alerta_min = False if self.total_pecas <= self.alerta_min else True
        self.motivo_alteracao_preco = None
        self.ean = self.generate_barcode() if not self.ean else self.ean
        self.sku = f"{self.genero.genero[:1]}{self.categoria.codigo}{self.subcategoria.codigo}{tamanho_sku}"
        super(Produto, self).save(*args, **kwargs)

        p = Produto.objects.filter(ean=self.ean).first()
        h = HistoricoAtualizacaoPrecos.objects.filter(ean=p).first()
        if ((h and p) and ((h.preco_compra != p.preco_compra) or (h.preco_venda != p.preco_venda))) or p and not h:
            HistoricoAtualizacaoPrecos.objects.create(
                ean=p,
                descricao=self.descricao,
                preco_compra=self.preco_compra,
                preco_venda=self.preco_venda,
                motivo_alteracao_preco=motivo,
                criado_por=self.criado_por
            )

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['descricao']

        db_table = 'produto'


class HistoricoAtualizacaoPrecos(models.Model):
    ean = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='hist_atual_preco_produto')
    descricao = models.CharField(max_length=30)
    preco_compra = models.DecimalField(max_digits=6, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=6, decimal_places=2)
    motivo_alteracao_preco = models.CharField(max_length=300)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hist_atual_preco_criado_por',
                                   editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ean.ean}'

    class Meta:
        verbose_name = 'Historico de Atualização de Preços'
        verbose_name_plural = 'Historico de Atualização de Preços'
        ordering = ['-criado_em']

        db_table = 'historico_atualizacao_precos'


# class Vendas(models.Model):
#     # BARCODE, PRODUTO, PREÇO, QUANTIDADE, DESCONTO, SUBTOTAL, TOTAL, FORMA_PGTO
#     barcode = models.ForeignKey(Produto, on_delete=models.PROTECT)
#     produto = models.



class HistoricoVendas(models.Model):
    itens_compra = models.JSONField(default=dict)
    status = models.CharField(max_length=30, choices=VENDAS_STATUS, default='Concluída')
    valor_compra = models.DecimalField(max_digits=6, decimal_places=2)
    vendedor = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='cargo_vendedor')
    caixa = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='cargo_caixa')
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hist_vendas_criado_por', editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Histórico de Venda'
        verbose_name_plural = 'Histórico de Vendas'
        ordering = ['-criado_em']

        db_table = 'historico_vendas'

# //TODO VERIFICAR ON_DELETE E UNIQUE https://docs.djangoproject.com/pt-br/3.1/ref/models/fields/
# //TODO EM VENDAS PRECISA VER COMO PEGAR SOMENTE OS FUNCIONÁRIOS COM CARGO VENDEDOR E CAIXA OU GRUPO?!
# //TODO VERIFICAR COMO COLOCAR O USUÁRIO NO CAMPO CRIADO_POR
# //TODO NA TABELA PEDIDOS COLOCAR CAMPO AUTORIZADO PARA O ANALISTA
# //TODO ACRESCENTAR CAMPO FORMA DE PAGTO EM VENDASHISTORY
# //TODO EM VENDAS COLOCAR BARCODE, PRODUTO, PREÇO,	QUANTIDADE,	DESCONTO, SUBTOTAL,	TOTAL, FORMA_PGTO
# //TODO FAZER FUNÇÃO DELETE PARA CRIAR LOG E ENVIAR EMAIL AOS ADMINS
