# 9. Dados Tabulares e Binários Estruturados

Este módulo cobre:
- Manipulação de dados binários com `struct`
- Serialização de objetos com `pickle`
- Leitura e escrita de arquivos Excel com `pandas`/`openpyxl`

## Exemplos
Veja o arquivo `tabulares_binarios.py` para funções práticas:
- `escrever_binario` e `ler_binario`: manipulação binária
- `salvar_pickle` e `ler_pickle`: serialização de objetos
- `ler_excel` e `escrever_excel`: manipulação de planilhas Excel

## Como rodar
1. Instale dependências:
   ```bash
   pip install pandas openpyxl
   ```
2. Execute exemplos adaptando conforme sua necessidade:
   ```bash
   python arquivos/tabulares_binarios.py
   ```

## Explicação
- `struct` permite manipular dados binários de baixo nível.
- `pickle` facilita salvar e carregar objetos Python.
- `pandas` e `openpyxl` são poderosos para manipular dados tabulares e planilhas.

Referências:
- [struct](https://docs.python.org/3/library/struct.html)
- [pickle](https://docs.python.org/3/library/pickle.html)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
