# Generated by Django 4.1.7 on 2023-04-30 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_estoque', '0002_rename_volum_ml_itens_volume_item_venda_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='itens',
            name='marca',
            field=models.CharField(default='NA', max_length=30),
        ),
        migrations.AddField(
            model_name='itens',
            name='produto_sabor',
            field=models.CharField(default='NA', max_length=30),
        ),
        migrations.AddField(
            model_name='itens',
            name='tipo',
            field=models.CharField(default='NA', max_length=30),
        ),
    ]
