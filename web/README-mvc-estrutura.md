# 4. MVC e Estrutura de Projetos

Este módulo cobre:
- Padrão MVC (Model, View, Controller)
- MVT no Django (Model, View, Template)
- Estrutura de projetos em Flask/FastAPI
- Separação de camadas (services, repos, controllers)

## Exemplos
- `mvc_flask.py`: exemplo MVC em Flask
- `mvt_django.py`: referência à estrutura MVT do Django
- `estrutura_fastapi.py`: exemplo de estrutura modular em FastAPI

## Como rodar
1. Instale dependências:
   ```bash
   pip install flask fastapi uvicorn django
   ```
2. Execute Flask:
   ```bash
   python web/mvc_flask.py
   ```
3. Execute FastAPI:
   ```bash
   uvicorn main:app --reload
   ```
4. Para Django, crie projeto:
   ```bash
   django-admin startproject exemplo_django
   ```

## Explicação
- MVC separa dados, lógica e apresentação.
- Django usa MVT, separando templates das views.
- FastAPI incentiva modularização por routers.

Referências:
- [MVC](https://developer.mozilla.org/en-US/docs/Glossary/MVC)
- [Django MVT](https://docs.djangoproject.com/en/4.0/topics/http/views/)
