# Generated by Django 4.1.1 on 2022-10-26 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrimeraApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('cargo', models.CharField(max_length=20)),
            ],
        ),
    ]
