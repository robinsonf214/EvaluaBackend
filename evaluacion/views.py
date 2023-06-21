from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Evaluacion, Alimentos, Categoria
from .serializers import EvaluacionSerializer,AlimentosSerializer, CategoriaSerializer 

class EvaluacionCreateView(generics.ListCreateAPIView):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer
class EvaluacionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer


class AlimentosCreateView(generics.ListCreateAPIView):
    queryset = Alimentos.objects.all()
    serializer_class = AlimentosSerializer

class AlimentosRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alimentos.objects.all()
    serializer_class = AlimentosSerializer


class CategoriaCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer