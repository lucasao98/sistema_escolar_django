# Generated by Django 4.1.3 on 2022-11-15 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_aluno_id_turma_alter_aula_id_turma_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Aluno',
        ),
    ]