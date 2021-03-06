# Generated by Django 2.2.9 on 2020-09-14 11:55

import core.models
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhrasesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modified_at', models.DateField(auto_now=True, verbose_name='Modificado')),
                ('activated', models.BooleanField(default=True, verbose_name='Ativado?')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('phrase', models.TextField(verbose_name='Frase')),
                ('image', stdimage.models.StdImageField(upload_to=core.models.get_file_path, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Phrase',
                'verbose_name_plural': 'Phrases',
            },
        ),
    ]
