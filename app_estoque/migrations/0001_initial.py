# Generated by Django 4.1.7 on 2023-03-28 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Itens',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('volum_ml', models.IntegerField()),
                ('categoria', models.CharField(max_length=30)),
            ],
        ),
    ]
