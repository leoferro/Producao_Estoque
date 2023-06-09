# Generated by Django 4.1.7 on 2023-05-01 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_estoque', '0007_alter_item_venda_data_venda'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_venda',
            name='fk_compra_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app_estoque.compra'),
        ),
        migrations.AlterField(
            model_name='item_venda',
            name='desconto',
            field=models.FloatField(default=0),
        ),
    ]
