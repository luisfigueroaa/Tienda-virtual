# Generated by Django 3.0.5 on 2020-04-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0004_pedidos_entregado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidos',
            name='entregado',
            field=models.BooleanField(default='false'),
        ),
    ]
