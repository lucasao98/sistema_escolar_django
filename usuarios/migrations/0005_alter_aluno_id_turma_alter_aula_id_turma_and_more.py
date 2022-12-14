# Generated by Django 4.1.3 on 2022-11-15 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turmas', '0001_initial'),
        ('usuarios', '0004_alter_aula_id_disciplina_delete_disciplina'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='id_turma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='disciplina', to='turmas.turma', verbose_name=' Id da turma'),
        ),
        migrations.AlterField(
            model_name='aula',
            name='id_turma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aulas', to='turmas.turma', verbose_name=' Id da turma'),
        ),
        migrations.DeleteModel(
            name='Turma',
        ),
    ]
