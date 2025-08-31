# 1. Fundamentos da Web

Este módulo cobre:
- Conceito de cliente/servidor
- HTTP: request, response, headers, status codes
- HTML básico e JSON
- Conceito de URL e rotas

## Exemplos
Veja o arquivo `fundamentos_web.py` para um servidor HTTP simples:
- Responde requisições GET com HTML
- Mostra headers e status code

## Como rodar
```bash
python web/fundamentos_web.py
```
Acesse `http://localhost:8080` no navegador.

## Explicação
- Cliente faz requisições HTTP para o servidor.
- Servidor responde com status, headers e corpo (HTML ou JSON).
- URLs identificam recursos e rotas.

Referência:
- [MDN – HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
