# Generated by Django 3.0.5 on 2020-04-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0003_auto_20200416_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='entregado',
            field=models.BooleanField(default='', editable=False),
        ),
    ]
