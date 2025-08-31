# 4. Arquivos Grandes e Performance

Este módulo cobre:
- Leitura eficiente de arquivos grandes (linha a linha, chunks)
- Uso de `mmap` para acesso rápido
- Compressão e descompressão com `gzip`, `bz2`, `lzma`

## Exemplos
Veja o arquivo `arquivos_grandes.py` para funções práticas:
- `ler_linha_a_linha`: lê arquivo texto linha por linha
- `ler_em_chunks`: lê arquivo binário em blocos
- `ler_mmap`: acesso rápido via memória
- `comprimir_gzip` e `descomprimir_gzip`: compacta/descompacta arquivos

## Como rodar
```bash
python arquivos/arquivos_grandes.py
```
(Adapte os exemplos conforme sua necessidade.)

## Explicação
- Leitura streaming evita sobrecarregar a memória.
- Chunks são úteis para arquivos binários ou muito grandes.
- `mmap` permite manipular arquivos como se fossem arrays de bytes.
- Compressão reduz espaço em disco e facilita transferência.

Referências:
- [mmap](https://docs.python.org/3/library/mmap.html)
- [gzip](https://docs.python.org/3/library/gzip.html)
- [bz2](https://docs.python.org/3/library/bz2.html)
- [lzma](https://docs.python.org/3/library/lzma.html)
