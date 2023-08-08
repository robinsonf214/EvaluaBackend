# Generated by Django 4.2.2 on 2023-08-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0005_evaluacion_estilo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('id_estilo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=70)),
                ('descripcion', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'estilo',
            },
        ),
        migrations.RemoveField(
            model_name='alimentos',
            name='estilo',
        ),
        migrations.AddField(
            model_name='alimentos',
            name='estilo',
            field=models.ManyToManyField(to='evaluacion.estilo'),
        ),
    ]