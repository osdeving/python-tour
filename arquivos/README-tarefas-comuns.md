# 8. Tarefas Comuns

Este módulo cobre:
- Buscar arquivos usando glob
- Buscar e substituir texto em múltiplos arquivos
- Deduplicar e filtrar linhas
- Concatenar arquivos grandes
- Converter formatos (CSV ↔ JSON)

## Exemplos
Veja o arquivo `tarefas_comuns.py` para funções práticas:
- `buscar_arquivos`: busca arquivos por padrão
- `buscar_substituir`: busca e substitui texto
- `deduplicar_arquivo`: remove linhas duplicadas
- `concatenar_arquivos`: junta arquivos grandes
- `csv_para_json`: converte CSV para JSON

## Como rodar
```bash
python arquivos/tarefas_comuns.py
```
(Adapte os exemplos conforme sua necessidade.)

## Explicação
- glob permite buscar arquivos por padrão (ex: *.txt)
- Manipulação de texto em múltiplos arquivos é útil para automação
- Deduplicação evita dados repetidos
- Conversão de formatos facilita integração

Referência:
- [glob](https://docs.python.org/3/library/glob.html)
