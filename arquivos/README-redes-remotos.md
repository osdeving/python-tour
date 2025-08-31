# 10. Redes e Arquivos Remotos

Este módulo cobre:
- Download de arquivos via HTTP (requests)
- Download via FTP/SFTP
- Referência a cloud storage (S3/GCS/Azure)

## Exemplos
Veja o arquivo `redes_remotos.py` para funções práticas:
- `baixar_arquivo_http`: baixa arquivo de uma URL
- `baixar_arquivo_ftp`: baixa arquivo via FTP
- `baixar_arquivo_sftp`: baixa arquivo via SFTP

## Como rodar
1. Instale dependências:
   ```bash
   pip install requests paramiko
   ```
2. Execute exemplos adaptando conforme sua necessidade:
   ```bash
   python arquivos/redes_remotos.py
   ```

## Explicação
- HTTP é o método mais comum para baixar arquivos.
- FTP/SFTP são usados para servidores de arquivos.
- Para cloud storage, use bibliotecas específicas (boto3, gcsfs, azure-storage-blob).

Referências:
- [requests](https://requests.readthedocs.io/)
- [ftplib](https://docs.python.org/3/library/ftplib.html)
- [paramiko](https://docs.paramiko.org/)
