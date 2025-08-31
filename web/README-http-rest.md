# 2. HTTP e REST

Este módulo cobre:
- Métodos HTTP: GET, POST, PUT, DELETE, PATCH
- Status codes (2xx, 3xx, 4xx, 5xx)
- Boas práticas de APIs RESTful
- Versionamento de API

## Exemplos
Veja o arquivo `http_rest.py` para um exemplo de API REST:
- Endpoint `/api/resource` aceita todos os métodos HTTP
- Retorna status code apropriado para cada método

## Como rodar
1. Instale o Flask:
   ```bash
   pip install flask
   ```
2. Execute:
   ```bash
   python web/http_rest.py
   ```
3. Teste com curl ou Postman:
   ```bash
   curl -X GET http://localhost:5000/api/resource
   curl -X POST http://localhost:5000/api/resource
   # etc
   ```

## Explicação
- Cada método HTTP tem um propósito (GET: leitura, POST: criação, etc).
- Status codes indicam sucesso, erro ou redirecionamento.
- APIs RESTful devem ser previsíveis e seguir convenções.
- Versionamento pode ser feito via URL (`/v1/resource`).

Referência:
- [restfulapi.net](https://restfulapi.net/)
