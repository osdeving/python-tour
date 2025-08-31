# 6. Controle e Segurança

Este módulo cobre:
- Tratamento de exceções ao manipular arquivos
- Escrita segura usando arquivos temporários
- Permissões de arquivos
- File locking (bloqueio de arquivos)

## Exemplos
Veja o arquivo `controle_seguranca.py` para funções práticas:
- `ler_arquivo_seguro`: leitura com tratamento de erros
- `escrita_segura`: escrita atômica
- `alterar_permissao` e `info_permissao`: manipulação de permissões
- `lock_arquivo`: bloqueio de arquivo (Unix)

## Como rodar
```bash
python arquivos/controle_seguranca.py
```
(Adapte os exemplos conforme sua necessidade.)

## Explicação
- Sempre trate exceções para evitar falhas inesperadas.
- Escrita segura evita corrupção de dados.
- Permissões controlam acesso e segurança.
- File locking previne concorrência indesejada.

Referências:
- [os](https://docs.python.org/3/library/os.html)
- [stat](https://docs.python.org/3/library/stat.html)
- [fcntl](https://docs.python.org/3/library/fcntl.html)
