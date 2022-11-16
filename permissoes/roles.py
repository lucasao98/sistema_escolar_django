from rolepermissions.roles import AbstractUserRole


class Diretor(AbstractUserRole):
    available_permissions = {
        'cadastrar_professores': True,
        'cadastrar_alunos': True,
        'deletar_professores': True,
        'deletar_alunos': True,
        'definir_horarios': True,
        'cadastrar_turma': True,
        'editar_turma': True,
        'deletar_turmas': True,
        'cadastrar_disciplinas': True,
        'deletar_disciplinas': True,
        'editar_disciplinas': True,
    }


class Professor(AbstractUserRole):
    available_permissions = {
        'cadastrar_aula': True,
        'editar_aula': True,
        'deletar_aula': True,
    }


class Aluno(AbstractUserRole):
    available_permissions = {
        'editar_aluno': True,
    }


class Admin(AbstractUserRole):
    available_permissions = {
    }