# Generated by Django 4.1.3 on 2022-11-15 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disciplinas', '0001_initial'),
        ('usuarios', '0003_remove_professor_instituicao_alter_aula_id_professor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='id_disciplina',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aulas', to='disciplinas.disciplina', verbose_name='Id da disciplina'),
        ),
        migrations.DeleteModel(
            name='Disciplina',
        ),
    ]
