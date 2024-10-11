# Generated by Django 5.1.1 on 2024-10-11 00:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testes', '0004_rename_tbtipo_tbtipos'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbPropriedades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PORTA', models.IntegerField()),
                ('DESCRICAO', models.CharField(max_length=20)),
                ('FK_PLACA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testes.tbplacas')),
                ('FK_TIPO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testes.tbtipos')),
            ],
        ),
    ]