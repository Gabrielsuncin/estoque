from django.contrib import admin
from django.http import HttpResponse
from datetime import datetime
import csv
import xlwt
from .models import (Fornecedor, Funcionario, Genero, Categoria, Subcategoria, Produto, HistoricoVendas,
                     HistoricoAtualizacaoPrecos, TamanhoProduto)


def export_as_csv(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={meta}.csv'
    writer = csv.writer(response)
    writer.writerow(field_names)
    for obj in queryset:
        obj.criado_em = obj.criado_em.strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([getattr(obj, field) for field in field_names])
    return response


def export_xlsx(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{meta}.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('meta')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in range(len(field_names)):
        ws.write(row_num, col_num, field_names[col_num], font_style)

    default_style = xlwt.XFStyle()
    rows = queryset.values_list()
    rows = [[x.strftime("%Y-%m-%d %H:%M:%S") if isinstance(x, datetime) else x for x in row] for row in rows]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], default_style)

    wb.save(response)
    return response


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

    actions = (export_as_csv, export_xlsx)

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

    actions = (export_as_csv, export_xlsx)

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ['id', 'genero', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'genero', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    list_filter = ['genero', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]

    actions = (export_as_csv, export_xlsx)

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'categoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'categoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    list_filter = ['categoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]

    actions = (export_as_csv, export_xlsx)

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)


@admin.register(Subcategoria)
class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'subcategoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'subcategoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    list_filter = ['subcategoria', 'codigo', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]

    actions = (export_as_csv, export_xlsx)

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)


@admin.register(TamanhoProduto)
class TamanhoProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'tamanho', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'tamanho', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    list_filter = ['tamanho', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]

    actions = (export_as_csv, export_xlsx)

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao', 'genero', 'categoria', 'subcategoria', 'tamanho', 'cor', 'grade',
                    'min_pecas', 'alerta_min', 'limite_alerta_min', 'total_pecas', 'preco_compra', 'preco_venda',
                    'motivo_alteracao_preco', 'auto_pedido', 'ean',
                    'sku', 'fornecedor', 'criado_por', 'criado_em', 'atualizado_por', 'atualizado_em', ]
    search_fields = ['id', 'descricao', 'genero', 'categoria', 'subcategoria', 'tamanho', 'cor', 'grade',
                     'alerta_min', 'limite_alerta_min', 'motivo_alteracao_preco', 'auto_pedido', 'ean', 'sku',
                     'fornecedor', 'criado_por', 'criado_em',
                     'atualizado_por', 'atualizado_em', ]
    list_filter = ['descricao', 'genero', 'categoria', 'subcategoria', 'tamanho', 'cor', 'grade',
                   'alerta_min', 'limite_alerta_min', 'motivo_alteracao_preco', 'auto_pedido', 'ean', 'sku',
                   'fornecedor', 'criado_por', 'criado_em',
                   'atualizado_por', 'atualizado_em', ]

    actions = (export_as_csv, export_xlsx)

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)


@admin.register(HistoricoAtualizacaoPrecos)
class HistoricoAtualizacaoPrecosAdmin(admin.ModelAdmin):
    list_display = ['id', 'ean', 'descricao', 'preco_compra', 'preco_venda', 'motivo_alteracao_preco', 'criado_por',
                    'criado_em']
    search_fields = ['id', 'ean', 'descricao', 'preco_compra', 'preco_venda', 'motivo_alteracao_preco', 'criado_por',
                     'criado_em', ]
    list_filter = ['ean', 'descricao', 'preco_compra', 'preco_venda', 'motivo_alteracao_preco', 'criado_por',
                   'criado_em', ]

    actions = (export_as_csv, export_xlsx)


@admin.register(HistoricoVendas)
class HistoricoVendasAdmin(admin.ModelAdmin):
    list_display = ['id', 'itens_compra', 'status', 'valor_compra', 'vendedor', 'caixa', 'criado_por', 'criado_em', ]
    search_fields = ['id', 'itens_compra', 'status', 'valor_compra', 'vendedor', 'caixa', 'criado_por', 'criado_em', ]
    list_filter = ['itens_compra', 'status', 'valor_compra', 'vendedor', 'caixa', 'criado_por', 'criado_em', ]

    actions = (export_as_csv, export_xlsx)

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)


export_xlsx.short_description = "Exportar dados em formato Excel"
export_as_csv.short_description = "Exportar dados em formato CSV"

# //TODO SELECIONAR CAMPOS A SEREM MOSTRADOS NO FILTRO
# //TODO REFATORAR SAVE_MODEL
