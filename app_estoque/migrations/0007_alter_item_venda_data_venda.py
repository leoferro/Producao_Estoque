# Generated by Django 4.1.7 on 2023-04-30 23:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_estoque', '0006_alter_item_venda_data_venda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_venda',
            name='data_venda',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]