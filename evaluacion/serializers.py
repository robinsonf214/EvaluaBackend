from rest_framework import serializers
from .models import Evaluacion, Alimentos, Categoria, Caracteristica, Subategoria

class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluacion
        fields = '__all__'

class AlimentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alimentos
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class CaracteristicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caracteristica
        fields = '__all__'

class SubategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subategoria
        fields = '__all__'