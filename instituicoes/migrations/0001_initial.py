# Generated by Django 4.1.3 on 2022-11-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('editado_em', models.DateTimeField(auto_now=True)),
                ('nome_instituicao', models.CharField(max_length=255, verbose_name='Nome da Instituição')),
                ('telefone_instituicao', models.CharField(max_length=30, verbose_name='Telefone da Instituição')),
                ('email_instituicao', models.CharField(max_length=50, unique=True, verbose_name='Email da Instituição')),
                ('rua_instituicao', models.CharField(max_length=255, verbose_name='Rua da Instituição')),
                ('cidade_instituicao', models.CharField(max_length=100, verbose_name='Cidade da Instituição')),
                ('pais_instituicao', models.CharField(max_length=100, verbose_name='País da Instituição')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
