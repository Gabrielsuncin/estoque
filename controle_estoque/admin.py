from django.contrib import admin
from .models import Fornecedor, Funcionario, Genero, Categoria, Subcategoria, Produto


# Register your models here.


class FornecedorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome_empresa', 'cnpj', 'endereco', 'estado', 'ativo', 'created_at', 'updated_at']
    search_fields = ['id', 'nome_empresa', 'endereco', 'estado', 'ativo', ]
    list_filter = ['nome_empresa', 'cnpj', 'estado', 'ativo', ]


class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'funcionario', 'cargo_funcionario', 'cpf', 'data_admissao', 'estado', 'ativo', ]
    search_fields = ['id', 'funcionario', 'cargo_funcionario', 'cpf', 'data_admissao', 'estado', 'ativo', ]
    list_filter = ['funcionario', 'cargo_funcionario', 'data_admissao', 'estado', 'ativo', ]


class GeneroAdmin(admin.ModelAdmin):
    list_display = ['id', 'genero', ]
    search_fields = ['id', 'genero', ]
    list_filter = ['id', 'genero', ]


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'categoria', ]
    search_fields = ['id', 'categoria', ]
    list_filter = ['id', 'categoria', ]


class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'subcategoria', ]
    search_fields = ['id', 'subcategoria', ]
    list_filter = ['id', 'subcategoria', ]


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'descricao', 'genero', 'categoria', 'subcategoria', 'tamanho', 'cor', 'grade',
                    'min_pecas', 'total_pecas', 'preco_compra', 'preco_venda', 'ean', 'sku', 'fornecedor', ]
    search_fields = ['id', 'nome', 'descricao', 'genero', 'categoria', 'subcategoria', 'tamanho', 'cor', 'grade', 'ean',
                     'sku', 'fornecedor', ]
    list_filter = ['id', 'nome', 'descricao', 'genero', 'categoria', 'subcategoria', 'tamanho', 'cor', 'grade', 'ean',
                     'sku', 'fornecedor', ]


admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subcategoria, SubcategoriaAdmin)
admin.site.register(Produto, ProdutoAdmin)
