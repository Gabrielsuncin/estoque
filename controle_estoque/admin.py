from django.contrib import admin
from .models import Fornecedor, Funcionario, Genero, Categoria, Subcategoria, Produto, HistoricoVendas, \
    HistoricoAtualizacaoPrecos, TamanhoProduto


def salva_criado_por(request, obj):
    if not obj.pk:
        obj.criado_por = request.user
    else:
        obj.atualizado_por = request.user
    obj.save()


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_empresa', 'cnpj', 'endereco', 'estado', 'ativo', 'criado_por', 'criado_em',
                    'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'nome_empresa', 'endereco', 'estado', 'ativo', 'criado_por', 'criado_em', 'atualizado_por',
                     'atualizado_em', ]
    list_filter = ['nome_empresa', 'cnpj', 'estado', 'ativo', 'criado_por', 'criado_em', 'atualizado_por',
                   'atualizado_em', ]

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'funcionario', 'cargo_funcionario', 'cpf', 'data_admissao', 'estado', 'ativo', 'criado_por',
                    'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'funcionario', 'cargo_funcionario', 'cpf', 'data_admissao', 'estado', 'ativo', 'criado_por',
                     'criado_em', 'atualizado_por', 'atualizado_em', ]
    list_filter = ['funcionario', 'cargo_funcionario', 'data_admissao', 'estado', 'ativo', 'criado_por', 'criado_em',
                   'atualizado_por', 'atualizado_em', ]

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['id', 'genero', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'genero', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    list_filter = ['genero', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'categoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'categoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    list_filter = ['categoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)


@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'subcategoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'subcategoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    list_filter = ['subcategoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)


@admin.register(TamanhoProduto)
class TamanhoProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tamanho', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'tamanho', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    list_filter = ['tamanho', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao', 'genero', 'categoria', 'subcategoria', 'tamanho', 'cor', 'grade',
                    'min_pecas', 'alerta_min', 'limite_alerta_min', 'total_pecas', 'preco_compra', 'preco_venda', 'motivo_alteracao_preco', 'auto_pedido', 'ean',
                    'sku', 'fornecedor', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'descricao', 'genero', 'categoria', 'subcategoria', 'tamanho', 'cor', 'grade',
                     'alerta_min', 'limite_alerta_min', 'motivo_alteracao_preco', 'auto_pedido', 'ean', 'sku', 'fornecedor', 'criado_por', 'criado_em',
                     'atualizado_por', 'atualizado_em', ]
    list_filter = ['descricao', 'genero', 'categoria', 'subcategoria', 'tamanho', 'cor', 'grade',
                   'alerta_min', 'limite_alerta_min', 'motivo_alteracao_preco', 'auto_pedido', 'ean', 'sku', 'fornecedor', 'criado_por', 'criado_em',
                   'atualizado_por', 'atualizado_em', ]

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)


@admin.register(HistoricoAtualizacaoPrecos)
class HistoricoAtualizacaoPrecosAdmin(admin.ModelAdmin):
    list_display = ['id', 'ean', 'descricao', 'preco_compra', 'preco_venda', 'motivo_alteracao_preco', 'criado_por',
                    'criado_em' ]
    search_fields = ['id', 'ean', 'descricao', 'preco_compra', 'preco_venda', 'motivo_alteracao_preco', 'criado_por',
                    'criado_em', ]
    list_filter = ['ean', 'descricao', 'preco_compra', 'preco_venda', 'motivo_alteracao_preco', 'criado_por',
                    'criado_em', ]


@admin.register(HistoricoVendas)
class HistoricoVendasAdmin(admin.ModelAdmin):
    list_display = ['id', 'itens_compra', 'status', 'valor_compra', 'vendedor', 'caixa', 'criado_por', 'criado_em', ]
    search_fields = ['id', 'itens_compra', 'status', 'valor_compra', 'vendedor', 'caixa', 'criado_por', 'criado_em', ]
    list_filter = ['itens_compra', 'status', 'valor_compra', 'vendedor', 'caixa', 'criado_por', 'criado_em', ]

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)


# //TODO SELECIONAR CAMPOS A SEREM MOSTRADOS NO FILTRO
# //TODO REFATORAR SAVE_MODEL
