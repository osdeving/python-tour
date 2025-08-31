# 1. Fundamentos de arquivos em Python

Este módulo cobre:
- Abrir arquivos com `open()`
- Modos de abertura (`r`, `w`, `a`, `x`, `b`, `+`)
- Uso de context manager (`with open(...) as f`)
- Leitura e escrita em arquivos de texto e binários

## Exemplos
Veja o arquivo `fundamentos.py` para exemplos práticos:
- Leitura e escrita de texto
- Escrita de binário

## Como rodar
```bash
python arquivos/fundamentos.py
```
(Adapte os exemplos conforme sua necessidade.)

## Explicação
- Sempre use o context manager para garantir fechamento do arquivo.
- Modos de abertura:
  - `r`: leitura
  - `w`: escrita (sobrescreve)
  - `a`: acrescenta
  - `x`: cria novo
  - `b`: binário
  - `+`: leitura/escrita

Referência: [Python Docs – Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
