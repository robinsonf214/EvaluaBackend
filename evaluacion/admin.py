from django.contrib import admin
from .models import Evaluacion, Alimentos, Categoria, Caracteristica, Subategoria

# Register your models here.
admin.site.register(Evaluacion)
admin.site.register(Alimentos)
admin.site.register(Categoria)
admin.site.register(Caracteristica)
admin.site.register(Subategoria)