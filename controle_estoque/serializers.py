from rest_framework import serializers

from controle_estoque.models import Produto


class VendasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
