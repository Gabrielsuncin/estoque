from django.contrib import admin
from .models import Fornecedor, Funcionario

# Register your models here.


class FornecedorAdmin(admin.ModelAdmin):

    list_display = ['id', 'nome_empresa', 'cnpj', 'endereco', 'estado', 'ativo', ]
    search_fields = ['id', 'nome_empresa', 'endereco', 'estado', 'ativo', ]
    list_filter = ['nome_empresa', 'cnpj',  'estado', 'ativo', ]


class FuncionarioAdmin(admin.ModelAdmin):

    list_display = ['id', 'funcionario', 'cargo_funcionario', 'cpf', 'data_admissao', 'estado', 'ativo', ]
    search_fields = ['id', 'funcionario', 'cargo_funcionario', 'cpf', 'data_admissao', 'estado', 'ativo', ]
    list_filter = ['funcionario', 'cargo_funcionario', 'data_admissao', 'estado', 'ativo', ]


admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
