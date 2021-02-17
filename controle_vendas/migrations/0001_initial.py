# Generated by Django 3.1.1 on 2021-02-17 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('controle_estoque', '0001_initial'),
        ('controle_usuarios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoVendas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itens_compra', models.JSONField(default=dict)),
                ('status', models.CharField(choices=[('Concluída', 'Concluída'), ('Cancelada', 'Cancelada')], default='Concluída', max_length=30)),
                ('valor_compra', models.DecimalField(decimal_places=2, max_digits=6)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('caixa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargo_caixa', to='controle_usuarios.funcionario')),
                ('criado_por', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='hist_vendas_criado_por', to=settings.AUTH_USER_MODEL)),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cargo_vendedor', to='controle_usuarios.funcionario')),
            ],
            options={
                'verbose_name': 'Histórico de Venda',
                'verbose_name_plural': 'Histórico de Vendas',
                'ordering': ['-criado_em'],
            },
        ),
        migrations.CreateModel(
            name='HistoricoAtualizacaoPrecos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30)),
                ('preco_compra', models.DecimalField(decimal_places=2, max_digits=6)),
                ('preco_venda', models.DecimalField(decimal_places=2, max_digits=6)),
                ('motivo_alteracao_preco', models.CharField(max_length=300)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('criado_por', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='hist_atual_preco_criado_por', to=settings.AUTH_USER_MODEL)),
                ('ean', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hist_atual_preco_produto', to='controle_estoque.produto')),
            ],
            options={
                'verbose_name': 'Historico de Atualização de Preços',
                'verbose_name_plural': 'Historico de Atualização de Preços',
                'ordering': ['-criado_em'],
            },
        ),
    ]