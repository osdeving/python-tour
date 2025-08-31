# 6. APIs Avançadas

Este módulo cobre:
- Documentação automática (Swagger/OpenAPI)
- Versionamento de APIs
- Paginação, filtros e ordenação
- Upload/download de arquivos

## Exemplos
Veja o arquivo `api_avancada.py` para um exemplo FastAPI:
- Paginação, filtro e ordenação via query params
- Upload de arquivos
- Documentação automática em `/docs` e `/redoc`

## Como rodar
1. Instale dependências:
   ```bash
   pip install fastapi uvicorn
   ```
2. Execute:
   ```bash
   uvicorn web.api_avancada:app --reload
   ```
3. Teste endpoints e acesse a documentação automática:
   - [http://localhost:8000/docs](http://localhost:8000/docs)
   - [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Explicação
- FastAPI gera documentação OpenAPI automaticamente.
- Paginação, filtros e ordenação são essenciais para APIs escaláveis.
- Upload/download de arquivos é comum em APIs modernas.

Referência:
- [OpenAPI Specification](https://swagger.io/specification/)
