# 7. Bancos de Dados e ORM

Este módulo cobre:
- Conexão com bancos (sqlite3, psycopg2, mysqlclient)
- ORMs: SQLAlchemy, Django ORM, Tortoise ORM
- Migrations (alembic, django-migrations)
- Padrão Repository

## Exemplos
- `orm_sqlalchemy.py`: exemplo SQLAlchemy com SQLite
- `orm_django.py`: referência ao Django ORM
- `migrations_alembic.py`: referência a migrations com Alembic

## Como rodar
1. Instale dependências:
   ```bash
   pip install sqlalchemy alembic django
   ```
2. Execute SQLAlchemy:
   ```bash
   python web/orm_sqlalchemy.py
   ```
3. Para Django, crie projeto:
   ```bash
   django-admin startproject exemplo_django
   ```
4. Para Alembic:
   ```bash
   alembic init alembic
   ```

## Explicação
- ORMs facilitam manipulação de bancos sem SQL direto.
- Migrations automatizam mudanças de schema.
- Padrão Repository separa lógica de acesso a dados.

Referências:
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Django ORM](https://docs.djangoproject.com/en/4.0/topics/db/models/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
