# 13. Ferramentas e Boas Práticas

Este módulo cobre:
- Estrutura de pastas limpa (src layout)
- Arquivos .env e pydantic-settings
- Logs estruturados (structlog)
- Monitoramento (Prometheus, Grafana, Sentry)

## Exemplos
- `estrutura_pastas.py`: sugestão de layout
- `env_settings.py`: uso de .env e pydantic-settings
- `logs_structlog.py`: logs estruturados
- `monitoramento.py`: referência a monitoramento

## Como rodar
1. Instale dependências:
   ```bash
   pip install pydantic-settings structlog sentry-sdk prometheus-fastapi-instrumentator
   ```
2. Adapte exemplos conforme seu projeto.

## Explicação
- Estrutura organizada facilita manutenção.
- .env centraliza configurações sensíveis.
- Logs estruturados facilitam análise e monitoramento.
- Ferramentas de monitoramento ajudam na observabilidade.

Referências:
- [Structlog](https://www.structlog.org/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [Sentry](https://sentry.io/welcome/)
