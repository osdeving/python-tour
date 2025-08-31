# 🌐 Roadmap – Desenvolvimento Web em Python (APIs, MVC e além)

> Guia prático para aprender desenvolvimento web com Python.  
> Use os checkboxes `[ ]` para acompanhar seu progresso.

---

## 📑 Table of Contents
- [1. Fundamentos da Web](#1-fundamentos-da-web)
- [2. HTTP e REST](#2-http-e-rest)
- [3. Frameworks Web em Python](#3-frameworks-web-em-python)
- [4. MVC e Estrutura de Projetos](#4-mvc-e-estrutura-de-projetos)
- [5. APIs REST](#5-apis-rest)
- [6. APIs Avançadas](#6-apis-avançadas)
- [7. Bancos de Dados e ORM](#7-bancos-de-dados-e-orm)
- [8. Autenticação e Autorização](#8-autenticação-e-autorização)
- [9. Frontend + Backend](#9-frontend--backend)
- [10. Testes e Qualidade](#10-testes-e-qualidade)
- [11. Segurança em Aplicações Web](#11-segurança-em-aplicações-web)
- [12. Deploy e Produção](#12-deploy-e-produção)
- [13. Ferramentas e Boas Práticas](#13-ferramentas-e-boas-práticas)

---

## 1. Fundamentos da Web
- [ ] O que é cliente/servidor  
- [ ] HTTP (request, response, headers, status codes)  
- [ ] HTML básico e JSON  
- [ ] Conceito de URL e rotas  

🔗 Referência: [MDN – HTTP Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)

---

## 2. HTTP e REST
- [ ] Métodos HTTP (`GET`, `POST`, `PUT`, `DELETE`, `PATCH`)  
- [ ] Status codes (2xx, 3xx, 4xx, 5xx)  
- [ ] RESTful APIs – boas práticas  
- [ ] Versionamento de API  

🔗 Referência: [restfulapi.net](https://restfulapi.net/)

---

## 3. Frameworks Web em Python
- [ ] Flask (minimalista)  
- [ ] FastAPI (foco em APIs rápidas, async, OpenAPI)  
- [ ] Django (completo, MVC, ORM integrado)  
- [ ] Comparação: quando usar cada um  

🔗 Referências: [Flask](https://flask.palletsprojects.com/), [FastAPI](https://fastapi.tiangolo.com/), [Django](https://www.djangoproject.com/)

---

## 4. MVC e Estrutura de Projetos
- [ ] Padrão MVC (Model, View, Controller)  
- [ ] MVT no Django (Model, View, Template)  
- [ ] Estrutura de projetos em Flask/FastAPI  
- [ ] Separação de camadas (services, repos, controllers)  

---

## 5. APIs REST
- [ ] Rotas e endpoints  
- [ ] Query params, path params, body  
- [ ] Validação de entrada (`pydantic`)  
- [ ] Serialização de saída (JSON, schemas)  

---

## 6. APIs Avançadas
- [ ] Documentação automática (Swagger/OpenAPI)  
- [ ] Versionamento de APIs  
- [ ] Paginação, filtros e ordenação  
- [ ] Upload/download de arquivos  

🔗 Referência: [OpenAPI Specification](https://swagger.io/specification/)

---

## 7. Bancos de Dados e ORM
- [ ] Conexão com bancos (`sqlite3`, `psycopg2`, `mysqlclient`)  
- [ ] ORMs: SQLAlchemy, Django ORM, Tortoise ORM  
- [ ] Migrations (`alembic`, `django-migrations`)  
- [ ] Padrão Repository  

---

## 8. Autenticação e Autorização
- [ ] Cookies e sessões  
- [ ] JWT (JSON Web Tokens)  
- [ ] OAuth2 (Authorization Code, Password Flow)  
- [ ] Autorização baseada em papéis (RBAC)  

🔗 Referência: [OAuth2 RFC](https://datatracker.ietf.org/doc/html/rfc6749)

---

## 9. Frontend + Backend
- [ ] Servindo HTML (templates Jinja2, Django Templates)  
- [ ] APIs para frontend SPA (React, Vue, Angular)  
- [ ] CORS (Cross-Origin Resource Sharing)  
- [ ] Integração com Next.js, Nuxt ou similares  

---

## 10. Testes e Qualidade
- [ ] Testes unitários (`pytest`)  
- [ ] Testes de integração (HTTPX, TestClient)  
- [ ] Mock de requests (`responses`)  
- [ ] Linters e formatadores (Black, Flake8, Ruff)  

---

## 11. Segurança em Aplicações Web
- [ ] CSRF, XSS, SQL Injection  
- [ ] Rate limiting (evitar brute force)  
- [ ] Hash de senhas (`bcrypt`, `argon2`)  
- [ ] Helmet para headers HTTP (via middlewares)  

🔗 Referência: [OWASP Top 10](https://owasp.org/Top10/)

---

## 12. Deploy e Produção
- [ ] WSGI vs ASGI  
- [ ] Gunicorn, Uvicorn, Daphne  
- [ ] Docker para empacotar apps  
- [ ] CI/CD (GitHub Actions, GitLab CI, etc.)  
- [ ] Deploy em serviços (Heroku, Railway, Vercel, AWS, GCP, Azure)  

---

## 13. Ferramentas e Boas Práticas
- [ ] Estrutura de pastas limpa (src layout)  
- [ ] Arquivos `.env` e `pydantic-settings`  
- [ ] Logs estruturados (`logging`, `structlog`)  
- [ ] Monitoramento (Prometheus, Grafana, Sentry)  

---
