# 5. APIs REST

Este módulo cobre:
- Rotas e endpoints
- Query params, path params, body
- Validação de entrada (pydantic)
- Serialização de saída (JSON, schemas)

## Exemplos
Veja o arquivo `api_rest.py` para um exemplo FastAPI:
- Endpoint GET com path param e query param
- Endpoint POST com validação de entrada

## Como rodar
1. Instale dependências:
   ```bash
   pip install fastapi uvicorn pydantic
   ```
2. Execute:
   ```bash
   uvicorn web.api_rest:app --reload
   ```
3. Teste com curl ou HTTPie:
   ```bash
   http GET http://localhost:8000/items/1?q=teste
   http POST http://localhost:8000/items/ name=Caneta price:=2.5
   ```

## Explicação
- Path params identificam recursos.
- Query params filtram ou modificam resultados.
- Body recebe dados estruturados.
- Pydantic valida e serializa dados automaticamente.

Referência:
- [FastAPI](https://fastapi.tiangolo.com/tutorial/path-params/)
- [Pydantic](https://docs.pydantic.dev/)
