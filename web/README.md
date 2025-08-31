# Guia rápido: Web com Flask

Este diretório contém exemplos de código para criar aplicações web em Python usando Flask.

## Estrutura dos arquivos
- `app.py`: Aplicação principal Flask.
- `blueprint.py`: Exemplo de uso de Blueprint para modularizar rotas.

## Como rodar os exemplos

1. Instale o Flask:
   ```bash
   pip install flask
   ```
2. Execute a aplicação principal:
   ```bash
   python web/app.py
   ```
   Acesse `http://localhost:5000` no navegador.

3. Para usar o Blueprint, importe e registre no `app.py`:
   ```python
   from blueprint import bp
   app.register_blueprint(bp)
   ```
   Acesse `http://localhost:5000/hello`.

## Explicação
- O Flask é um microframework para web em Python.
- Blueprints permitem organizar rotas e funcionalidades em módulos.

Consulte os arquivos para exemplos práticos e adapte conforme sua necessidade.
