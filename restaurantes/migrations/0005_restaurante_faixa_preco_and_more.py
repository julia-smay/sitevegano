# Generated by Django 4.1 on 2023-05-31 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantes', '0004_restaurante_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurante',
            name='faixa_preco',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='restaurante',
            name='informacoes_adicionais',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
    ]