from django.contrib import admin
from .models import Fornecedor, Funcionario, Genero, Categoria, Subcategoria, Produto, HistoricoVendas, \
    HistoricoAtualizacaoPrecos, TamanhoProduto


# def save_model(self, request, obj, form, change):
#     if not obj.pk:
#         obj.criado_por = request.user
#     else:
#         obj.atualizado_por = request.user
#     obj.save()


class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_empresa', 'cnpj', 'endereco', 'estado', 'ativo', 'criado_por', 'criado_em',
                    'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'nome_empresa', 'endereco', 'estado', 'ativo', 'criado_por', 'criado_em', 'atualizado_por',
                     'atualizado_em', ]
    list_filter = ['nome_empresa', 'cnpj', 'estado', 'ativo', 'criado_por', 'criado_em', 'atualizado_por',
                   'atualizado_em', ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.criado_por = request.user
        else:
            obj.atualizado_por = request.user
        obj.save()


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'funcionario', 'cargo_funcionario', 'cpf', 'data_admissao', 'estado', 'ativo', 'criado_por',
                    'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'funcionario', 'cargo_funcionario', 'cpf', 'data_admissao', 'estado', 'ativo', 'criado_por',
                     'criado_em', 'atualizado_por', 'atualizado_em', ]
    list_filter = ['funcionario', 'cargo_funcionario', 'data_admissao', 'estado', 'ativo', 'criado_por', 'criado_em',
                   'atualizado_por', 'atualizado_em', ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.criado_por = request.user
        else:
            obj.atualizado_por = request.user
        obj.save()


class GeneroAdmin(admin.ModelAdmin):
    list_display = ['id', 'genero', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'genero', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    list_filter = ['id', 'genero', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.criado_por = request.user
        else:
            obj.atualizado_por = request.user
        obj.save()


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'categoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'categoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    list_filter = ['id', 'categoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.criado_por = request.user
        else:
            obj.atualizado_por = request.user
        obj.save()


class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'subcategoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'subcategoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    list_filter = ['id', 'subcategoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.criado_por = request.user
        else:
            obj.atualizado_por = request.user
        obj.save()


class TamanhoProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tamanho', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'tamanho', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    list_filter = ['id', 'tamanho', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.criado_por = request.user
        else:
            obj.atualizado_por = request.user
        obj.save()


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao', 'genero', 'categoria', 'subcategoria', 'tamanho', 'cor', 'grade',
                    'min_pecas', 'alerta_min', 'limite_alerta_min', 'total_pecas', 'preco_compra', 'preco_venda', 'motivo_alteracao_preco', 'ean',
                    'sku', 'fornecedor', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'descricao', 'genero', 'categoria', 'subcategoria', 'tamanho', 'cor', 'grade',
                     'alerta_min', 'limite_alerta_min', 'motivo_alteracao_preco', 'ean', 'sku', 'fornecedor', 'criado_por', 'criado_em',
                     'atualizado_por', 'atualizado_em', ]
    list_filter = ['id', 'descricao', 'genero', 'categoria', 'subcategoria', 'tamanho', 'cor', 'grade',
                   'alerta_min', 'limite_alerta_min', 'motivo_alteracao_preco', 'ean', 'sku', 'fornecedor', 'criado_por', 'criado_em',
                   'atualizado_por', 'atualizado_em', ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.criado_por = request.user
        else:
            obj.atualizado_por = request.user
        obj.save()


class HistoricoAtualizacaoPrecosAdmin(admin.ModelAdmin):
    list_display = ['id', 'ean', 'descricao', 'preco_compra', 'preco_venda', 'motivo_alteracao_preco', 'criado_por',
                    'criado_em' ]
    search_fields = ['id', 'ean', 'descricao', 'preco_compra', 'preco_venda', 'motivo_alteracao_preco', 'criado_por',
                    'criado_em', ]
    list_filter = ['id', 'ean', 'descricao', 'preco_compra', 'preco_venda', 'motivo_alteracao_preco', 'criado_por',
                    'criado_em', ]

    # def save_model(self, request, obj, form, change):
    #     if not obj.pk:
    #         obj.criado_por = request.user
    #     else:
    #         obj.atualizado_por = request.user
    #     obj.save()


class HistoricoVendasAdmin(admin.ModelAdmin):
    list_display = ['id', 'itens_compra', 'status', 'valor_compra', 'vendedor', 'caixa', 'criado_por', 'criado_em', ]
    search_fields = ['id', 'itens_compra', 'status', 'valor_compra', 'vendedor', 'caixa', 'criado_por', 'criado_em', ]
    list_filter = ['id', 'itens_compra', 'status', 'valor_compra', 'vendedor', 'caixa', 'criado_por', 'criado_em', ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.criado_por = request.user
        else:
            obj.atualizado_por = request.user
        obj.save()


admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subcategoria, SubcategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(HistoricoVendas, HistoricoVendasAdmin)
admin.site.register(HistoricoAtualizacaoPrecos, HistoricoAtualizacaoPrecosAdmin)
admin.site.register(TamanhoProduto, TamanhoProdutoAdmin)

# //TODO SELECIONAR CAMPOS A SEREM MOSTRADOS NO FILTRO
# //TODO FAZER DECORATOR PARA SAVE_MODEL
