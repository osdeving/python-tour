# 11. Logs e Persistência Simples

Este módulo cobre:
- Escrita contínua e rotativa de logs
- Persistência simples com `sqlite3` e `shelve`

## Exemplos
Veja o arquivo `logs_persistencia.py` para funções práticas:
- `configurar_log`: cria log simples
- `configurar_log_rotativo`: cria log com rotação
- `salvar_sqlite`: salva dados em banco SQLite
- `salvar_shelve`: salva dados em banco de chave-valor

## Como rodar
```bash
python arquivos/logs_persistencia.py
```
(Adapte os exemplos conforme sua necessidade.)

## Explicação
- Logging é essencial para monitorar aplicações.
- Rotação de logs evita arquivos gigantes.
- SQLite é banco leve, ideal para persistência local.
- Shelve é útil para persistir objetos Python simples.

Referências:
- [logging](https://docs.python.org/3/library/logging.html)
- [sqlite3](https://docs.python.org/3/library/sqlite3.html)
- [shelve](https://docs.python.org/3/library/shelve.html)
