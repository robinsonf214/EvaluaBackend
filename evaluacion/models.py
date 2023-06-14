from django.db import models

# Create your models here.
class Evaluacion(models.Model):
    id_evaluacion = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    informacion = models.CharField(max_length=300)
    nota_final = models.IntegerField()
    class Meta:
        db_table = 'evaluacion'

class Alimentos(models.Model):
    id_alimentos = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=60)
    estilo = models.CharField(max_length=80)
    categorias = models.ManyToManyField('Categoria')
    class Meta:
        db_table = 'alimentos'

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    caracteristicas = models.ManyToManyField('Caracteristica')
    nombre = models.CharField(max_length=70)
    descripcion = models.CharField(max_length=300)
    calificacion = models.IntegerField()
    class Meta:
        db_table = 'categoria'

class Caracteristica(models.Model):
    id_caracteristica = models.IntegerField(primary_key=True)
    valoracion = models.IntegerField()
    nombre = models.CharField(max_length=70)
    class Meta:
        db_table = 'caracteristica'
    
class Subategoria(models.Model):
    id_subcategoria = models.IntegerField(primary_key=True)
    caracteristicas = models.ManyToManyField('Caracteristica')
    nombre = models.CharField(max_length=70)
    calificacion = models.IntegerField()
    class Meta:
        db_table = 'subategoria'

    