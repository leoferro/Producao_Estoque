# Generated by Django 4.1.7 on 2023-04-30 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_estoque', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itens',
            old_name='volum_ml',
            new_name='volume',
        ),
        migrations.CreateModel(
            name='Item_Venda',
            fields=[
                ('item_venda_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade', models.PositiveSmallIntegerField()),
                ('desconto', models.FloatField()),
                ('fk_item_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_estoque.itens')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('compra_id', models.AutoField(primary_key=True, serialize=False)),
                ('data_compra', models.DateField()),
                ('numero_referencia', models.PositiveBigIntegerField()),
                ('fornecedor', models.CharField(max_length=30)),
                ('quantidade', models.PositiveSmallIntegerField()),
                ('custo_unitario', models.FloatField()),
                ('validade', models.DateField()),
                ('valor_de_venda', models.FloatField()),
                ('restantes', models.PositiveSmallIntegerField()),
                ('fk_item_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_estoque.itens')),
            ],
        ),
    ]