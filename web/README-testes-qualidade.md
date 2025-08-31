# 10. Testes e Qualidade

Este módulo cobre:
- Testes unitários (pytest)
- Testes de integração (HTTPX, TestClient)
- Mock de requests (responses)
- Linters e formatadores (Black, Flake8, Ruff)

## Exemplos
- `test_flask.py`: teste unitário Flask
- `test_fastapi.py`: teste integração FastAPI
- `test_django.py`: referência a testes Django

## Como rodar
1. Instale dependências:
   ```bash
   pip install pytest fastapi flask
   ```
2. Execute pytest:
   ```bash
   pytest web/test_flask.py
   pytest web/test_fastapi.py
   ```
3. Para Django:
   ```bash
   python manage.py test
   ```
4. Para linters/formatadores:
   ```bash
   pip install black flake8 ruff
   black web/
   flake8 web/
   ruff web/
   ```

## Explicação
- Testes garantem qualidade e evitam regressões.
- Linters/formatadores mantêm o código limpo.

Referências:
- [pytest](https://docs.pytest.org/)
- [Black](https://black.readthedocs.io/)
- [Flake8](https://flake8.pycqa.org/)
- [Ruff](https://docs.astral.sh/ruff/)
