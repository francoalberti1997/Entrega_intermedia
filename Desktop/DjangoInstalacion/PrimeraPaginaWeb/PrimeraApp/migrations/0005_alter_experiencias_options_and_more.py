# Generated by Django 4.1.1 on 2022-10-28 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrimeraApp', '0004_experiencias_evaluacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experiencias',
            options={'verbose_name': 'Calificación', 'verbose_name_plural': 'Calificaciones'},
        ),
        migrations.AlterField(
            model_name='experiencias',
            name='evaluacion',
            field=models.CharField(choices=[(1, 'Bad'), (2, 'Normal'), (3, 'Good')], max_length=1),
        ),
    ]
