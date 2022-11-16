# Generated by Django 4.1.3 on 2022-11-15 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instituicoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('editado_em', models.DateTimeField(auto_now=True)),
                ('nome_professor', models.CharField(max_length=100, verbose_name='Nome do Professor')),
                ('sobrenome_professor', models.CharField(max_length=255, verbose_name='Sobrenome do Professor')),
                ('email_professor', models.CharField(max_length=100, verbose_name='Email do Professor')),
                ('telefone_professor', models.CharField(max_length=50, verbose_name='Telefone do Professor')),
                ('is_active', models.BooleanField(default=0)),
                ('instituicao', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='professores', to='instituicoes.instituicao', verbose_name='Id da Instituição')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricoAcademico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('editado_em', models.DateTimeField(auto_now=True)),
                ('nome_instituicao', models.CharField(max_length=255, verbose_name='Nome da Faculdade')),
                ('data_inicio', models.DateTimeField(verbose_name='Data de Inicio da Faculdade')),
                ('data_fim', models.DateTimeField(verbose_name='Data de Fim da Faculdade')),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='historico', to='professores.professor', verbose_name='Id do professor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]