from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Cliente
from .serializers import Evaluacion

class EvaluacionCreateView(generics.ListCreateAPIView):
    queryset = Evaluacion.objects.all()
    serializer_class = Evaluacion

class EvaluacionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluacion.objects.all()
    serializer_class = EvaluacionSerializer

