# Generated by Django 5.0.3 on 2024-11-01 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testes', '0007_tbtestes_fk_propriedade_tbtestes_resultado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbtestes',
            name='DATA',
            field=models.DateTimeField(verbose_name='TIMESTAMP'),
        ),
    ]
