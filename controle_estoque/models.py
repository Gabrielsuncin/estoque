import os
from pathlib import Path

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
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subcategoria_criado_por',
                                   editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subcategoria_atualizado_por',
                                       editable=False,
                                       null=True, blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.subcategoria}'

    class Meta:
        verbose_name = 'Subcategoria'
        verbose_name_plural = 'Subcategorias'
        ordering = ['subcategoria']

        db_table = 'subcategoria'


# class TabelaPrecos(models.Model):
#     produto = models.CharField(max_length=30)
#     preco_compra = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
#     preco_venda = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
#     criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tabela_precos_criado_por',
#                                    editable=False)
#     criado_em = models.DateTimeField(auto_now_add=True)
#     atualizado_por = models.ForeignKey(User, on_delete=models.CASCADE,
#                                        related_name='tabela_precos_atualizado_por', editable=False, null=True,
#                                        blank=True)
#     atualizado_em = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f'{self.produto}'
#
#     class Meta:
#         verbose_name = 'Tabela de Preços'
#         verbose_name_plural = 'Tabela de Preços'
#         ordering = ['produto']
#
#         db_table = 'tabela_precos'


class Produto(models.Model):
    # produto = models.CharField(max_length=30)
    descricao = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    tamanho = models.CharField(max_length=10)
    cor = models.CharField(max_length=30)
    grade = models.CharField(max_length=30)
    min_pecas = models.PositiveSmallIntegerField()
    alerta_min = models.PositiveSmallIntegerField()
    limite_alerta_min = models.BooleanField(default=False, editable=False)
    total_pecas = models.PositiveSmallIntegerField()
    preco_compra = models.DecimalField(max_digits=6, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=6, decimal_places=2)
    motivo_alteracao_preco = models.CharField(max_length=300, null=True)
    ean = models.CharField(max_length=15, editable=False)
    sku = models.CharField(max_length=10, editable=False)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='produto_criado_por', editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_por = models.ForeignKey(User, on_delete=models.CASCADE,
                                       related_name='produto_atualizado_por', editable=False, null=True, blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.ean}'

    def tamanho_codigo(self, tamanho):
        tamanhos = {"P": '100', "M": "200", "G": "300", "GG": "400", "XG": "500"}
        return tamanhos[tamanho]

    def generate_barcode(self):
        '''
        //TODO Criar essa função recebendo o número após ser checado no DB se o mesmo não existe
        Se não encontrar esse code_id no DB atribui o code_id ao produto
        Se já existir gera outro code_id
        '''
        code_id = str(randint(7890000000000, 7899999999999))
        ean_number = barcode.get('ean13', code_id)
        barcodes_folder = Path(__file__).resolve().parent / "barcodes"
        ean_number.save(os.path.join(barcodes_folder, code_id))
        return code_id

    def generate_sku(self):
        """
        Exemplo:
        Genero: M
        Categoria: CS
        Subcategoria: ML
        Tamanho: 004
        Sequencias: 001
        Ficando: MCSML004001

        As sequências se iniciarão em 001 para cada tipo de produto de acordo com a categoria
        """
        pass

    def atingiu_limite_min(self):
        if self.total_pecas <= self.alerta_min:
            self.limite_alerta_min = False
        else:
            self.limite_alerta_min = True

    def save(self, *args, **kwargs):
        self.atingiu_limite_min()
        tamanho = f"{self.tamanho}" if self.tamanho.isdigit() else f"{self.tamanho_codigo(self.tamanho)}"
        if not self.ean:
            self.ean = self.generate_barcode()

        categoria_number = ''
        sub_categoria_number = ''
        if len(str(self.categoria_id)) < 2:
            categoria_number = f"0{self.categoria_id}"
        if len(str(self.subcategoria_id)) < 2:
            sub_categoria_number = f"0{self.subcategoria_id}"
        self.sku = f"{self.genero_id}{categoria_number}{sub_categoria_number}{tamanho}"

        motivo = self.motivo_alteracao_preco

        self.motivo_alteracao_preco = None
        super().save(*args, **kwargs)

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


class HistoricoVendas(models.Model):
    itens_compra = models.JSONField(default=dict)
    status = models.CharField(max_length=30, choices=VENDAS_STATUS, default='Concluída')
    valor_compra = models.DecimalField(max_digits=6, decimal_places=2)
    vendedor = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='cargo_vendedor')
    caixa = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='cargo_caixa')
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vendas_criado_por', editable=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Histórico de Venda'
        verbose_name_plural = 'Histórico de Vendas'
        ordering = ['-criado_em']

        db_table = 'historico_vendas'

# //TODO VERIFICAR ON_DELETE E UNIQUE
# //TODO EM VENDAS PRECISA VER COMO PEGAR SOMENTE OS FUNCIONÁRIOS COM CARGO VENDEDOR E CAIXA OU GRUPO?!
# //TODO COLOCAR CAMPO AUTOMÁTICO PARA INFORMAR SE O PRODUTO SERÁ ENVIADO AUTOMATICAMENTE PARA O PEDIDO
# //TODO VERIFICAR COMO COLOCAR O USUÁRIO NO CAMPO CRIADO_EM
# //TODO NA TABELA PEDIDOS COLOCAR CAMPO AUTORIZADO PARA O ANALISTA
# //TODO ACRESCENTAR CAMPO FORMA DE PAGTO EM VENDASHISTORY
# //TODO EM VENDAS COLOCAR FORMA DE PAGTO, QUANTIDADE, SUBTOTAL, DESCONTO E TOTAL
# //TODO CRIAR CAMPO BOOL PARA PRODUTOS QUE ATINGIREM O ALERTA_MIN
# //TODO CRIAR FUNÇÃO PARA SKU CONTENDO UM PADRÃO. AS IDEIAS ESTÃO COMENTADAS COM A FUNÇÃO