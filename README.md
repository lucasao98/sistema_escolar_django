# Sistema de Gestão Institucional

Esse projeto objetiva a auxiliar a gestão institucional, seja ela ensino fundamental, médio, ensino superior,
e até escolas de idiomas, deixando para trás o atual sistema papel e caneta e partindo para a tecnologia.

## Tecnologias

- Django
- Sqlite3
- Html 5
- Css3
- Bootstrap v5.0

## Instalação
-Para executar o projeto em sua máquina primeiro faça o clone do projeto

- Em seguida execute:
```sh
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Após isso entre na pasta projeto_final

## Executando
Para executar o projeto em sua máquina rode o comando:

```sh
python manage.py migrate
```
Para executar as migrações. Após isso execute o projeto com comando:

```sh
python manage.py runserver
```
