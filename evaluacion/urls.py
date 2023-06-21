from django.urls import path
from .views import EvaluacionCreateView, EvaluacionRetrieveUpdateDestroyView,AlimentosCreateView, AlimentosRetrieveUpdateDestroyView
from .views import CategoriaCreateView, CategoriaRetrieveUpdateDestroyView

urlpatterns = [
    path('evaluacion/', EvaluacionCreateView.as_view(), name='evaluacion-list-create'),
    path('evaluacion/<int:pk>/', EvaluacionRetrieveUpdateDestroyView.as_view(), name='evaluacion-retrieve-update-destroy'),
    path('alimentos/', AlimentosCreateView.as_view(), name='alimentos-list-create'),
    path('alimento/<int:pk>/', AlimentosRetrieveUpdateDestroyView.as_view(), name='alimentos-retrieve-update-destroy'),
     path('categorias/', CategoriaCreateView.as_view(), name='categoria-list-create'),
    path('categoria/<int:pk>/', CategoriaRetrieveUpdateDestroyView.as_view(), name='categoria-retrieve-update-destroy'),
]